 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.tumor_radius = FloatText(
          value=250,
          step=10,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Background phenotype (without drug effect)---', disabled=True, layout=divider_button_layout)

        param_name3 = Button(description='oxygen_uptake_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.oxygen_uptake_rate = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='max_birth_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.max_birth_rate = FloatText(
          value=0.00072,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='o2_proliferation_saturation', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.o2_proliferation_saturation = FloatText(
          value=38,
          step=1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='o2_proliferation_threshold', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.o2_proliferation_threshold = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='o2_reference', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.o2_reference = FloatText(
          value=38,
          step=1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='max_necrosis_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'lightgreen'

        self.max_necrosis_rate = FloatText(
          value=0.0027777777777778,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name9 = Button(description='o2_necrosis_threshold', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        self.o2_necrosis_threshold = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='o2_necrosis_max', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'lightgreen'

        self.o2_necrosis_max = FloatText(
          value=2.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'tan'

        self.apoptosis_rate = FloatText(
          value=5.316666666666667e-5,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name12 = Button(description='is_motile', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'lightgreen'

        self.is_motile = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name13 = Button(description='bias', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'tan'

        self.bias = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name14 = Button(description='gradient_substrate_index', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'lightgreen'

        self.gradient_substrate_index = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='negative_taxis', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'tan'

        self.negative_taxis = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name16 = Button(description='speed', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'lightgreen'

        self.speed = FloatText(
          value=1.1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'tan'

        self.persistence_time = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='max_relative_adhesion_distance', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'lightgreen'

        self.max_relative_adhesion_distance = FloatText(
          value=1.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name19 = Button(description='adhesion_strength', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'tan'

        self.adhesion_strength = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='repulsion_strength', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'lightgreen'

        self.repulsion_strength = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Model parameters---', disabled=True, layout=divider_button_layout)

        param_name21 = Button(description='effect_model', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'tan'

        self.effect_model = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='EC_50', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'lightgreen'

        self.EC_50 = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name23 = Button(description='Hill_power', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'tan'

        self.Hill_power = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name24 = Button(description='enable_active_influx', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'lightgreen'

        self.enable_active_influx = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name25 = Button(description='relative_max_internal_concentration', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'tan'

        self.relative_max_internal_concentration = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name26 = Button(description='internalization_rate', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'lightgreen'

        self.internalization_rate = FloatText(
          value=0.0058,
          step=0.001,
          style=style, layout=widget_layout)

        param_name27 = Button(description='reference_external_concentration', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'tan'

        self.reference_external_concentration = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name28 = Button(description='cycle', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'lightgreen'

        self.cycle = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name29 = Button(description='apoptosis', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'tan'

        self.apoptosis = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name30 = Button(description='motility', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'lightgreen'

        self.motility = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name31 = Button(description='mechanics', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'tan'

        self.mechanics = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name32 = Button(description='secretion', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'lightgreen'

        self.secretion = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Maximum drug-induced phenotypic response---', disabled=True, layout=divider_button_layout)

        param_name33 = Button(description='treat_max_birth_rate', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'tan'

        self.treat_max_birth_rate = FloatText(
          value=0.00018,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name34 = Button(description='treat_o2_proliferation_saturation', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'lightgreen'

        self.treat_o2_proliferation_saturation = FloatText(
          value=38,
          step=1,
          style=style, layout=widget_layout)

        param_name35 = Button(description='treat_o2_proliferation_threshold', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'tan'

        self.treat_o2_proliferation_threshold = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name36 = Button(description='treat_o2_reference', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'lightgreen'

        self.treat_o2_reference = FloatText(
          value=38,
          step=1,
          style=style, layout=widget_layout)

        param_name37 = Button(description='treat_max_necrosis_rate', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'tan'

        self.treat_max_necrosis_rate = FloatText(
          value=0.0027777777777778,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name38 = Button(description='treat_o2_necrosis_threshold', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'lightgreen'

        self.treat_o2_necrosis_threshold = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name39 = Button(description='treat_o2_necrosis_max', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'tan'

        self.treat_o2_necrosis_max = FloatText(
          value=2.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name40 = Button(description='treat_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name40.style.button_color = 'lightgreen'

        self.treat_apoptosis_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name41 = Button(description='treat_is_motile', disabled=True, layout=name_button_layout)
        param_name41.style.button_color = 'tan'

        self.treat_is_motile = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name42 = Button(description='treat_bias', disabled=True, layout=name_button_layout)
        param_name42.style.button_color = 'lightgreen'

        self.treat_bias = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name43 = Button(description='treat_gradient_substrate_index', disabled=True, layout=name_button_layout)
        param_name43.style.button_color = 'tan'

        self.treat_gradient_substrate_index = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name44 = Button(description='treat_negative_taxis', disabled=True, layout=name_button_layout)
        param_name44.style.button_color = 'lightgreen'

        self.treat_negative_taxis = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name45 = Button(description='treat_speed', disabled=True, layout=name_button_layout)
        param_name45.style.button_color = 'tan'

        self.treat_speed = FloatText(
          value=1.1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name46 = Button(description='treat_persistence_time', disabled=True, layout=name_button_layout)
        param_name46.style.button_color = 'lightgreen'

        self.treat_persistence_time = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name47 = Button(description='treat_max_relative_adhesion_distance', disabled=True, layout=name_button_layout)
        param_name47.style.button_color = 'tan'

        self.treat_max_relative_adhesion_distance = FloatText(
          value=1.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name48 = Button(description='treat_adhesion_strength', disabled=True, layout=name_button_layout)
        param_name48.style.button_color = 'lightgreen'

        self.treat_adhesion_strength = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name49 = Button(description='treat_repulsion_strength', disabled=True, layout=name_button_layout)
        param_name49.style.button_color = 'tan'

        self.treat_repulsion_strength = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name50 = Button(description='treat_oxygen_uptake_rate', disabled=True, layout=name_button_layout)
        param_name50.style.button_color = 'lightgreen'

        self.treat_oxygen_uptake_rate = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'lightgreen'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'tan'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'lightgreen'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'tan'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'lightgreen'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'tan'
        units_button28 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'lightgreen'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'tan'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'lightgreen'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'tan'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'lightgreen'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'tan'
        units_button34 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'lightgreen'
        units_button35 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'
        units_button37 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'lightgreen'
        units_button38 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'tan'
        units_button39 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button39.style.button_color = 'lightgreen'
        units_button40 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button40.style.button_color = 'tan'
        units_button41 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button41.style.button_color = 'lightgreen'
        units_button42 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button42.style.button_color = 'tan'
        units_button43 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button43.style.button_color = 'lightgreen'
        units_button44 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button44.style.button_color = 'tan'
        units_button45 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button45.style.button_color = 'lightgreen'
        units_button46 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button46.style.button_color = 'tan'
        units_button47 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button47.style.button_color = 'lightgreen'
        units_button48 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button48.style.button_color = 'tan'
        units_button49 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button49.style.button_color = 'lightgreen'
        units_button50 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button50.style.button_color = 'tan'
        units_button51 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button51.style.button_color = 'lightgreen'
        units_button52 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button52.style.button_color = 'tan'
        units_button53 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button53.style.button_color = 'lightgreen'

        desc_button1 = Button(description='Initialize the random number generator' , tooltip='Initialize the random number generator', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='Initial tumor radius' , tooltip='Initial tumor radius', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='Uptake rate of oxygen' , tooltip='Uptake rate of oxygen', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button9 = Button(description='Maximum birth rate' , tooltip='Maximum birth rate', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='Oxygen value above which the proliferation rate is maximized' , tooltip='Oxygen value above which the proliferation rate is maximized', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='Oxygen value below which the proliferation ceases' , tooltip='Oxygen value below which the proliferation ceases', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='Oxygen value that corresponds to the reference phenotype' , tooltip='Oxygen value that corresponds to the reference phenotype', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='Maximum necrosis rate' , tooltip='Maximum necrosis rate', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Oxygen value at which necrosis starts' , tooltip='Oxygen value at which necrosis starts', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='Oxygen value at which necrosis reaches its maximum rate' , tooltip='Oxygen value at which necrosis reaches its maximum rate', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='Tumor background apoptosis rate' , tooltip='Tumor background apoptosis rate', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='Boolean variable that used to enable or disable cell motility' , tooltip='Boolean variable that used to enable or disable cell motility', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='Set the degree to which cell motility is biased along migration bias direction' , tooltip='Set the degree to which cell motility is biased along migration bias direction', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='The substrate index used for chemotaxis (0:NP1)' , tooltip='The substrate index used for chemotaxis (0:NP1)', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='Boolean variable that used to determine if go along grad(substrate[index])' , tooltip='Boolean variable that used to determine if go along grad(substrate[index])', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='Speed of motility' , tooltip='Speed of motility', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='Mean time cell continues at its current speed and direction before sampling the environment to choose a new motility direction' , tooltip='Mean time cell continues at its current speed and direction before sampling the environment to choose a new motility direction', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='Maximum distance of cell adhesion to other cells or a basement membrane (relative to cell radius)' , tooltip='Maximum distance of cell adhesion to other cells or a basement membrane (relative to cell radius)', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='Strength used to change cell-cell adhesive forces' , tooltip='Strength used to change cell-cell adhesive forces', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='Strength used to change cell-cell repulsion forces' , tooltip='Strength used to change cell-cell repulsion forces', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='Which treatment model used (0: Simple or 1: AUC)' , tooltip='Which treatment model used (0: Simple or 1: AUC)', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='Drug value that gives 50% of max effect' , tooltip='Drug value that gives 50% of max effect', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='Power used in the hill function for calculating drug effect' , tooltip='Power used in the hill function for calculating drug effect', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='Boolean variable used to enable or disable active model for uptaking NPs' , tooltip='Boolean variable used to enable or disable active model for uptaking NPs', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='Max ratio of internal concentration and reference external concentration for NPs' , tooltip='Max ratio of internal concentration and reference external concentration for NPs', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='NPs internalization rate' , tooltip='NPs internalization rate', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='Reference external NPs concentration' , tooltip='Reference external NPs concentration', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='Boolean variable for enable or disable cycle' , tooltip='Boolean variable for enable or disable cycle', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='Boolean variable for enable or disable apoptosis' , tooltip='Boolean variable for enable or disable apoptosis', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='Boolean variable for enable or disable motility' , tooltip='Boolean variable for enable or disable motility', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='Boolean variable for enable or disable mechanics' , tooltip='Boolean variable for enable or disable mechanics', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='Boolean variable for enable or disable secretion' , tooltip='Boolean variable for enable or disable secretion', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='Max drug effect on maximum birth rate' , tooltip='Max drug effect on maximum birth rate', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='Max drug effect on oxygen value above which the proliferation rate is maximized' , tooltip='Max drug effect on oxygen value above which the proliferation rate is maximized', disabled=True, layout=desc_button_layout) 
        desc_button39.style.button_color = 'lightgreen'
        desc_button40 = Button(description='Max drug effect on oxygen value below which the proliferation ceases' , tooltip='Max drug effect on oxygen value below which the proliferation ceases', disabled=True, layout=desc_button_layout) 
        desc_button40.style.button_color = 'tan'
        desc_button41 = Button(description='Max drug effect on oxygen value that corresponds to the reference phenotype' , tooltip='Max drug effect on oxygen value that corresponds to the reference phenotype', disabled=True, layout=desc_button_layout) 
        desc_button41.style.button_color = 'lightgreen'
        desc_button42 = Button(description='Max drug effect on maximum necrosis rate' , tooltip='Max drug effect on maximum necrosis rate', disabled=True, layout=desc_button_layout) 
        desc_button42.style.button_color = 'tan'
        desc_button43 = Button(description='Max drug effect on oxygen value at which necrosis starts' , tooltip='Max drug effect on oxygen value at which necrosis starts', disabled=True, layout=desc_button_layout) 
        desc_button43.style.button_color = 'lightgreen'
        desc_button44 = Button(description='Max drug effect on oxygen value at which necrosis reaches its maximum rate' , tooltip='Max drug effect on oxygen value at which necrosis reaches its maximum rate', disabled=True, layout=desc_button_layout) 
        desc_button44.style.button_color = 'tan'
        desc_button45 = Button(description='Max drug effect on tumor apoptosis rate' , tooltip='Max drug effect on tumor apoptosis rate', disabled=True, layout=desc_button_layout) 
        desc_button45.style.button_color = 'lightgreen'
        desc_button46 = Button(description='Max drug effect on boolean variable that used to enable or disable cell motility' , tooltip='Max drug effect on boolean variable that used to enable or disable cell motility', disabled=True, layout=desc_button_layout) 
        desc_button46.style.button_color = 'tan'
        desc_button47 = Button(description='Max drug effect on set the degree to which cell motility is biased along migration bias direction' , tooltip='Max drug effect on set the degree to which cell motility is biased along migration bias direction', disabled=True, layout=desc_button_layout) 
        desc_button47.style.button_color = 'lightgreen'
        desc_button48 = Button(description='Max drug effect on the substrate index used for chemotaxis (0:NP1)' , tooltip='Max drug effect on the substrate index used for chemotaxis (0:NP1)', disabled=True, layout=desc_button_layout) 
        desc_button48.style.button_color = 'tan'
        desc_button49 = Button(description='Max drug effect on boolean variable that used to determine if go along grad(substrate[index])' , tooltip='Max drug effect on boolean variable that used to determine if go along grad(substrate[index])', disabled=True, layout=desc_button_layout) 
        desc_button49.style.button_color = 'lightgreen'
        desc_button50 = Button(description='Max drug effect on speed of motility' , tooltip='Max drug effect on speed of motility', disabled=True, layout=desc_button_layout) 
        desc_button50.style.button_color = 'tan'
        desc_button51 = Button(description='Max drug effect on mean time cell continues at its current speed and direction before sampling the environment to choose a new motility direction' , tooltip='Max drug effect on mean time cell continues at its current speed and direction before sampling the environment to choose a new motility direction', disabled=True, layout=desc_button_layout) 
        desc_button51.style.button_color = 'lightgreen'
        desc_button52 = Button(description='Max drug effect on maximum distance of cell adhesion to other cells or a basement membrane (relative to cell radius)' , tooltip='Max drug effect on maximum distance of cell adhesion to other cells or a basement membrane (relative to cell radius)', disabled=True, layout=desc_button_layout) 
        desc_button52.style.button_color = 'tan'
        desc_button53 = Button(description='Max drug effect on strength used to change cell-cell adhesive forces' , tooltip='Max drug effect on strength used to change cell-cell adhesive forces', disabled=True, layout=desc_button_layout) 
        desc_button53.style.button_color = 'lightgreen'
        desc_button54 = Button(description='Max drug effect on strength used to change cell-cell repulsion forces' , tooltip='Max drug effect on strength used to change cell-cell repulsion forces', disabled=True, layout=desc_button_layout) 
        desc_button54.style.button_color = 'tan'
        desc_button55 = Button(description='Max drug effect on uptake rate of oxygen' , tooltip='Max drug effect on uptake rate of oxygen', disabled=True, layout=desc_button_layout) 
        desc_button55.style.button_color = 'lightgreen'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.tumor_radius, units_button2, desc_button2] 
        row3 = [param_name3, self.oxygen_uptake_rate, units_button4, desc_button3] 
        row9 = [param_name4, self.max_birth_rate, units_button5, desc_button9] 
        row10 = [param_name5, self.o2_proliferation_saturation, units_button6, desc_button10] 
        row11 = [param_name6, self.o2_proliferation_threshold, units_button7, desc_button11] 
        row12 = [param_name7, self.o2_reference, units_button8, desc_button12] 
        row13 = [param_name8, self.max_necrosis_rate, units_button9, desc_button13] 
        row14 = [param_name9, self.o2_necrosis_threshold, units_button10, desc_button14] 
        row15 = [param_name10, self.o2_necrosis_max, units_button11, desc_button15] 
        row16 = [param_name11, self.apoptosis_rate, units_button12, desc_button16] 
        row17 = [param_name12, self.is_motile, units_button13, desc_button17] 
        row18 = [param_name13, self.bias, units_button14, desc_button18] 
        row19 = [param_name14, self.gradient_substrate_index, units_button15, desc_button19] 
        row20 = [param_name15, self.negative_taxis, units_button16, desc_button20] 
        row21 = [param_name16, self.speed, units_button17, desc_button21] 
        row22 = [param_name17, self.persistence_time, units_button18, desc_button22] 
        row23 = [param_name18, self.max_relative_adhesion_distance, units_button19, desc_button23] 
        row24 = [param_name19, self.adhesion_strength, units_button20, desc_button24] 
        row25 = [param_name20, self.repulsion_strength, units_button21, desc_button25] 
        row26 = [param_name21, self.effect_model, units_button23, desc_button26] 
        row27 = [param_name22, self.EC_50, units_button24, desc_button27] 
        row28 = [param_name23, self.Hill_power, units_button25, desc_button28] 
        row29 = [param_name24, self.enable_active_influx, units_button26, desc_button29] 
        row30 = [param_name25, self.relative_max_internal_concentration, units_button27, desc_button30] 
        row31 = [param_name26, self.internalization_rate, units_button28, desc_button31] 
        row32 = [param_name27, self.reference_external_concentration, units_button29, desc_button32] 
        row33 = [param_name28, self.cycle, units_button30, desc_button33] 
        row34 = [param_name29, self.apoptosis, units_button31, desc_button34] 
        row35 = [param_name30, self.motility, units_button32, desc_button35] 
        row36 = [param_name31, self.mechanics, units_button33, desc_button36] 
        row37 = [param_name32, self.secretion, units_button34, desc_button37] 
        row38 = [param_name33, self.treat_max_birth_rate, units_button36, desc_button38] 
        row39 = [param_name34, self.treat_o2_proliferation_saturation, units_button37, desc_button39] 
        row40 = [param_name35, self.treat_o2_proliferation_threshold, units_button38, desc_button40] 
        row41 = [param_name36, self.treat_o2_reference, units_button39, desc_button41] 
        row42 = [param_name37, self.treat_max_necrosis_rate, units_button40, desc_button42] 
        row43 = [param_name38, self.treat_o2_necrosis_threshold, units_button41, desc_button43] 
        row44 = [param_name39, self.treat_o2_necrosis_max, units_button42, desc_button44] 
        row45 = [param_name40, self.treat_apoptosis_rate, units_button43, desc_button45] 
        row46 = [param_name41, self.treat_is_motile, units_button44, desc_button46] 
        row47 = [param_name42, self.treat_bias, units_button45, desc_button47] 
        row48 = [param_name43, self.treat_gradient_substrate_index, units_button46, desc_button48] 
        row49 = [param_name44, self.treat_negative_taxis, units_button47, desc_button49] 
        row50 = [param_name45, self.treat_speed, units_button48, desc_button50] 
        row51 = [param_name46, self.treat_persistence_time, units_button49, desc_button51] 
        row52 = [param_name47, self.treat_max_relative_adhesion_distance, units_button50, desc_button52] 
        row53 = [param_name48, self.treat_adhesion_strength, units_button51, desc_button53] 
        row54 = [param_name49, self.treat_repulsion_strength, units_button52, desc_button54] 
        row55 = [param_name50, self.treat_oxygen_uptake_rate, units_button53, desc_button55] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)
        box40 = Box(children=row40, layout=box_layout)
        box41 = Box(children=row41, layout=box_layout)
        box42 = Box(children=row42, layout=box_layout)
        box43 = Box(children=row43, layout=box_layout)
        box44 = Box(children=row44, layout=box_layout)
        box45 = Box(children=row45, layout=box_layout)
        box46 = Box(children=row46, layout=box_layout)
        box47 = Box(children=row47, layout=box_layout)
        box48 = Box(children=row48, layout=box_layout)
        box49 = Box(children=row49, layout=box_layout)
        box50 = Box(children=row50, layout=box_layout)
        box51 = Box(children=row51, layout=box_layout)
        box52 = Box(children=row52, layout=box_layout)
        box53 = Box(children=row53, layout=box_layout)
        box54 = Box(children=row54, layout=box_layout)
        box55 = Box(children=row55, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          div_row1,
          box3,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          div_row2,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          div_row3,
          box38,
          box39,
          box40,
          box41,
          box42,
          box43,
          box44,
          box45,
          box46,
          box47,
          box48,
          box49,
          box50,
          box51,
          box52,
          box53,
          box54,
          box55,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.oxygen_uptake_rate.value = float(uep.find('.//oxygen_uptake_rate').text)
        self.max_birth_rate.value = float(uep.find('.//max_birth_rate').text)
        self.o2_proliferation_saturation.value = float(uep.find('.//o2_proliferation_saturation').text)
        self.o2_proliferation_threshold.value = float(uep.find('.//o2_proliferation_threshold').text)
        self.o2_reference.value = float(uep.find('.//o2_reference').text)
        self.max_necrosis_rate.value = float(uep.find('.//max_necrosis_rate').text)
        self.o2_necrosis_threshold.value = float(uep.find('.//o2_necrosis_threshold').text)
        self.o2_necrosis_max.value = float(uep.find('.//o2_necrosis_max').text)
        self.apoptosis_rate.value = float(uep.find('.//apoptosis_rate').text)
        self.is_motile.value = ('true' == (uep.find('.//is_motile').text.lower()) )
        self.bias.value = float(uep.find('.//bias').text)
        self.gradient_substrate_index.value = int(uep.find('.//gradient_substrate_index').text)
        self.negative_taxis.value = ('true' == (uep.find('.//negative_taxis').text.lower()) )
        self.speed.value = float(uep.find('.//speed').text)
        self.persistence_time.value = float(uep.find('.//persistence_time').text)
        self.max_relative_adhesion_distance.value = float(uep.find('.//max_relative_adhesion_distance').text)
        self.adhesion_strength.value = float(uep.find('.//adhesion_strength').text)
        self.repulsion_strength.value = float(uep.find('.//repulsion_strength').text)
        self.effect_model.value = int(uep.find('.//effect_model').text)
        self.EC_50.value = float(uep.find('.//EC_50').text)
        self.Hill_power.value = float(uep.find('.//Hill_power').text)
        self.enable_active_influx.value = ('true' == (uep.find('.//enable_active_influx').text.lower()) )
        self.relative_max_internal_concentration.value = float(uep.find('.//relative_max_internal_concentration').text)
        self.internalization_rate.value = float(uep.find('.//internalization_rate').text)
        self.reference_external_concentration.value = float(uep.find('.//reference_external_concentration').text)
        self.cycle.value = ('true' == (uep.find('.//cycle').text.lower()) )
        self.apoptosis.value = ('true' == (uep.find('.//apoptosis').text.lower()) )
        self.motility.value = ('true' == (uep.find('.//motility').text.lower()) )
        self.mechanics.value = ('true' == (uep.find('.//mechanics').text.lower()) )
        self.secretion.value = ('true' == (uep.find('.//secretion').text.lower()) )
        self.treat_max_birth_rate.value = float(uep.find('.//treat_max_birth_rate').text)
        self.treat_o2_proliferation_saturation.value = float(uep.find('.//treat_o2_proliferation_saturation').text)
        self.treat_o2_proliferation_threshold.value = float(uep.find('.//treat_o2_proliferation_threshold').text)
        self.treat_o2_reference.value = float(uep.find('.//treat_o2_reference').text)
        self.treat_max_necrosis_rate.value = float(uep.find('.//treat_max_necrosis_rate').text)
        self.treat_o2_necrosis_threshold.value = float(uep.find('.//treat_o2_necrosis_threshold').text)
        self.treat_o2_necrosis_max.value = float(uep.find('.//treat_o2_necrosis_max').text)
        self.treat_apoptosis_rate.value = float(uep.find('.//treat_apoptosis_rate').text)
        self.treat_is_motile.value = ('true' == (uep.find('.//treat_is_motile').text.lower()) )
        self.treat_bias.value = float(uep.find('.//treat_bias').text)
        self.treat_gradient_substrate_index.value = int(uep.find('.//treat_gradient_substrate_index').text)
        self.treat_negative_taxis.value = ('true' == (uep.find('.//treat_negative_taxis').text.lower()) )
        self.treat_speed.value = float(uep.find('.//treat_speed').text)
        self.treat_persistence_time.value = float(uep.find('.//treat_persistence_time').text)
        self.treat_max_relative_adhesion_distance.value = float(uep.find('.//treat_max_relative_adhesion_distance').text)
        self.treat_adhesion_strength.value = float(uep.find('.//treat_adhesion_strength').text)
        self.treat_repulsion_strength.value = float(uep.find('.//treat_repulsion_strength').text)
        self.treat_oxygen_uptake_rate.value = float(uep.find('.//treat_oxygen_uptake_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//oxygen_uptake_rate').text = str(self.oxygen_uptake_rate.value)
        uep.find('.//max_birth_rate').text = str(self.max_birth_rate.value)
        uep.find('.//o2_proliferation_saturation').text = str(self.o2_proliferation_saturation.value)
        uep.find('.//o2_proliferation_threshold').text = str(self.o2_proliferation_threshold.value)
        uep.find('.//o2_reference').text = str(self.o2_reference.value)
        uep.find('.//max_necrosis_rate').text = str(self.max_necrosis_rate.value)
        uep.find('.//o2_necrosis_threshold').text = str(self.o2_necrosis_threshold.value)
        uep.find('.//o2_necrosis_max').text = str(self.o2_necrosis_max.value)
        uep.find('.//apoptosis_rate').text = str(self.apoptosis_rate.value)
        uep.find('.//is_motile').text = str(self.is_motile.value)
        uep.find('.//bias').text = str(self.bias.value)
        uep.find('.//gradient_substrate_index').text = str(self.gradient_substrate_index.value)
        uep.find('.//negative_taxis').text = str(self.negative_taxis.value)
        uep.find('.//speed').text = str(self.speed.value)
        uep.find('.//persistence_time').text = str(self.persistence_time.value)
        uep.find('.//max_relative_adhesion_distance').text = str(self.max_relative_adhesion_distance.value)
        uep.find('.//adhesion_strength').text = str(self.adhesion_strength.value)
        uep.find('.//repulsion_strength').text = str(self.repulsion_strength.value)
        uep.find('.//effect_model').text = str(self.effect_model.value)
        uep.find('.//EC_50').text = str(self.EC_50.value)
        uep.find('.//Hill_power').text = str(self.Hill_power.value)
        uep.find('.//enable_active_influx').text = str(self.enable_active_influx.value)
        uep.find('.//relative_max_internal_concentration').text = str(self.relative_max_internal_concentration.value)
        uep.find('.//internalization_rate').text = str(self.internalization_rate.value)
        uep.find('.//reference_external_concentration').text = str(self.reference_external_concentration.value)
        uep.find('.//cycle').text = str(self.cycle.value)
        uep.find('.//apoptosis').text = str(self.apoptosis.value)
        uep.find('.//motility').text = str(self.motility.value)
        uep.find('.//mechanics').text = str(self.mechanics.value)
        uep.find('.//secretion').text = str(self.secretion.value)
        uep.find('.//treat_max_birth_rate').text = str(self.treat_max_birth_rate.value)
        uep.find('.//treat_o2_proliferation_saturation').text = str(self.treat_o2_proliferation_saturation.value)
        uep.find('.//treat_o2_proliferation_threshold').text = str(self.treat_o2_proliferation_threshold.value)
        uep.find('.//treat_o2_reference').text = str(self.treat_o2_reference.value)
        uep.find('.//treat_max_necrosis_rate').text = str(self.treat_max_necrosis_rate.value)
        uep.find('.//treat_o2_necrosis_threshold').text = str(self.treat_o2_necrosis_threshold.value)
        uep.find('.//treat_o2_necrosis_max').text = str(self.treat_o2_necrosis_max.value)
        uep.find('.//treat_apoptosis_rate').text = str(self.treat_apoptosis_rate.value)
        uep.find('.//treat_is_motile').text = str(self.treat_is_motile.value)
        uep.find('.//treat_bias').text = str(self.treat_bias.value)
        uep.find('.//treat_gradient_substrate_index').text = str(self.treat_gradient_substrate_index.value)
        uep.find('.//treat_negative_taxis').text = str(self.treat_negative_taxis.value)
        uep.find('.//treat_speed').text = str(self.treat_speed.value)
        uep.find('.//treat_persistence_time').text = str(self.treat_persistence_time.value)
        uep.find('.//treat_max_relative_adhesion_distance').text = str(self.treat_max_relative_adhesion_distance.value)
        uep.find('.//treat_adhesion_strength').text = str(self.treat_adhesion_strength.value)
        uep.find('.//treat_repulsion_strength').text = str(self.treat_repulsion_strength.value)
        uep.find('.//treat_oxygen_uptake_rate').text = str(self.treat_oxygen_uptake_rate.value)
