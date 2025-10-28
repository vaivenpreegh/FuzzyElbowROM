import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #4CAF50; /* Change to your desired color */
        color: white; /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)






if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = False



# 1) PAGE CONFIG & HEADER IMAGES ----------------------------------------
st.set_page_config(page_title="Elbow Strength Analyzer", layout="wide")

st.write()

#st.info(
#    "Active Range of Motion & Elbow Strength Analyzer ",width="stretch"
#)

tcol1, tcol2, tcol3, tcol4, tcol5 = st.columns([1, .75,2,.75,1])  # Adjust ratios for desired centering

with tcol3:  # Place content in the middle column
  with st.container(border=True):  # Create a container with a border (the "box")
#         st.markdown(
 #            "<h3 style='text-align: center;color:#33ff33;font-size:24px;'>Active Range of Motion &</h3>",
  #            unsafe_allow_html=True
   #        )
    #     st.markdown(
    #         "<h3 style='text-align: right;color:#33ff33;font-size:24px;'>Elbow Strength Analyzer</h3>",
    #         unsafe_allow_html=True
    #     )#90EE90
   #   st.info(
   #     "               Active Range of Motion (AROM) & Elbow Strength Analyzer ", width="stretch"
   #   )
   st.markdown(
    """
    <div style="background-color:#90EE90; padding:10px; border-radius:5px; color:black">
        <strong> Active Range of Motion (AROM) & Elbow Strength Analyzer</strong>   
    </div>
    """,
    unsafe_allow_html=True
   )


st.write()


if (not st.session_state.show_sidebar) or (st.session_state.show_sidebar == False):

#st.markdown(
         #       "<p style='text-align: center;'>This is some additional text inside the centered box.</p>",
         #       unsafe_allow_html=True
         #   )

  #st.info('Lateral epicondylitis, or tennis elbow, is caused by repetitive strain on elbow tendons, leading to pain, inflammation, and reduced mobility. Severity is often gauged by the range of motion (ROM) in the elbow and wrist.')
  st.markdown(
    """
    <div style="background-color:#90D5FF; padding:10px; border-radius:5px; color:black">
        <strong> Lateral epicondylitis or tennis elbow </strong> is caused by repetitive strain on elbow tendons, leading to pain, inflammation, and reduced mobility.<br> Severity is often gauged by the range of motion (ROM) in the elbow and wrist.   
    </div>
    """,
    unsafe_allow_html=True
   )



  col1, col2, col3 = st.columns([1,1,1])
  #elbowStrengthImg = Image.open('images/ElbowStrength.png').resize((5,5))
  #tennisElbowImg = Image.open('images/TennisElbow.png').resize((5,5))
  #col1.image(elbowStrengthImg, caption="Elbow Anatomy", use_container_width=True)
  #col2.image("images/TennisElbow.png", caption="Sample Movement", use_container_width=True)


  with col1:
      st.image("images/ElbowStrength.png", width=300)
  with col2:
      st.image("images/TennisElbowPain.jpg", width=300,caption="Tennis Elbow Anatomy")
  with col3:
      st.image("images/TennisElbow.png", width=300)

  #col1.image("images/ElbowStrength.png", caption="Elbow Anatomy", use_container_width=True)
  #col2.image("images/TennisElbow.png", caption="Sample Movement", use_container_width=True)

  # 2) INSTRUCTION BOX -----------------------------------------------------

  icol1, icol2, icol3 = st.columns([1, 2, 1])  # Adjust ratios for desired centering

  with icol2:  # Place content in the middle column

   st.info(
     "Enter ROM values in sidebar and click " 
     "**Assess Elbow Strength** to analyze elbow health")

   enterdata = st.button("Enter ROM details..")

   st.info(
       'The system analyzes elbow movements Flexion, Extension, Pronation, Supination, and Wrist Extension, integrating pain level to determine Elbow Strength')

   if enterdata:
    st.session_state.show_sidebar = True


# 3) DEFINE FUZZY   VARIABLES & MEMBERSHIP FUNCTIONS ----------------------
flexion    = ctrl.Antecedent(np.arange(69, 180, 1),   'Elbow Flexion')
extension  = ctrl.Antecedent(np.arange(-5,   8,   1), 'Elbow Extension')
wextension = ctrl.Antecedent(np.arange(20,  75,  1),  'Wrist Extension')
pronation  = ctrl.Antecedent(np.arange(30, 100,  1),  'Elbow Pronation')
supination = ctrl.Antecedent(np.arange(0,  100,  1),  'Elbow Supination')
elbowHealth= ctrl.Consequent(np.arange(0,   15,  1),  'AROM Assessment')

flexion['Hypomobility']   = fuzz.trimf(flexion.universe,    [69, 100, 143])
flexion['Normal']         = fuzz.trapmf(flexion.universe,   [130,143,149,160])
flexion['Hypermobility']  = fuzz.trimf(flexion.universe,    [149,170,180])

extension['Hypomobility']  = fuzz.trimf(extension.universe, [-5,  -2,  0])
extension['Normal']        = fuzz.trapmf(extension.universe,[-2,   0,  1, 3])
extension['Hypermobility'] = fuzz.trimf(extension.universe, [2,    5,  8])

wextension['Hypomobility']  = fuzz.trimf(wextension.universe, [20,  35, 50])
wextension['Normal']        = fuzz.trapmf(wextension.universe, [40,  50, 60, 70])
wextension['Hypermobility'] = fuzz.trimf(wextension.universe, [60,  73, 75])

pronation['Hypomobility']   = fuzz.trimf(pronation.universe,  [30, 30, 78])
pronation['Normal']         = fuzz.trapmf(pronation.universe, [68, 78, 84, 94])
pronation['Hypermobility']  = fuzz.trimf(pronation.universe,  [84, 90,100])

supination['Hypomobility']  = fuzz.trimf(supination.universe, [0,   0, 85])
supination['Normal']        = fuzz.trapmf(supination.universe, [80, 85, 89, 94])
supination['Hypermobility'] = fuzz.trimf(supination.universe, [89, 95,100])

elbowHealth['Very Limited'] = fuzz.trimf(elbowHealth.universe, [0,   2,   4])
elbowHealth['Limited']      = fuzz.trimf(elbowHealth.universe, [4,   6,   8])
elbowHealth['Normal']       = fuzz.trimf(elbowHealth.universe, [8,  10,  12])

rules = [
    ctrl.Rule(flexion['Hypomobility'],                                   elbowHealth['Very Limited']),
    ctrl.Rule(wextension['Hypomobility'],                                elbowHealth['Very Limited']),
    ctrl.Rule(flexion['Normal'] & (extension['Hypomobility'] | extension['Hypermobility']),
                                                                          elbowHealth['Very Limited']),
    ctrl.Rule((flexion['Hypomobility'] | flexion['Hypermobility']) &
              (extension['Hypomobility'] | extension['Hypermobility']),
                                                                          elbowHealth['Very Limited']),
    ctrl.Rule(flexion['Normal'] & wextension['Normal'] &
              (pronation['Hypomobility'] | pronation['Hypermobility']),
                                                                          elbowHealth['Limited']),
    ctrl.Rule(flexion['Normal'] & wextension['Normal'] &
              (supination['Hypomobility'] | supination['Hypermobility']),
                                                                          elbowHealth['Limited']),
    ctrl.Rule(flexion['Normal'] & extension['Normal'] & wextension['Normal'] &
              pronation['Normal'] &
              (supination['Normal'] | supination['Hypomobility']),
                                                                          elbowHealth['Normal']),
]

system     = ctrl.ControlSystem(rules)
simulation = ctrl.ControlSystemSimulation(system)



# 4) SIDEBAR CONTROLS -----------------------------------------------------

if st.session_state.show_sidebar:
    with st.sidebar:
     st.sidebar.header("Analyzer Controls")
     flexion_val    = st.sidebar.slider("Elbow Flexion (°)",    69, 180, 140)
     extension_val  = st.sidebar.slider("Elbow Extension (°)",  -5,   8,   0)
     pronation_val  = st.sidebar.slider("Elbow Pronation (°)",  30, 100,  78)
     supination_val = st.sidebar.slider("Elbow Supination (°)",   0, 100,  85)
     wextension_val = st.sidebar.slider("Wrist Extension (°)",  20,  75,  50)
     pain_level     = st.sidebar.selectbox(
       "Select pain level:",
         ["None", "Low", "Moderate", "Severe"]
     )
     assess = st.sidebar.button("Assess Elbow Strength")

# 5) RUN ASSESSMENT & DISPLAY RESULTS ------------------------------------
    if assess:
     # Fuzzy inputs and compute
     simulation.input['Elbow Flexion']    = flexion_val
     simulation.input['Elbow Extension']  = extension_val
     simulation.input['Elbow Pronation']  = pronation_val
     simulation.input['Elbow Supination'] = supination_val
     simulation.input['Wrist Extension']  = wextension_val
     simulation.compute()
     output_value = round(simulation.output['AROM Assessment'], 2)

    # Classify elbow strength
     if output_value is not None:
      if pain_level == 'Severe' or output_value <= 4:
        elbow_strength = 'Weak - Limited ROM and/or high pain levels'
      elif output_value <= 8:
        elbow_strength = 'Average - Moderate ROM or mild pain interference' if pain_level in ('None','Low','Moderate') else 'Weak'
      else:
        elbow_strength = 'Good - High ROM and low pain levels' if pain_level in ('None','Low','Moderate') else 'Average'
     else:
        output_value = 0
        elbow_strength = ''

     fcol1, fcol2, fcol3 = st.columns([1, 2, 1])  # Adjust ratios for desired centering

     with fcol2:  # Place content in the middle column

      st.info('Predicted Elbow Strength Based on Fuzzy Logic Analysis')
      # Main assessment plot
      fig_main, ax_main = plt.subplots(figsize=(4, 2))

      plt.rcParams["axes.titlesize"] = 10  # Font size for all axes titles
      plt.rcParams["axes.labelsize"] = 4  # Font size for all axes labels
      plt.rcParams["xtick.labelsize"] = 4  # Font size for x-tick labels
      plt.rcParams["ytick.labelsize"] = 6  # Font size for y-tick labels
      plt.rcParams["legend.fontsize"] = 6  # Font size for legends

      ax_main.plot(elbowHealth.universe, elbowHealth['Very Limited'].mf, label='Very Limited')
      ax_main.plot(elbowHealth.universe, elbowHealth['Limited'].mf,      label='Limited')
      ax_main.plot(elbowHealth.universe, elbowHealth['Normal'].mf,       label='Normal')
      ax_main.axvline(output_value, color='red', linestyle='--',
                    label=f'Output: {output_value}')

      #ax_main.tick_params(axis='x', labelsize=15)
      #ax_main.tick_params(axis='y', labelsize=15)

     # ax_main.set_title('Fuzzy AROM Assessment')
      ax_main.set_xlabel('Aggregated ROM Score (all movements)')
      ax_main.set_ylabel('Membership Degree in Strength')
      ax_main.legend()
      st.pyplot(fig_main)

    # Display computed results
     rcol1, rcol2 = st.columns(2)
     with rcol1:
       st.info("AROM Score:   " + str(output_value))
     with rcol2:
       if elbow_strength == 'Good':
           st.info("Elbow Strength:  " + str(elbow_strength),icon=":material/thumb_up:")
       elif elbow_strength == 'Weak':
           st.info("Elbow Strength:  " + str(elbow_strength), icon=":material/sick:")
       else:
           st.info("Elbow Strength:  " + str(elbow_strength))
    # Tabs for detailed plots
     tab1, tab2, tab3 = st.tabs([
        "Flexion & Extension",
        "Pronation / Supination / Wrist Ext.",
        "Glossary: Conditions & Movements "
     ])

     with tab3:
       st.info('Hypomobility is a condition where one or more joints have a reduced range of motion. Limits flexibility and can make movements like bending, reaching, or rotating difficult. ')
       st.info('Hypermobility is a condition where joints can bend or stretch more than typical. This often causes joint pain, instability which leads to frequent sprains and dislocations.')
       st.write()
       st.info('Elbow flexion: Movement that bends forearm toward upper arm. Every day tasks like eating, lifting, or brushing hair.')
       st.info('Elbow extension: Movement that straightens the arm by increasing the angle between the forearm and upper arm. It is opposite of flexion and is essential for reaching, pushing, and stabilizing the arm.')
       st.info('Elbow pronation: Rotational movement of the forearm when turning the palm downward. Daily tasks like typing, turning doorknobs, and using tools.')
       st.info('Elbow supination: Rotational movement of the forearm when turning the palm upward. Simple tasks like holding a bowl or receiving change. Key motion for functional hand use.')
     with tab1:

        fig_fe, (ax_f, ax_e) = plt.subplots(1, 2, figsize=(12, 4))
        # Flexion
        for label in ['Hypomobility','Normal','Hypermobility']:
            ax_f.plot(
                flexion.universe,
                flexion[label].mf,
                label=label
            )
        ax_f.axvline(flexion_val, color='red', linestyle='--',
                     label=f'Input: {flexion_val}')
        ax_f.set_title('Elbow Flexion')
        ax_f.set_xlabel('°')
        ax_f.legend(fontsize=8)
        # Extension
        for label in ['Hypomobility','Normal','Hypermobility']:
            ax_e.plot(
                extension.universe,
                extension[label].mf,
                label=label
            )
        ax_e.axvline(extension_val, color='red', linestyle='--',
                     label=f'Input: {extension_val}')
        ax_e.set_title('Elbow Extension')
        ax_e.set_xlabel('°')
        ax_e.legend(fontsize=8)
        st.pyplot(fig_fe)

     with tab2:
        fig_psw, axes = plt.subplots(1, 3, figsize=(18, 4))
        for ax, var, val, title in zip(
            axes,
            [pronation, supination, wextension],
            [pronation_val, supination_val, wextension_val],
            ['Pronation','Supination','Wrist Extension']
        ):
            for label in ['Hypomobility','Normal','Hypermobility']:
                ax.plot(var.universe, var[label].mf, label=label)
            ax.axvline(val, color='red', linestyle='--', label=f'Input: {val}')
            ax.set_title(title)
            ax.set_xlabel('°')
            ax.legend(fontsize=7)
            ax.yaxis.set_major_locator(MultipleLocator(0.2))
        st.pyplot(fig_psw)


