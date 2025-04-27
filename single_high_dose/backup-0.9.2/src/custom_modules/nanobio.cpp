/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./nanobio.h"

// declare cell definitions here 

// Cell_Definition tumor_cell; 

void create_cell_types( void )
{
	// use the same random seed so that future experiments have the 
	// same initial histogram of oncoprotein, even if threading means 
	// that future division and other events are still not identical 
	// for all runs 
	
	SeedRandom( parameters.ints("random_seed") ); // or specify a seed here 
	
	// housekeeping 
	
	initialize_default_cell_definition();
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment ); 
	
	// turn the default cycle model to live, 
	// so it's easier to turn off proliferation
	cell_defaults.phenotype.cycle.sync_to_cycle_model( live ); 
	
	
	// Make sure we're ready for 2D
	cell_defaults.functions.set_orientation = up_orientation; 
	cell_defaults.phenotype.geometry.polarity = 1.0; 
	cell_defaults.phenotype.motility.restrict_to_2D = true; 
	
	// set functions 
	cell_defaults.functions.update_migration_bias = chemotaxis_function; 
	
	
	// use default proliferation and death 
	int cycle_start_index = live.find_phase_index( PhysiCell_constants::live ); 
	int cycle_end_index = live.find_phase_index( PhysiCell_constants::live ); 
	int apoptosis_index = cell_defaults.phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model ); 
	
	
	cell_defaults.parameters.o2_proliferation_saturation = parameters.doubles( "o2_proliferation_saturation" ); // 38.0; 
	cell_defaults.parameters.o2_proliferation_threshold = parameters.doubles( "o2_proliferation_threshold" ); // 5.0; 
	cell_defaults.parameters.o2_reference = parameters.doubles( "o2_reference" ); // 38.0; 
	
	
	// set default uptake and secretion 
	int oxygen_substrate_index = microenvironment.find_density_index( "oxygen" ); 
	cell_defaults.phenotype.secretion.secretion_rates[oxygen_substrate_index] = parameters.doubles( "oxygen_uptake_rate" ); // 10; 
	cell_defaults.phenotype.secretion.uptake_rates[oxygen_substrate_index] = parameters.doubles( "oxygen_secretion_rate" ); // 0; 
	cell_defaults.phenotype.secretion.saturation_densities[oxygen_substrate_index] = parameters.doubles( "oxygen_saturation_density" ); // 0; 
	
	int NP1_substrate_index = microenvironment.find_density_index( "NP1" ); 
	cell_defaults.phenotype.secretion.secretion_rates[NP1_substrate_index] = parameters.doubles( "NP1_uptake_rate" ); // 0; 
	cell_defaults.phenotype.secretion.uptake_rates[NP1_substrate_index] = parameters.doubles( "NP1_secretion_rate" ); // 0; 
	cell_defaults.phenotype.secretion.saturation_densities[NP1_substrate_index] = parameters.doubles( "NP1_saturation_density" ); // 0; 
	
	// modify the uptake rates for the NPs 
	cell_defaults.phenotype.secretion.uptake_rates[ NP1_substrate_index ] 
		= parameters.doubles( "internalization_rate" );  // r = 0.0058
	cell_defaults.phenotype.secretion.uptake_rates[ NP1_substrate_index ] 
		*= parameters.doubles( "relative_max_internal_concentration" );  // r*R = 0.0058 * 2.0
	
	
    // set reference phenotype properties cycling
	cell_defaults.phenotype.cycle.data.transition_rate( cycle_start_index ,cycle_end_index ) = parameters.doubles( "max_birth_rate" );  // 0.00072
		
	// mechanics 
	cell_defaults.phenotype.mechanics.cell_cell_adhesion_strength = parameters.doubles( "adhesion_strength" ); // 0.4; 
	cell_defaults.phenotype.mechanics.cell_cell_repulsion_strength = parameters.doubles( "repulsion_strength" ); // 10; 
	cell_defaults.phenotype.mechanics.relative_maximum_adhesion_distance = parameters.doubles( "max_relative_adhesion_distance" ); // 1.5; 
	
	// apoptosis 
	cell_defaults.phenotype.death.rates[apoptosis_index] = parameters.doubles( "apoptosis_rate" ); // 5.316666666666667e-5;  
	
	// necrosis 
	cell_defaults.parameters.max_necrosis_rate = parameters.doubles( "max_necrosis_rate" ); // 0.0027777777777778; 
	cell_defaults.parameters.necrosis_type = PhysiCell_constants::stochastic_necrosis;
	cell_defaults.parameters.o2_necrosis_threshold = parameters.doubles( "o2_necrosis_threshold" ); // 5; 
	cell_defaults.parameters.o2_necrosis_max = parameters.doubles( "o2_necrosis_max" ); // 2.5; 
	
	// motility 
	cell_defaults.phenotype.motility.migration_bias = parameters.doubles( "bias" ); // 0.25
	cell_defaults.phenotype.motility.migration_speed = parameters.doubles( "speed" ); // 1.1
	cell_defaults.phenotype.motility.persistence_time = parameters.doubles( "persistence_time" ); // 10.0; 
	cell_defaults.phenotype.motility.is_motile = parameters.bools( "is_motile" ); // false; 

	cell_defaults.custom_data.add_variable( "motility_gradient_substrate_index" , "dimensionless", 
		parameters.ints( "gradient_substrate_index" )  ); // 0
	cell_defaults.custom_data.add_variable( "negative_taxis" , "dimensionless", 
		parameters.bools( "negative_taxis" ) ); // false
	
	
	// update the phenotype function 
	cell_defaults.functions.update_phenotype = tumor_cell_phenotype_with_nanoparticle_response; 
	
	
	// Name the default cell type 
	cell_defaults.type = 0; 
	cell_defaults.name = "tumor cell"; 
		
		
	// In our model, turn default Ki67 to live model 
	// cell_defaults.phenotype.sync_to_functions( cell_defaults.functions ); 


	// add custom data here, if any 
	
	// create bins for storing NPs !!!
	std::vector<double> NPs_bin_tmp(100, 0.0);
	cell_defaults.custom_data.add_vector_variable( "NPs bins" , "dimensionless", NPs_bin_tmp );    
	cell_defaults.custom_data.add_variable( "Cell drug" , "dimensionless", 0.0 );
	cell_defaults.custom_data.add_variable( "Drug concentration" , "dimensionless", 0.0 );  // the concentration of drug in one cell
	cell_defaults.custom_data.add_variable( "Drug_concentration_AUC" , "dimensionless", 0.0 ); 
	cell_defaults.custom_data.add_variable( "Drug effect" , "dimensionless", 0.0 ); 
	cell_defaults.custom_data.add_variable( "Cell intern NPs" , "dimensionless", 0.0 ); // save the internalization NPs for every phenotype time

	// add proper custom variables to cell default for this NP1
	cell_defaults.custom_data.add_variable( "NP1" , "dimensionless" , 0.0 );
	cell_defaults.custom_data.add_variable( "NP1_AUC" , "dimensionless" , 0.0 );
	cell_defaults.custom_data.add_variable( "NP1 response" , "dimensionless" , 0.0 );
	cell_defaults.custom_data.add_variable( "NP1 effect" , "dimensionless" , 0.0 );

	
	return; 
}



void setup_microenvironment( void )
{
	
	// set domain parameters
	// parse domain parameters automatically from XML !!!!!
	
	
	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}

	 
	/*
	// in XML since version 1.6.0   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	// turn on gradients 
	default_microenvironment_options.calculate_gradients = ture; 
	
	// do not use oxygen as first substrate 
	default_microenvironment_options.use_oxygen_as_first_field = false; 
	
	
	// set Dirichlet conditions 
	default_microenvironment_options.outer_Dirichlet_conditions = true;
	
	
	// track the internalized_substrates
	default_microenvironment_options.track_internalized_substrates_in_each_agent == true;
	
	*/
	
	// put any custom code to set non-homogeneous initial conditions or 
	// extra Dirichlet nodes here. 
	
	// initialize BioFVM 
	
	initialize_microenvironment(); 	
	
	
	return; 
}

void setup_tissue( void )
{
	// create some cells near the origin
	pugi::xml_node node = xml_find_node( physicell_config_root , "domain" );
	
	double cell_radius = cell_defaults.phenotype.geometry.radius; 
	double cell_spacing = 0.95 * 2.0 * cell_radius; 
	
	double tumor_radius = parameters.doubles( "tumor_radius" ); // 250
	
	Cell* pCell = NULL; 
	
	double center_x = 0.5*(  xml_get_double_value( node , "x_min" ) + xml_get_double_value( node , "x_max" ) );
	double center_y = 0.5*(  xml_get_double_value( node , "y_min" ) + xml_get_double_value( node , "y_max" ) );
		
	double x = 0; 
	double x_outer =  tumor_radius; 
	double y = 0; 
	
	int n = 0; 
	while( y < tumor_radius )
	{
		x = 0; 
		if( n % 2 == 1 )
		{ x = 0.5*cell_spacing; }
		x_outer = sqrt( tumor_radius*tumor_radius - y*y ); 
		
		while( x < x_outer )
		{
			pCell = create_cell(); // tumor cell 
			pCell->assign_position( center_x+x , center_y+y , 0.0 );

			
			if( fabs( y ) > 0.01 )
			{
				pCell = create_cell(); // tumor cell 
				pCell->assign_position( center_x+x , center_y-y , 0.0 );

			}
			
			if( fabs( x ) > 0.01 )
			{ 
				pCell = create_cell(); // tumor cell 
				pCell->assign_position( center_x-x , center_y+y , 0.0 );

				
				if( fabs( y ) > 0.01 )
				{
					pCell = create_cell(); // tumor cell 
					pCell->assign_position( center_x-x , center_y-y , 0.0 );

				}
			}
			x += cell_spacing; 
			
		}
		
		y += cell_spacing * sqrt(3.0)/2.0; 
		n++; 
	}
	
	return; 
}


std::vector<std::string> nanobio_coloring_function( Cell* pCell )
{
	
	static bool color_initialized = false; 
	static int custom_data_index = 0;
	static double blue_value = 0; 
	static double yellow_value = 1; 
	static double diff = 1.0; 
	
	if( color_initialized == false )
	{
		pugi::xml_node node = xml_find_node( physicell_config_root , "visualization" ); 
		custom_data_index = xml_get_int_value( node , "custom_data_index" ); 
		blue_value = xml_get_double_value( node , "blue_value" ); 
		yellow_value = xml_get_double_value( node , "yellow_value" ); 
		
		diff = yellow_value - blue_value; 
		
		
		std::cout << "Shading cells according to custom varaiable " 
			<< custom_data_index << " : " 
			<< pCell->custom_data.variables[ custom_data_index ].name << std::endl; 
		std::cout << "\tIf this is not what you expect, change: " << std::endl << std::endl 
			<< "\t<visualization>\n\t\t<custom_data_index />\n\t</visualization>" 
			<< std::endl << std::endl;  
		
		color_initialized = true; 
	}
	
	// immune are black
	std::vector< std::string > output( 4, "black" ); 
	
	if( pCell->type == 1 )
	{ return output; } 
	
	// live cells are green, but shaded by internal NP value 
	if( pCell->phenotype.death.dead == false )
	{
		// nanobio_parameters.NP_preform_PD.cell_NP_i; 
		
		double scaled_value = pCell->custom_data[custom_data_index];
		
		scaled_value -= blue_value; 
		scaled_value /= diff;

		if( scaled_value > 1.0 )
		{ scaled_value = 1.0; } 
		if( scaled_value < 0.0 )
		{ scaled_value = 0.0; } 
		
		int SV = (int) round( scaled_value * 255.0 ); 
		
		char szTempString [128];
		sprintf( szTempString , "rgb(%u,%u,%u)", SV, SV, 255-SV );
		output[0].assign( szTempString );
		output[1].assign( szTempString );

		sprintf( szTempString , "rgb(%u,%u,%u)", (int)round(output[0][0]/2.0) , (int)round(output[0][1]/2.0) , (int)round(output[0][2]/2.0) );
		output[2].assign( szTempString );
		
		return output; 
	}

	// if not, dead colors 
	
	if (pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::apoptotic )  // Apoptotic - Red
	{
		output[0] = "rgb(255,0,0)";
		output[2] = "rgb(125,0,0)";
	}
	
	// Necrotic - Brown
	if( pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic_swelling || 
		pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic_lysed || 
		pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic )
	{
		output[0] = "rgb(250,138,38)";
		output[2] = "rgb(139,69,19)";
	}	
	
	return output; 


}


// cell phenotype function 
void tumor_cell_phenotype_with_nanoparticle_response( Cell* pCell, Phenotype& phenotype, double dt )
{
	// supported cycle models:
	// advanced_Ki67_cycle_model= 0;
	// basic_Ki67_cycle_model=1
	// live_cells_cycle_model = 5; 
	
	if( phenotype.death.dead == true )
	{ return; }
	
	// set up shortcuts to find the Q and K(1) phases (assuming Ki67 basic or advanced model)
	static bool indices_initiated = false; 
	static int start_phase_index; // Q_phase_index; 
	static int end_phase_index; // K_phase_index;
	static int necrosis_index; 
	static int apoptosis_index; 
	
	static int oxygen_i = pCell->get_microenvironment()->find_density_index( "oxygen" ); 
	
	if( indices_initiated == false )
	{
		// Ki67 models
		
		if( phenotype.cycle.model().code == PhysiCell_constants::advanced_Ki67_cycle_model || 
			phenotype.cycle.model().code == PhysiCell_constants::basic_Ki67_cycle_model )
		{
			start_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::Ki67_negative );
			necrosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::necrosis_death_model ); 
			apoptosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model );  
			
			if( phenotype.cycle.model().code == PhysiCell_constants::basic_Ki67_cycle_model )
			{
				end_phase_index = 
					phenotype.cycle.model().find_phase_index( PhysiCell_constants::Ki67_positive );
				indices_initiated = true; 
			}
			if( phenotype.cycle.model().code == PhysiCell_constants::advanced_Ki67_cycle_model )
			{
				end_phase_index = 
					phenotype.cycle.model().find_phase_index( PhysiCell_constants::Ki67_positive_premitotic );
				indices_initiated = true; 
			}
		}
		
		// live model 
			
		if( phenotype.cycle.model().code ==  PhysiCell_constants::live_cells_cycle_model )
		{
			start_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live );
			necrosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::necrosis_death_model ); 
			apoptosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model );  
			
			end_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live );
			indices_initiated = true; 
		}
		
		// cytometry models 
		
		if( phenotype.cycle.model().code == PhysiCell_constants::flow_cytometry_cycle_model || 
			phenotype.cycle.model().code == PhysiCell_constants::flow_cytometry_separated_cycle_model )
		{
			start_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::G0G1_phase );
			necrosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::necrosis_death_model ); 
			apoptosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model );  

			end_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::S_phase );
			indices_initiated = true; 
		}		
		
	}
	
	// don't continue if we never "figured out" the current cycle model. 
	if( indices_initiated == false )
	{
		return; 
	}
	
	// sample the microenvironment to get the pO2 value 
	double pO2 = (pCell->nearest_density_vector())[oxygen_i]; 
		
	int n = pCell->phenotype.cycle.current_phase_index(); 
	
	// function:
	// birth_rate_max*(  r1*(pO2-pO2_min)/(pO2_ref-pO2_min)*g + r2*(g-g_min)/(g_ref-g_min) ); 
	// mult_o2 = max( 0 , min( (pO2-pO2_min)/(pO2_ref-pO2_min) , 1 ))
	// mult_g = max( 0, mind( (g-g_min)/(g_ref-g_min) ,1 ))
	// mult = ( r1*mult_o2*mult_g + r2*mult_g ); 
	
	// this multiplier is for linear interpolation of the oxygen value 
	double O2 = 1.0;
	if( pO2 < pCell->parameters.o2_proliferation_saturation )      // (pO2 - 5) / (38 - 5) !!!!!!!!!!
	{
		O2 = ( pO2 - pCell->parameters.o2_proliferation_threshold ) 
			/ ( pCell->parameters.o2_proliferation_saturation - pCell->parameters.o2_proliferation_threshold );
	}
	if( pO2 < pCell->parameters.o2_proliferation_threshold )
	{ 
		O2 = 0.0; 
	}
	
	double multiplier = O2; // O2 
	
	// now, update the appropriate cycle transition rate 
	// phenotype.cycle.data.transition_rate(start_phase_index,end_phase_index) = 0; // close off birth !!!!
	
	phenotype.cycle.data.transition_rate(start_phase_index,end_phase_index) = multiplier * 
		 pCell->parameters.pReference_live_phenotype->cycle.data.transition_rate(start_phase_index,end_phase_index);
	
	// Update necrosis rate
	multiplier = 0.0;
	if( pO2 < pCell->parameters.o2_necrosis_threshold )
	{
		multiplier = ( pCell->parameters.o2_necrosis_threshold - pO2 ) 
			/ ( pCell->parameters.o2_necrosis_threshold - pCell->parameters.o2_necrosis_max );
	}
	if( pO2 < pCell->parameters.o2_necrosis_max )
	{ 
		multiplier = 1.0; 
	}	
	
	// now, update the necrosis rate 
	
	pCell->phenotype.death.rates[necrosis_index] = multiplier * pCell->parameters.max_necrosis_rate; 
	
	// therapy response here! 
	
	
	// influx / efflux, effect
	static int effect_model_type = parameters.ints( "effect_model" ); // 0
	
	advance_internalization( pCell, phenotype , dt ); 
	
	if( effect_model_type == 0 )
	{  simple_effect_model( pCell, phenotype , dt ); }
	else
	{  AUC_effect_model( pCell, phenotype , dt ); }
	
	advance_PD_model( pCell, phenotype, dt );
	

	return;
	
}



// custom cell phenotype functions
void chemotaxis_function( Cell* pCell , Phenotype& phenotype , double dt )
{
	static int motility_gradient_substrate_index_i = pCell->custom_data.find_variable_index( "motility_gradient_substrate_index" ); 
	static int negative_taxis_i = pCell->custom_data.find_variable_index( "negative_taxis" ); 

	if( phenotype.motility.is_motile == false || phenotype.motility.migration_bias < 1e-5 )
	{ return; }		

	phenotype.motility.migration_bias_direction = pCell->nearest_gradient( (int) pCell->custom_data[motility_gradient_substrate_index_i] );
	normalize( &( phenotype.motility.migration_bias_direction ) );	
	if( (bool) pCell->custom_data[negative_taxis_i] )
	{ phenotype.motility.migration_bias_direction *= -1.0; }
	
	
	return;
}


void advance_internalization( Cell* pCell, Phenotype& phenotype , double dt )
{
	
	// check if turn on the active influx for NPs internalization dynamics
	static bool enable_active_influx = parameters.bools( "enable_active_influx" );  // true; 
	
	static double relative_max_internal_concentration = parameters.doubles( "relative_max_internal_concentration" );  // R = 2.0
	static double internalization_rate = parameters.doubles( "internalization_rate" );  // r = 0.0058
	
	static int cell_NP_i = pCell->custom_data.find_variable_index("NP1");
	// static int cell_NP_AUC_i = pCell->custom_data.find_variable_index("NP1_AUC"); 
	static int cell_Drug_i = pCell->custom_data.find_variable_index("Cell drug");  
    static int cell_Drug_concentraion_i = pCell->custom_data.find_variable_index("Drug concentration"); 
	static int Drug_concentration_AUC_i = pCell->custom_data.find_variable_index("Drug_concentration_AUC"); 
	
    static int BioFVM_substrate_ID = microenvironment.find_density_index( "NP1" );
	
	static double NPs_saturation = 6000; 
	
	if( enable_active_influx )     // considering the voxel and cell volume 
	{   

        double last_intern = pCell->custom_data[ cell_NP_i ]; // save the last step uptake NPs !!!!!!!
			
		double temp = internalization_rate; // r 
		temp *= (pCell->nearest_density_vector())[BioFVM_substrate_ID]; // r*rho 
		temp *= dt; // dt*r*rho 
		temp *= phenotype.volume.total;  // dt*r*rho*Vi  
		// std::cout << "phenotype.volume.total= " << phenotype.volume.total << std::endl; 
		
		pCell->custom_data[ cell_NP_i ] += temp; // n(i) = n(i-1) + dt*r*rho*Vi 
		temp /= NPs_saturation;  // dt*r*rho*Vi/n*   
		temp += 1.0;  // 1 + dt*r*rho*Vi/n* 
		pCell->custom_data[ cell_NP_i ] /= temp; // n(i) = ( n(i-1) + dt*r*rho*Vi )/( 1 + dt*r*rho*Vi/n* );
			// ==> (  n(i) - n(i-1) )/dt = r*( 1 - n(i)/n* ) * n(xi)  


        // double last_intern = pCell->custom_data["Cell intern NPs"]; 
        // pCell->custom_data["Cell intern NPs"] = pCell->phenotype.molecular.internalized_total_substrates[1] - last_intern;  
		
        pCell->custom_data["Cell intern NPs"] = pCell->custom_data[ cell_NP_i ] - last_intern;
		
		// set the tissue-level uptake parameter 
		double temp2 = pCell->custom_data[ cell_NP_i ]; // n(i)
		temp2 /= NPs_saturation;  // n(i)/n*
		phenotype.secretion.uptake_rates[BioFVM_substrate_ID] = 1.0; // 1.0 
		phenotype.secretion.uptake_rates[BioFVM_substrate_ID] -= temp2; // 1 - n(i)/n* 	
		phenotype.secretion.uptake_rates[BioFVM_substrate_ID] *= internalization_rate; // r*( 1- n(i)/n* )
	}
	
	else
	{
		// set the internal drug level equal to the extracellular value 
		 pCell->custom_data[ cell_NP_i ] = 	(pCell->nearest_density_vector())[BioFVM_substrate_ID]; 
		 
		// set the tissue-level uptake parameter 
		phenotype.secretion.uptake_rates[BioFVM_substrate_ID] = internalization_rate; // r
		phenotype.secretion.uptake_rates[BioFVM_substrate_ID] *= relative_max_internal_concentration; // r*R
	}
	
	// the concentration of drug in one cell
	pCell->custom_data[ cell_Drug_concentraion_i ] = pCell->custom_data[ cell_Drug_i ]; // c
	pCell->custom_data[ cell_Drug_concentraion_i ] /= phenotype.volume.total; // c/Vcell
	
	// update AUC 
	// pCell->custom_data[ cell_NP_AUC_i ] += dt* pCell->custom_data[ cell_NP_i ];
	pCell->custom_data[ Drug_concentration_AUC_i ] += dt* pCell->custom_data[ cell_Drug_concentraion_i ];

	
	return; 

}



void advance_PD_model( Cell* pCell, Phenotype& phenotype, double dt )
{
	
	static int start_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live );
	static int end_phase_index = phenotype.cycle.model().find_phase_index( PhysiCell_constants::live );	
	static int apoptosis_index = phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model );
	
	// static int cell_effect_i = pCell->custom_data.find_variable_index("NP1 effect");
	static int Drug_effect_i = pCell->custom_data.find_variable_index("Drug effect"); 
	
	static bool cycle_enabled = parameters.bools( "cycle" );  // false;
	static bool apoptosis_enabled = parameters.bools( "apoptosis" );  // false;
	static bool motility_enabled = parameters.bools( "motility" ); // false
	static bool mechanics_enabled = parameters.bools( "mechanics" ); // false
	static bool secretion_enabled = parameters.bools( "secretion" ); // false
	
	
	// cell cycle 
	
	if( cycle_enabled )
	{
		static double treat_max_birth_rate = parameters.doubles( "treat_max_birth_rate" );  // 0.00018	
		interpolate( 
			&(phenotype.cycle.data.transition_rate(start_phase_index,end_phase_index)) , // overwrite this
			phenotype.cycle.data.transition_rate(start_phase_index,end_phase_index) , // unperturbed 
			treat_max_birth_rate ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]  // interpolation parameter  
		); 
	}
	
	// apoptosis 
	
	if( apoptosis_enabled )
	{
		static double apoptosis_rate = parameters.doubles( "apoptosis_rate" );  // 5.316666666666667e-5
		static double treat_apoptosis_rate = parameters.doubles( "treat_apoptosis_rate" ); // 0.001
		
		interpolate( 
			&(phenotype.death.rates[apoptosis_index]) , // overwrite this
			apoptosis_rate , // unperturbed
			treat_apoptosis_rate ,  // max perturb    
			pCell->custom_data[ Drug_effect_i ] // interpolation parameter 
		); 
	}
	
		// motility 

	if( motility_enabled )
	{
		static double migration_bias = parameters.doubles( "bias" ); 
        static double treat_migration_bias = parameters.doubles( "treat_bias" );      		
		interpolate( 
			&(phenotype.motility.migration_bias) , // overwrite this
			migration_bias , // unperturbed
			treat_migration_bias ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]  // interpolation parameter  
		); 
		
		static double motility_speed = parameters.doubles( "speed" ); 
		static double treat_motility_speed = parameters.doubles( "treat_speed" ); 
		interpolate( 
			&(phenotype.motility.migration_speed) , // overwrite this
			motility_speed , // unperturbed
			treat_motility_speed ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]  // interpolation parameter  
		); 
		
		static double persistence_time = parameters.doubles( "persistence_time" ); 
		static double treat_persistence_time = parameters.doubles( "treat_persistence_time" ); 
		interpolate( 
			&(phenotype.motility.persistence_time) , // overwrite this
			persistence_time , // unperturbed
			treat_persistence_time ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]   // interpolation parameter  
		); 

		if( pCell->custom_data[ Drug_effect_i ] >= 0.5 )
		{
			static int motility_gradient_substrate_index_i = pCell->custom_data.find_variable_index( "motility_gradient_substrate_index" ); 
			static int negative_taxis_i = pCell->custom_data.find_variable_index( "negative_taxis" ); 
			
			phenotype.motility.is_motile = parameters.bools( "treat_is_motile" ); // true
			pCell->custom_data[motility_gradient_substrate_index_i] = parameters.doubles( "treat_gradient_substrate_index" );  // 0
			pCell->custom_data[negative_taxis_i] = parameters.bools( "treat_negative_taxis" ); // false
			
		}
		else
		{
			static int motility_gradient_substrate_index_i = pCell->custom_data.find_variable_index( "motility_gradient_substrate_index" ); 
			static int negative_taxis_i = pCell->custom_data.find_variable_index( "negative_taxis" ); 

			phenotype.motility.is_motile = parameters.bools( "is_motile" ); // false
			pCell->custom_data[motility_gradient_substrate_index_i] = parameters.doubles( "gradient_substrate_index" );  // 0
			pCell->custom_data[negative_taxis_i] = parameters.bools( "negative_taxis" ); // false
		}
	}
	
	if( mechanics_enabled )
	{
		static double max_relative_adhesion_distance = parameters.doubles( "max_relative_adhesion_distance" ); 
		static double treat_max_relative_adhesion_distance = parameters.doubles( "treat_max_relative_adhesion_distance" ); 
		interpolate( 
			&(phenotype.mechanics.relative_maximum_adhesion_distance) , // overwrite this
			max_relative_adhesion_distance , // unperturbed
			treat_max_relative_adhesion_distance ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]  // interpolation parameter  
		); 
		
		static double adhesion_strength = parameters.doubles( "adhesion_strength" ); 
		static double treat_adhesion_strength = parameters.doubles( "treat_adhesion_strength" ); 
		interpolate( 
			&(phenotype.mechanics.cell_cell_adhesion_strength) , // overwrite this
			adhesion_strength , // unperturbed
			treat_adhesion_strength ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]  // interpolation parameter  
		); 
		
		static double repulsion_strength = parameters.doubles( "repulsion_strength" ); 
		static double treat_repulsion_strength = parameters.doubles( "treat_repulsion_strength" ); 
		interpolate( 
			&(phenotype.mechanics.cell_cell_repulsion_strength) , // overwrite this
			repulsion_strength , // unperturbed
			treat_repulsion_strength ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]  // interpolation parameter  
		); 
	}


	if( secretion_enabled )
	{
		static std::vector<double> uptake_rates = { parameters.doubles( "oxygen_uptake_rate" ), parameters.doubles( "NP1_uptake_rate" ) }; 
		static std::vector<double> secretion_rates = { parameters.doubles( "oxygen_secretion_rate" ), parameters.doubles( "NP1_secretion_rate" ) }; 
		static std::vector<double> saturation_densities = { parameters.doubles( "oxygen_saturation_density" ), parameters.doubles( "NP1_saturation_density" ) }; 
		
		static std::vector<double> treat_uptake_rates = { parameters.doubles( "treat_oxygen_uptake_rate" ), parameters.doubles( "treat_NP1_uptake_rate" ) }; 
		static std::vector<double> treat_secretion_rates = { parameters.doubles( "treat_oxygen_secretion_rate" ), parameters.doubles( "treat_NP1_secretion_rate" ) }; 
		static std::vector<double> treat_saturation_densities = { parameters.doubles( "treat_oxygen_saturation_density" ), parameters.doubles( "treat_NP1_saturation_density" ) }; 
		
		// std::cout << "uptake_rates= " << uptake_rates << std::endl;  
		
		interpolate( 
			&(phenotype.secretion.uptake_rates) , // overwrite this
			uptake_rates , // unperturbed
			treat_uptake_rates ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ] // interpolation parameter  
		); 
		
		interpolate( 
			&(phenotype.secretion.secretion_rates) , // overwrite this
			secretion_rates , // unperturbed
			treat_secretion_rates ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ]  // interpolation parameter  
		); 
		
		interpolate( 
			&(phenotype.secretion.saturation_densities) , // overwrite this
			saturation_densities , // unperturbed
			treat_saturation_densities ,  // max perturb 
			pCell->custom_data[ Drug_effect_i ] // interpolation parameter  
		); 
	}
	
		
	return; 
}




// two types of effect model for NPs or drug 
void simple_effect_model( Cell* pCell, Phenotype& phenotype, double dt )
{	
	static int cell_Drug_concentraion_i = pCell->custom_data.find_variable_index("Drug concentration");    
	static int Drug_effect_i = pCell->custom_data.find_variable_index("Drug effect"); 
	static double EC_50 = parameters.doubles( "EC_50" ); // 0.5
	static double Hill_power =  parameters.doubles( "Hill_power" ); // 2
	
	pCell->custom_data[ Drug_effect_i ] = Hill_function( pCell->custom_data[ cell_Drug_concentraion_i ] , Hill_power , EC_50 ); 
	
	return;
}


void AUC_effect_model( Cell* pCell, Phenotype& phenotype, double dt )
{
	static int Drug_concentration_AUC_i = pCell->custom_data.find_variable_index("Drug_concentration_AUC");
	static int Drug_effect_i = pCell->custom_data.find_variable_index("Drug effect"); 
	static double EC_50 = parameters.doubles( "EC_50" ); // 0.5
	static double Hill_power =  parameters.doubles( "Hill_power" ); // 2
	
	pCell->custom_data[ Drug_effect_i ] = Hill_function( pCell->custom_data[ Drug_concentration_AUC_i ] , Hill_power , EC_50 ); 
	
	return;
}



// not use now !!!!!!!
void apply_therapies( void )  
{
	return; 
}



double Hill_function( double input, double Hill_power , double EC_50 )
{
	double temp = input; // c
	temp /= EC_50; // c/c0
	temp = std::pow( temp, Hill_power ); // (c/c0)^n 
	double output = temp; // (c/c0)^n
	temp += 1.0; // 1 + (c/c0)^n 
	output /= temp; // // (c/c0)^n / ( 1 + (c/c0)^n ) 
	
	return output; 	
}


// output = (1-param)*input1 + param*input2 ( 0 <= param <= 1 )
void interpolate( double* pOutput , double input1, double input2, double param )
{
	*pOutput = input2; // input2
	*pOutput -= input1; // input2-input1
	*pOutput *= param; // param*(input2-input1)
	*pOutput += input1; // input1 + param*(input2-input1) 
		// == (1-param)*input1 + param*input2 
		
	return; 
	
}
void interpolate( std::vector<double>* pOutput , std::vector<double>& input1, std::vector<double> input2, double param )
{
	*pOutput = input2; // input2
	*pOutput -= input1; // input2-input1
	*pOutput *= param; // param*(input2-input1)
	*pOutput += input1; // input1 + param*(input2-input1) 
		// == (1-param)*input1 + param*input2 
	
	return;
}




int m = 100; 
std::vector<double> C(m, 0.0);
std::vector<double> R(m, 0.0);
std::vector< std::vector<double> > mat(m, std::vector<double> (m, 0.0));
std::vector<double> change(m, 0.0);


// C is fixed with time, 
void create_fixed_var( void )  // compute the fixed global variables for NPs-bin  !!!!!!!!!!!!!
{
    for(int i = 0; i < m; i++)
	{
		C[i] = 1 - i*(1.0/m);    // using 1.0 instead of 1, conver int to float
	}
		
	return; 
}


double gamma1 = 0.00001; // 0.001
double gamma2 = 10000; 
double use_cell_drug_conc = 1.0;
double time_step = 0.01; 	
	
void NPs_drug_func( std::vector<double>* N, double& c, double cell_volume )
{
	#pragma omp critical
	{
	 for(int j = 0; j < m; j++)
	 {
		R[j] = gamma1 * ( gamma2 * C[j] - use_cell_drug_conc * c / cell_volume );    // gamma1 * ( gamma2 * C[j] - use_cell_drug_conc * c / Vcell)
		
		if( R[j] < 0 )
		{
			R[j] = 0.0;
		}	
	 }
	 
	 R[m-1] = 0;
	}
	
	
	// T(n) = O(n)
	#pragma omp critical
	{
	for( int ii = 0; ii < m; ii++ )      
	{
		mat[ii][ii] = -R[ii];    // row == col 
	}
	
	for( int jj = 1; jj < m; jj++ )  // starting from 2nd row 
	{
		mat[jj][jj-1] = R[jj-1];  // row == ( col + 1 )
	}
	}

	#pragma omp critical
	{
	for(int k = 0; k < m; k++)
	{
		c += time_step * R[k] * (*N)[k];          // custom data - drug !!!!!!!!!!!!
	}
	}
	
	// change matrix updated, so add #pragma omp critical for change matrix when parallelled 
	// T(n) = O(n)
	#pragma omp critical
	{
		change[0] = time_step * mat[0][0] * (*N)[0];
		for( int ii = 1; ii < m; ii++ )
		{
			change[ii] = time_step * ( mat[ii][ii-1] * (*N)[ii-1] + mat[ii][ii] * (*N)[ii] ); 			
		}
	}
	
	
	*N += change;   // vector N(t) = N(t-1) + change
		
	
	return;
		
}

void intern_NPs() // update the internalization NPs in the first bin 
{
	static double max_NPs = 100002.5; 
	
	#pragma omp parallel for
    for( int i=0; i < (*all_cells).size() ;i++ )
	{
		Cell* pCell;  
		pCell = (*all_cells)[i];  
		
		// if cell is dead, stop uptake
		if( pCell->phenotype.death.dead == true )
	    { continue; }
		
		double total_NPs = 0.0; 		
		for( int j = 0; j < m; j++ )
		{
			total_NPs += pCell->custom_data.vector_variables[0].value[j];
		}
		if( total_NPs < max_NPs )
		{
			pCell->custom_data.vector_variables[0].value[0] += pCell->custom_data["Cell intern NPs"]; 
			// pCell->phenotype.secretion.uptake_rates[4] * (pCell->nearest_density_vector())[0] * dt * pCell->phenotype.volume.total; 
			// cell_total volume = 2494 
		}	
    	  
		// pCell->custom_data.vector_variables[0].value[0] += pCell->phenotype.molecular.internalized_total_substrates[nps]; 
	}
	
	return; 
}


void PK_model()  // update the ODE of transition from 1st bin to last bin 
{
	#pragma omp parallel for
    for( int i=0; i < (*all_cells).size() ;i++ )	
	{    
        Cell* pCell;  // or (*all_cells)[0];
		pCell = (*all_cells)[i];  
		
		// if cell is dead, stop update
		if( pCell->phenotype.death.dead == true )
	    { continue; }
	    
		NPs_drug_func( &pCell->custom_data.vector_variables[0].value, pCell->custom_data[ "Cell drug" ], pCell->phenotype.volume.total );     // the 1st vector-variable 
		
		// pCell->custom_data.vector_variables[0].value[0] += pCell->phenotype.secretion.uptake_rates[4]*dt; 		
	}
	
	return; 
 
}

















