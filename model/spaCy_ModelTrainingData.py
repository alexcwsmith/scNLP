#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:02:03 2020

@author: smith
"""
LABEL = "REGION"
PER = "PERSON"
DATE = "DATE"
NT = "NEUROTRANSMITTER"
PHYS = "PHYSIO"
FUNC = "FUNCTION"



TRAIN_DATA = [
    ("The LH sends a glutamatergic projection to the VTA.",
        {"entities": [(4, 6, LABEL), (15, 28, NT), (47, 50, LABEL)]}),
    
    ("Where does it start?",
     {"entities": []}),
    
    ("The NAcc is the ventral region of the striatum",
        {"entities": [(4, 8, LABEL), (38, 45, LABEL)]}),
    
    ("The PFC may exert its conflict resolution function through connections with other structures",
     {"entities": [(4, 7, LABEL), (22, 41, FUNC)]}),
    
    ("there have been many investigations into the PFC",
     {"entities": [(45, 48, LABEL)]}),
    
    ("This suggests that OFC weighs information from these opposing stimuli and regulates behavior?",
     {"entities": [(19, 22, LABEL), (74, 92, FUNC)]}),
    
    ("After learning, the reward memory is stored in the PFC and NAcc",
     {"entities": [(51, 54, LABEL), (59, 63, LABEL), (20, 43, FUNC)]}),
    
    ("Peters et al",
     {"entities": [(0, 6, PER)]}),

    ("Enhancing activity in PL increases fear and drug-seeking",
     {"entities": [(22, 24, LABEL), (25, 39, FUNC), (44, 56, FUNC)]},
     ),
       
    ("The neural circuit that underlies this approach behavior has been widely studied and involves the VTA and NAcc",
     {"entities": [(98, 101, LABEL), (106, 110, LABEL), (39, 56, FUNC)]},
     ),
  
    ("while activity in IL decreases fears and drug-seeking",
     {"entities": [(18, 20, LABEL), (21, 36, FUNC), (41, 53, FUNC)]}),

    ("In a series of experiments in the 1950s, Olds and Milner (1954) found that rats will press a lever to self-stimulate the VTA to NAcc pathway at an even faster rate than to obtain food.",
     {"entities": [(121, 124, LABEL), (128, 132, LABEL), (41, 45, PER), (50, 56, PER), (58, 62, "DATE")]}),
 
    ("there is also evidence that OFC signals aversive stimuli",
     {"entities": [(28, 32, LABEL), (32, 56, FUNC)]}),
    
    ("Taken together, these findings suggest both IL/PL and OFC coordinate the interaction between threat- and reward-related stimuli",
     {"entities": [(44, 46, LABEL), (47, 49, LABEL), (54, 57, LABEL), (73, 127, FUNC)]}),
    
    ("function of PFC is involved, but via divergent projections to the NAcc rather than to the amygdala",
     {"entities": [(12, 15, LABEL), (66, 70, LABEL), (90, 96, LABEL)]}),
    
    ("The ARC has important implications in the control of glucose homeostasis, including the regulation of food intake and energy balance",
     {"entities": [(4, 7, LABEL), (42, 72, FUNC), (88, 132, FUNC)]}),
    
    ("Activation of AgRP and NPY neurons have been reported to promote anabolic processes that lead to a markedly increase of food intake",
     {"entities": [(14, 18, NT), (23, 26, NT), (57, 83, FUNC), (108, 131, FUNC)]}),
        
    ("On the contrary, activation of POMC neurons favours catabolic processes, reducing appetite and food intake, whereas their inhibition increases feeding (Shin et al. 2017)",
     {"entities": [(31, 35, NT), (152, 156, PER), (52, 71, FUNC), (73, 106, FUNC), (133, 150, FUNC), (164, 168, "DATE")]}),
    
    ("Recently, a new population of neurons in the ARC have been discovered",
     {"entities": [(45, 48, LABEL)]}),

    ("Finally, the ARC also possesses glucosensing neurons (Wang et al. 2004; Spanswick et al. 1997",
     {"entities": [(13, 16, LABEL), (54, 58, PER), (66, 70, "DATE"), (72, 81, PER), (89, 93, "DATE"), (32, 44, PHYS)]}),
    
    ("Stimulation of projections to the lateral hypothalamus (AgRP→LHN projections) promotes feeding (Steculorum et al. 2016)",
     {"entities": [(34, 54, LABEL), (56, 60, LABEL), (61, 65, LABEL), (96, 106, PER), (114, 118, "DATE"), (78, 94, FUNC)]}),

    ("while activation of the projections to the anterior bed nucleus of the stria terminalis (AgRP→aBNST6vl projections) mediate the activation of BAT-Mstn expression",
     {"entities": [(43, 87, LABEL), (89, 93, LABEL), (94, 102, LABEL), (116, 138, FUNC), (142, 151, PHYS)]}),
    
    ("In fact, a recent study has reported that an increase of NPY from the ARC decreases the sympathetic outflow that controls",
     {"entities": [(57, 60, NT), (70, 73, LABEL), (74, 107, FUNC)]}),
    
    ("The VMH is a key brain region involved in glucose regulation and energy homeostasis in mammals (Chowdhury et al. 2017).",
     {"entities": [(4, 7, LABEL), (96, 105, PER), (113, 117, "DATE"), (42, 60, FUNC), (65, 83, FUNC)]}),
    
    ("In particular, the VMH has a crucial role in detecting hypoglycemic events and initiating the physiological counterregulatory signaling",
     {"entities": [(19, 22, LABEL), (45, 74, FUNC), (79, 135, FUNC)]}),
   #### 
    ("A subset of VMH neurons expresses the leptin receptor (Elmquist et al. 1998).",
     {"entities": [(12, 15, LABEL), (38, 44, NT), (45, 53, PHYS), (55, 63, PER), (71, 75, "DATE")]}),
    
    ("SF1 neurons in the VMH are required for maintenance of normal glucose and energy metabolism.",
     {"entities": [(0, 3, NT), (19, 22, LABEL), (40, 69, FUNC), (74, 91, FUNC)]}),
    
    ("Leptin is a hormone predominantly made in adipose cells that helps to regulate energy balance by i) inhibiting hunger, ii) stimulating glucose uptake.",
     {"entities": [(0, 6, NT), (79, 93, FUNC), (100, 117, FUNC), (123, 149, FUNC)]}),

    ("Two major neurotransmitters are involved in the neural circuitry of the VMH, the inhibitory neurotransmitter GABA and the excitatory one glutamate.",
     {"entities": [(72, 75, LABEL), (109, 113, NT), (137, 146, NT)]}),
    
    ("To begin with, VMH GABAergic neurotransmission has been extensively studied with respect to its role in glucose sensing.",
     {"entities": [(15, 18, LABEL), (19, 28, NT), (104, 119, FUNC)]}),
    
    ("It is known that glucose deprivation alters GABA levels within the brain.",
     {"entities": [(17, 24, PHYS), (44, 48, NT)]}),
###TESTED TO HERE   
    ("In more detail, diabetes induced an increment in local GABA concentrations in the VMH.",
     {"entities": [(55, 59, NT), (82, 85, LABEL)]}),
    
    ("This counterregulatory impairment is reversed by specifically reducing excessive GABAergic inhibitory tone in the VMH (Chan et al. 2011).",
     {"entities": [(81, 90, NT), (114, 117, LABEL), (119, 123, PER), (131, 135, "DATE")]}),
    
    ("For instance, electrical stimulation of the VMH increased the sympathetic tone.",
     {"entities": [(44, 47, LABEL), (48, 78, FUNC)]}),
    
    ("Regarding its action in the liver, electrical stimulation of the VMH was found many years ago.",
     {"entities": [(65, 68, LABEL)]}),
    
    ("An increase in glucose utilization in the interscapular BAT, heart, and skeletal muscle.",
     {"entities": [(15, 34, FUNC)]}),
    
    ("The fact that VMH stimulation does not increase insulin secretion from the pancreas",
     {"entities": [(14, 17, LABEL), (35, 65, FUNC), (75, 83, LABEL)]}),
    
    ("The LHN contains the primary orexinergic nucleus within the hypothalamus and widely projects to the entirety of the remainder of the hypothalamus.",
     {"entities": [(4, 7, LABEL), (29, 40, NT), (133, 145, LABEL)]}),
    
    ("In particular to the posterior hypothalamus, the arcuate nucleus and the paraventricular hypothalamic nucleus.",
     {"entities": [(21, 43, LABEL), (49, 64, LABEL), (73, 109, LABEL)]}),

    ("Many studies of stimulation of the LHN have showed an action of this area over hepatic glucose metabolism.",
     {"entities": [(35, 38, LABEL), (79, 105, FUNC)]}),

    ("On the contrary, most recent studies have proved its implications on glycogen metabolism in the liver, where VMH and LHN carry out reciprocal effects (Yi et al. 2010).",
     {"entities": [(109, 112, LABEL), (117, 120, LABEL), (151, 153, PER), (161, 165, "DATE"), (69, 88, FUNC)]}),
    
    ("The SCN is a small region of the hypothalamus, situated directly above the optic chiasm.",
     {"entities": [(4, 7, LABEL), (33, 45, LABEL), (75, 87, LABEL)]}),
    
    ("As previously mentioned, it is well known for regulating many different body functions in a 24-h cycle (circadian rhythms).",
     {"entities": [(46, 102, FUNC), (104, 121, FUNC)]}),
    
    ("In addition, studies of electrical stimulation of the SCN have also induced hyperglycemia, which was prevented by the use of sympathetic blockers or denervation (Yi et al. 2010).",
     {"entities": [(54, 57, LABEL), (162, 164, PER), (172, 176, "DATE"), (68, 89, FUNC), (125, 145, PHYS)]}),
    
    ("This suggests a sympathetic mediation of the effects due to SCN activation.",
     {"entities": [(60, 63, LABEL), (16, 37, FUNC)]}),
    
    ("The integration of information related to the body’s energy homeostasis does not occur solely in the hypothalamus. For example, meal-related satiety information is conveyed to the nucleus of the tractus solitarius (NTS) in the medulla.",
     {"entities": [(101, 113, LABEL), (180, 213, LABEL), (227, 234, LABEL), (53, 71, FUNC)]}),
###TESTED TO HERE    
    ("Some NTS neurones are glucose sensitive, while others express POMC, leptin receptors or the MC4R.",
     {"entities": [(5, 8, LABEL), (22, 29, PHYS), (62, 66, NT), (68, 84, PHYS), (92, 96, PHYS)]}),
    
    ("The NTS also sends a dense projection to the LHN, reinforcening its contribution in the control of body energy (Williams et al. 2001)",
     {"entities": [(4, 7, LABEL), (45, 48, LABEL), (112, 120, PER), (128, 132, "DATE"), (88, 110, FUNC), ]}),
    
    ("Notably, we demonstrated that RAB39B is an abundant protein in dopaminergic neurons in the SNpc, the neuronal subtype selectively lost in PD.",
     {"entities": [(30, 36, PHYS), (63, 75, NT), (91, 95, LABEL)]}),
    
    ("MC4R is localized in the thalamus, hypothalamus, and hippocampus among other brain and peripheral sites [20, 21].",
     {"entities": [(0, 4, PHYS), (25, 33, LABEL), (35, 47, LABEL), (53, 64, LABEL)]}),
    
    ("SIM1 homozygous knockout mice fail to properly form at least the paraventricular (PVH), supraoptic (SON), and anterior periventricular (aPV) hypothalamic nuclei and die perinatally [24].",
     {"entities": [(0, 4, PHYS), (65, 80, LABEL), (82, 85, LABEL), (88, 98, LABEL), (100, 103, LABEL), (110, 134, LABEL), (136, 139, LABEL)]}),
   
    ("We next explored the contribution of BRS3 in SIM1-expressing neurons, which are predominantly in the paraventricular nucleus of the hypothalamus (PVH).",
     {"entities": [(37, 41, PHYS), (45, 49, PHYS), (101, 144, LABEL)]}),
    
    ("BRS3 deletion in SIM1-expressing neurons impaired insulin tolerance and increased insulin levels.",
     {"entities": [(0, 4, PHYS), (17, 21, PHYS), (41, 67, PHYS), (72, 96, FUNC)]}),
    
    ("Glutamate excitotoxicity may develop during numerous events; as a secondary injury after traumatic injury (Park et al., 2008).",
     {"entities": [(0, 9, NT)]}),
    
    ("The release of glutamate is followed by the activation of its postsynaptic receptors.",
     {"entities": [(15, 24, NT), (44, 84, FUNC)]}),
    
    ("The experimental rats received one single injection of TGF-β1 (R&D Systems, United States) on day seven after 3-AP infusion. TGF-β1 was unilaterally injected into the lateral ventricle of rats mounted on a stereotaxic frame.",
     {"entities": [(167, 185, LABEL), (55, 61, PHYS), (125, 131, PHYS)]}),
    
    ("Membranous organelles make intimate contacts with each other and serve as platforms for multiple molecular processes executed by signalling proteins.",
     {"entities": [(27, 60, FUNC), (88, 148, FUNC)]}),
    
    ("GLP-1 mediates its effects by binding to its receptor, the GLP-1 receptor (GLP-1R), which is a G protein–coupled receptor that is abundantly present in the pancreatic beta cells.",
     {"entities": [(0, 5, NT), (59, 73, PHYS), (75, 81, PHYS), (156, 177, LABEL)]}),
    
    ("Projections of the medial cerebellar nucleus to the ventrolateral periaqueductal gray.",
     {"entities": [(19, 44, LABEL), (52, 85, LABEL)]}),
    
    ("First, we injected the mCbN with viruses expressing a channelrhodopsin-eYFP (ChR2-eYFP) fusion protein.",
     {"entities": [(23, 27, LABEL)]}),
    
    ("Middle, Confocal image of the mCbN after injection of AAV-hSyn-ChR2-eYFP virus",
     {"entities": [(30, 34, LABEL)]}),
    
    ("Previous tracing studies have demonstrated that the mCbN indeed projects to the vlPAG (Gonzalo-Ruiz et al., 1990).",
     {"entities": [(52, 56, LABEL), (80, 85, LABEL), (87, 99, PER), (108, 112, "DATE")]}),
    
    ("Right, Confocal image of virally labeled mCbN axons in the vlPAG.",
     {"entities": [(41, 45, LABEL), (59, 64, LABEL)]}),
    
    ("Example injection site of CTb-GFP in the vlPAG.",
     {"entities": [(41, 46, LABEL)]}),
    
    ("Low magnification image of mCbN labeled axons in vlPAG.",
     {"entities": [(27, 31, LABEL), (49, 54, LABEL)]}),
    
    ("Even the vlPAG, however, is heterogeneous, as pharmacological activation of the vlPAG elicits freezing, bradycardia, and anti-nociception (Bandler et al., 2000).",
     {"entities": [(9, 14, LABEL), (80, 85, LABEL), (139, 146, PER), (155, 159, "DATE"), (94, 137, FUNC)]}),
    
    ("Daily food intake (FI) is a function of meal size (MZ) and meal number.",
     {"entities": [(0, 17, FUNC), (19, 21, FUNC)]}),
    
    ("Feeding patterns via changes in the concentration of hypothalamic dopamine [32], among other neuromediators.",
     {"entities": [(0, 16, FUNC), (53, 65, LABEL), (66, 74, NT)]}),
    
    ("The beta toxin gene (cpb) is encoded on a large plasmid and codes for a small polypeptide protoxin.",
     {"entities": [(60, 98, FUNC)]}),

    ("Also, an intracerebral injection of the neurotoxin 6-hydroxydopamine (OHDA) into the medial forebrain bundle (MFB) has been shown to result in a parkinsonian rat model [28, 29].",
     {"entities": [(51, 58, PHYS), (70, 74, PHYS), (85, 108, LABEL), (110, 113, LABEL)]}),
    
    ("The level of DA was measured in the left hemisphere striatum, prefrontal cortex, and dorsal hippocampus using a dopamine ELISA kit according to the manufacturer's instructions.",
     {"entities": [(13, 15, NT), (52, 60, LABEL), (62, 79, LABEL), (85, 103, LABEL)]}),
    
    ("Serotonin levels were measured in the left hemisphere striatum, prefrontal cortex, and hippocampus of all rats on PND 76.",
     {"entities": [(0, 9, NT), (54, 62, LABEL), (64, 81, LABEL), (87, 98, LABEL)]}),
    
    ("Besides, given the hippocampus-dependent learning and memory, the long-lasting and elevated plasma corticosterone levels impaired learning and memory resulting in poor cognitive performance of maternally separated rats in the MWM test.",
     {"entities": [(19, 30, LABEL), (41, 60, FUNC), (99, 113, PHYS), (130, 149, FUNC)]}),
    
    ("The DRN contains a large number of 5-HT neurons that project to the forebrain and midbrain, including reward-related brain areas, such as the VTA, nucleus accumbens (NAc), and lateral hypothalamus (LH).",
     {"entities": [(4, 7, LABEL), (35, 39, NT), (68, 77, LABEL), (82, 91, LABEL), (102, 116, FUNC), (142, 145, LABEL), (147, 164, LABEL), (166, 169, LABEL), (176, 196, LABEL), (198, 200, LABEL)]}),
    
    ("Similar to an antidepressive effect, rewarding potency of DRN 5-HT neurons has been studied by using several lines of genetically-modified mice.",
     {"entities": [(14, 35, FUNC), (58, 61, LABEL), (62, 66, NT)]}),
    
    ("We examined the rewarding potency of optogenetic manipulation of DRN 5-HT neurons using an adeno-associated virus (AAV) expressing optogenetic actuators",
     {"entities": [(65, 68, LABEL), (69, 74, NT)]}),
    
    ("We found that the optogenetic activation of DRN 5-HT neurons and 5-HT projections from the DRN to VTA strongly reinforced nose-poke self-stimulation behavior and induced conditioned place preference.",
     {"entities": [(44, 47, LABEL), (48, 52, NT), (65, 69, NT), (91, 94, LABEL), (98, 101, LABEL), (111, 157, FUNC), (170, 198, FUNC)]}),
    
    ("Optogenetic Activation of 5-HT Neuron Terminals in the VTA is Responsible for Reinforcement of Nose-Poke Behavior but not in the LH, CeA, NAc, or Ventral Pallidum (VP).",
     {"entities": [(26, 30, NT), (55, 58, LABEL), (78, 113, FUNC), (129, 131, LABEL), (133, 136, LABEL), (138, 141, LABEL), (146, 162, LABEL), (164, 166, LABEL)]}),
    
    ("In this study, we examined the involvement of the VTA, LH, NAc, CeA, and VP.",
     {"entities": [(50, 53, LABEL), (55, 57, LABEL), (59, 62, LABEL), (64, 67, LABEL), (73, 75, LABEL)]}),
    
    ("In summary, our data provide direct evidence that selective stimulation of DRN 5-HT neurons projecting to the VTA was sufficient for reinforcing effect and conditioned place preference.",
     {"entities": [(75, 78, LABEL), (79, 83, NT), (110, 113, LABEL), (133, 151, FUNC), (156, 184, FUNC)]}),

    ("Adiponectin (ADPN) is a plasma protein that belongs to the complement 1q family and it is secreted by adipose tissue [1,2].",
     {"entities": []}),
   
    ("However, ADPN was found to modulate glucose metabolism in hippocampal neurons, increasing glucose uptake, glycolysis, and ATP production rates [27].",
     {"entities": [(27, 54, FUNC), (58, 69, LABEL)]}),
   
    ("In both humans and laboratory animals, kappa opioid receptor (KOR) activation produces depressive and anxiety-like effects.",
     {"entities": [(39, 51, NT), (87, 122, FUNC)]}),
   
    ("The brain stem contains the midbrain, pons, and medulla in the caudal fossa.",
     {"entities": [(4, 14, LABEL), (28, 36, LABEL), (38, 42, LABEL), (48, 55, LABEL), (63, 75, LABEL)]}),
   
    ("Therefore, we planned to inject retrograde tracer cholera toxin B subunit (CB) into the CSF-contacting nucleus.",
     {"entities": [(88, 110, LABEL)]}),
    
    ("The generic category of diffuse gliomas (DG) includes two distinct tumor entities: tumors derived from oligodendrocyte precursor cells – OPCs (OligoPDTs) versus those derived from stem cells (SCDTs).",
     {"entities": []}),
    
    ("In particular, NPY neurons in the Arc play a critical role in the control of energy homeostasis.",
     {"entities": [(15, 18, NT), (34, 37, LABEL), (66, 95, FUNC)]}),
    
    ("In addition, NAc dysfunction is associated with many mental disorders,",
     {"entities": [(13, 16, LABEL), (48, 69, FUNC)]}),
    
    ("The median number of whole-brain labeled neurons to the NAc subnuclei was 9,518.",
     {"entities": [(56, 59, LABEL)]}),
    
    ("The 75 brain regions could be grouped into nine major brain areas, including the isocortex, olfactory areas (OLF), hippocampal formation (HPF), cortical subplate (CTXsp), striatum (STR), pallidum (PAL), and thalamus (TH).",
     {"entities": [(81, 90, LABEL), (92, 107, LABEL), (109, 112, LABEL),  (115, 136, LABEL), (138, 141, LABEL), (144, 161, LABEL), (163, 168, LABEL), (171, 179, LABEL), (181, 184, LABEL), (187, 195, LABEL), (203, 211, LABEL), (213, 215, LABEL)]}),
    
    ("Summary of Distribution of Input Neurons to Subregions of NAcC and NAcS",
     {"entities": [(58, 62, LABEL), (67, 71, LABEL)]}),

    ("The critical cardiovascular features include hypotension and paradoxical sinus bradycardia, heart block, or sinus arrest after sympathetic excitation.",
     {"entities": []}),
    
    ("The neuropeptide oxytocin is mainly produced in the hypothalamic paraventricular (PVN) and supraoptic nuclei (SON), and it is released from magnocellular cells by axonal and somatodendritic release.",
     {"entities": [(17, 25, NT), (52, 64, LABEL), (65, 80, LABEL), (82, 85, LABEL), (91, 108, LABEL), (110, 113, LABEL)]}),
    
    ("The VTA projects primarily to NAcc/PFC and receives input from the lateral hypothalamus that detects the presence of food reward (Schultz, 1998).",
     {"entities": [(4, 7, LABEL), (30, 34, LABEL), (35, 38, LABEL), (67, 87, LABEL), (130, 137, PER), (139, 143, "DATE"), (93, 128, FUNC)]}),
    
    ("Notwithstanding, the approach system must interact and even suppress the aversive system to attain reward.",
     {"entities": []}),
    
    ("In brief, in instrumental conditioning, the response associated with the availability of a reward excites the pathway from the VTA to NAcc, which in turn triggers an approach response by acting on the motor system.",
     {"entities": [(127, 130, LABEL), (134, 138, LABEL), (166, 183, FUNC)]}),
    
    ("BJ and MM contributed equally to the manuscript.",
     {"entities": []}),
    
    ("Individuals affected by prenatal alcohol exposure (PAE) can present with a complex profile of cognitive, behavioral, physical, and mental health problems.",
     {"entities": []}),
    
    ("All SES measures were based on the participants\u2019 current caregiver participating in the study.",
     {"entities": []}),
    
    ("A secondary aim was to examine the potential cognitive relevance of observed differences in SES-brain associations between the Control and PAE groups.",
     {"entities": []}),
    
    ("All analyses were conducted with the statistical program R (v3.0.2) (R Core Team, 2013).",
     {"entities": []}),
###100    
    ("Prescription opioid medication dispensings were also extracted for the matched samples.",
     {"entities": []}),
    
    ("Homelessness, housing and health are intrinsically linked [10]. ",
     {"entities": []}),
    
    ("Descriptive statistics are reported as percentages for dichotomous variables and means with standard deviations for all other variables.",
     {"entities": []}),
    
    ("Imaging revealed enhanced soft tissue thickening around the right paraspinal site at T11–12 (Fig. 2A).",
     {"entities": []}),
    
    ("In 2016, 40% of the opioid-related overdose deaths were associated with the use of prescription opioids.",
     {"entities": [(3, 7, "DATE")]}),
    
    ("For quantification, pERK levels were normalized against corresponding tubulin levels determined in the same experiment, which served as a loading control.",
     {"entities": [(20, 24, PHYS), (70, 77, PHYS)]}),
    
    ("Dopamine (DA) released by dopaminergic VTA and SNc inputs to striatum signals the difference between received and expected rewards the reward prediction error (RPE)",
     {"entities": [(0, 8, NT), (10, 12, NT), (26, 38, NT), (39, 42, LABEL), (47, 50, LABEL), (61, 69, LABEL), (82, 131, FUNC), (135, 158, FUNC), (160, 163, FUNC)]}),
    
    ("The BG is suggested to remain involved in action selection after the action-reward association is learned [5,25].",
     {"entities": [(4, 6, LABEL), (42, 58, FUNC)]}),
###TESTED TO HERE    
    ("On the other hand, clinical interventions for Parkinson disease (PD) do not cause impairments in learned movements [26–28].",
     {"entities": []}),
    
    ("Specifically, GPi lesions and deep brain stimulation (DBS) in the STN, which both thought to disrupt the main output of the BG, are used to improve motor functions.",
     {"entities": [(14, 17, LABEL), (66, 69, LABEL), (148, 163, FUNC)]}),
#110    
    ("Other models are constructed based on functional ideas and emulate how biophysical changes caused by a disorder violate the functions [35–39].",
     {"entities": []}),
    
    ("We adopt rate model formalism extensively used to reproduce activity and function of numerous brain structures [46].",
     {"entities": []}),
    
    ("The BG receives inputs from the prefrontal cortex (PFC) signaling the conditioning stimulus (CS) as well as reward inputs via substantia nigra pars compacta",
     {"entities": [(4, 6, LABEL), (32, 49, LABEL), (51, 54, LABEL), (126, 156, LABEL), (56, 91, FUNC), (108, 121, FUNC)]}),
    
    ("The rest of the nuclei are the globus pallidus external (GPe), subthalamic nucleus (STN), and the output structures: substantia nigra pars reticulata and globus pallidus internal (SNr/GPi).",
     {"entities": [(31, 55, LABEL), (57, 60, LABEL), (63, 82, LABEL), (84, 87, LABEL), (117, 149, LABEL), (154, 178, LABEL), (180, 183, LABEL), (184, 187, LABEL)]}),
    
    ("The activity of every neuron is governed by the following differential equation [42]:",
     {"entities": []}),
    
    ("The pathology of Huntington’s Disease (HD) is less well-understood; however, it is clear that there is a progression of the disease from chorea (involuntary, jerky movement) at its onset to akinesia (loss of the power of voluntary movement) at its conclusion [76].",
     {"entities": []}),
    
    ("For example, rates of cancer incidence and mortality [16], heart disease [17], obesity [18], diabetes [19], smoking [20], and drug use [21] are all higher in Appalachia compared to other US regions, and those living in Appalachia are at greater risk of low health literacy [22] and perceive their overall health status as poorer than those living in other areas [23].",
     {"entities": []}),
    
    ("Elevated rates of opioid use in the region likely intersect with family planning practices in a variety of ways.",
     {"entities": [(18, 24, NT)]}),
    
    ("3.1.2. Appropriate Outreach Materials",
     {"entities": []}),
    
    ("Spinal epidural abscess (SEA) is a rare but life-threatening infection; recent epidemiologic studies report an increased incidence of SEA over the past two decades [1, 2].",
     {"entities": []}),
 #120   
    ("Review of laboratory tests revealed a hemoglobin of 11.1 g/dL (nonpregnant reference range: 12-14 g/dL), hematocrit of 33.1% (nonpregnant reference range: 37%-48%),",
     {"entities": []}),
    
    ("The use of cannabis during pregnancy could produce neurochemical alterations both in humans and in research animals.",
     {"entities": []}),
    
    ("Chronic non-malignant pain (CNMP) affects between an estimated 11% and 20% of the population in Europe and USA and can impact heavily on people’s quality of life.",
     {"entities": []}),
    
    ("Another review, which identified 11 patient survey studies, found that between 40 and 94% of prescribed pills went unused, with one outlier reporting roughly 10% unused (57).",
     {"entities": []}),
    
    ("KORs are Gi/o protein-coupled receptors highly expressed in the midbrain dopamine system (Mansour et al., 1996)",
     {"entities": [(0, 4, PHYS), (64, 88, LABEL), (90, 97, PER), (106, 110, "DATE")]}),
    
    ("Moreover, Margolis et al. (2006) found that KORs inhibit VTA dopamine neurons that project to the mPFC and basolateral amygdala, but not those that project to the NAc.",
     {"entities": [(10, 18, PER), (27, 31, "DATE"), (44, 48, PHYS), (49, 56, FUNC), (57, 60, LABEL), (61, 69, NT)]}),
    
    ("Furthermore, the activation of KOR decreases the amplitude of excitatory (Margolis et al., 2005) and inhibitory (Ford et al., 2007) postsynaptic currents into midbrain dopamine neurons.",
     {"entities": [(31, 34, PHYS), (35, 72, FUNC), (74, 82, PER), (91, 95, "DATE"), (113, 117, PER), (126, 130, "DATE"), (159, 184, LABEL)]}),
    
    ("How do KORs modulate dopamine signaling to elaborate motivated behaviors and when does it result in a sensitized compulsive behavior?",
     {"entities": [(7, 11, PHYS), (21, 29, NT)]}),
    
    ("AE and JF wrote the first draft of the manuscript with input from MA.",
     {"entities": []}),
    
    ("The work of the authors cited in this review has been supported by FONDECYT grant numbers: 1110352 and 1150200 to MA; 1141088 to JF; DIPOG grant 391340281 to JF; FONDECYT Postdoctoral fellow 3170497 to JC and 3190843 to AE.",
     {"entities": []}),
  #130  
    ("An earlier onset of OCD symptoms is observed in men compared with women (Mathis et al., 2011), with women showing more prevalence of contamination and cleaning symptoms (Labad et al., 2008).",
     {"entities": [(73, 79, PER), (88, 92, "DATE"), (170, 175, PER), (184, 188, "DATE")]}),
    
    ("Second, we entered the gene list, selected identifiers as official gene symbols, selected list types as gene lists, and submitted lists.",
     {"entities": []}),
    
    ("For given DEGs identified between the isotonic NP cells and hypertonic NP cells by the above analysis (see the “Identification of DEGs” section), function and pathway enrichment analysis was carried out with the following ontology sources",
     {"entities": []}),
    
    ("Enrichment analysis of gene ontology and KEGG by gene set enrichment analysis (GSEA)\nThe gene sequences were obtained from isotonic and hypertonic NP cells.",
     {"entities": []}),
    
    ("In this study, we performed GSEA analysis on gene sequences of nucleus pulposus under isotonic and hypertonic NP cells as follows.",
     {"entities": [(63, 79, LABEL)]}),
    
    ("The R language was used to perform the clustering analysis of significant genes based on the gene expression level. ",
     {"entities": []}),
    
    ("To perform the Gene Ontology and KEGG analysis of DEGs, the DAVID online tool was implemented.",
     {"entities": []}),
    
    ("However, the role of CXCL13 in pain was contrary to our expectation.",
     {"entities": []}),
    
    ("Chapman reported that somatostatin has a marked antinociceptive function",
     {"entities": [(0, 7, PER), (22, 34, NT)]}),
    
    ("Finally, the enrichment results of Gene Ontology and KEGG are presented.",
     {"entities": []}),

    ("Through gene enrichment analysis of DEGs, the influence of osmotic pressure on gene expression in NP cells was comprehensively summarized: regulation of extracellular matrix organization and the JAK/STAT signalling pathway.",
     {"entities": [(195, 203, PHYS)]}),
    
    ("Metascape (http://metascape.org/gp/index.html#/main/step1)74 was used to construct the PPI network and screen the significant module.",
     {"entities": []}),
    
    ("Moreover, the Search Tool for the Retrieval of Interacting Genes (STRING, http://string.embl.de/) was also applied to construct the PPI network, and Cytoscape was used to present the network",
     {"entities": []}),
    
    ("A Venn diagram was delineated to identify significant common genes among “Metascape_MCODE”, “Cytoscape_MCODE”, and “Cytoscape_cytoHubba” by FunRich software (http://www.funrich.org).",
     {"entities": []}),
    
    ("The comparative toxicogenomics database (http://ctdbase.org/) is a web-based tool that provides information about interactions between chemicals and gene products and their relationships to diseases",
     {"entities": []}),
    
    ("There was also a positive association between the relative expression of OPRL1 and the relative expression of CCL5.",
     {"entities": [(73, 78, PHYS), (110, 114, PHYS)]}),
    
    ("The miRNAs that regulate the four significant genes were screened out with TargetScan",
     {"entities": [(4, 10, PHYS)]}),
    
    ("However, the expression of CXCL13 was negatively related to the expression of CCL5.",
     {"entities": [(27, 33, PHYS), (78, 82, PHYS)]}),
    
    ("Enrichment plot: Gene Ontology_LYSOSOME_LOCALIZATION.",
     {"entities": []}),
    
    ("Ontology enrichment analysis by GSEA indicated that 1274/4081 genes were upregulated in hypertonic NP cells.",
     {"entities": []}),
 #150   
    ("Two of three available reviewers (TH, JB, or NH) independently screened the titles/abstracts for eligibility.",
     {"entities": []}),
    
    ("The content is solely the responsibility of the authors and does not necessarily represent the official views of the NIH, the Food and Drug Administration, or the American Heart Association.",
     {"entities": []}),
    
    ("While other disciplines (e.g. economics, [12] moral reasoning, [13] social psychology [14]) have explored the conditions under which hypothetical decisions accurately reflect real-world decisions.",
     {"entities": []}),
    
    ("Table 1 presents participant characteristics by tobacco use status. Of the total sample, 65.4% were never users (n\xa0=\xa0743), 4.7% were cigarette only users (n\xa0=\xa053), 3.3% were smokeless only users (n\xa0=\xa038), 5.6% were e-cigarette only users (n\xa0=\xa064), and 21.0% were polytobacco users (n\xa0=\xa0238).",
     {"entities": []}),
    
    ("In a US regional adolescent sample (11-18\u2009years of age), over 80% of those engaged in opioid PDM endorsed pain relief as a motive, though other motives could be selected as well.",
     {"entities": []}),
    
    ("In particular, the links between major depressive disorder, depressive symptoms and/or suicidality and opioid PDM are robust and well-established in adolescents.",
     {"entities": []}),
    
    ("Limited evidence from the NSDUH suggests that links between opioid PDM and other substance use vary by age group,101 with evidence both that past-year benzodiazepine PDM is less likely with aging among those engaged in opioid PDM but that frequency of past-year benzodiazepine PDM is somewhat higher in those 26 and older.",
     {"entities": []}),
    
    ("Notably, while the pattern of stimulant PDM prevalence mirrors other medication classes, nationally representative US data and multi-national administrative pharmacy data indicate that stimulant use patterns differ, with increases through childhood and adolescence to a peak in young adulthood, followed by declines.",
     {"entities": []}),
    
    ("The presence of antinociceptive activity at a low level of NO suggests the importance of NO in the modulation of nociceptive transmission.",
     {"entities": [(59, 61, NT), (89, 91, NT)]}),
    
    ("Based on the results obtained, it is plausible to suggest that modulation of cGMP synthesis plays a role in the nociceptive transmission.",
     {"entities": [(77, 80, PHYS)]}),
 #160   
    ("However, the inhibition of guanylyl cyclase neither helps to enhance nor play a role in the antinociceptive activity of MEDL.",
     {"entities": [(27, 43, PHYS), (120, 124, PHYS), (92, 116, FUNC)]}),
    
    ("Finally, no association was found between housing status (using the categories No Housing Problem, Housing Problem, No Fixed Abode), χ2 (2) = 2.05, p > .05.",
     {"entities": []}),
    
    ("Functional annotation for DEGs with database for annotation, visualization and integrated discovery (DAVID)\nThe DAVID (https://david.ncifcrf.gov/home.jsp) (version 6.8)71 was one online analysis tool suite with the functional annotation for Gene Ontology72 and Kyoto Encyclopedia of Genes and Genomes (KEGG)73.",
     {"entities": []}),
    
    ("As a fully functional package, the limma R package included the original data input and preprocessing capabilities of complementary DNA (cDNA) chips extracted from NP cells, as well as a linear model for analysing differentially expressed genes.",
     {"entities": []}),
    
    ("Oh found that subcutaneous injection of CCL5 in mice produced allodynia 32.",
     {"entities": [(0, 2, PER), (41, 45, PHYS), (62, 71, FUNC)]}),
    
    ("In addition, the analgesic activity of morphine could be attenuated by chemokines, especially CCL5 and CXCL1236.",
     {"entities": [(17, 35, FUNC), (94, 98, PHYS), (103, 111, PHYS)]}),
    
    ("KEGG enrichment analysis by GSEA indicated that 70/168 gene sets were upregulated in hypertonic NP cells compared to isotonic NP cells, while 98/168 gene sets were downregulated.",
     {"entities": []}),
    
    ("First, while our search strategy sought to encompass as many synonyms for ‘hypothetical’ and ‘real-world’ decisions as possible, there are likely studies touching on this issue that were not captured by our search.",
     {"entities": []}),
    
    ("Five distinct subtypes of muscarinic acetylcholine receptors (M1–M5) have been identified in the human genome [1].",
     {"entities": [(26, 60, PHYS)]}),
  #170  
    ("M5 muscarinic receptors are expressed solely in the substantia nigra and ventral tegmental area (VTA) [7].",
     {"entities": [(0, 23, PHYS), (52, 68, LABEL), (73, 95, LABEL), (97, 100, LABEL)]}),
   
    ("Cholinergic neurons in the nucleus accumbens (NAcc) project to VTA, where they stimulate dopaminergic neurons.",
     {"entities": [(0, 9, NT), (27, 44, LABEL), (46, 50, LABEL), (63, 66, LABEL), (79, 101, FUNC)]}),
    
    ("The VTA dopaminergic neurons project back to NAcc, where they stimulate cholinergic neurons.",
     {"entities": [(4, 7, LABEL), (8, 20, NT), (45, 49, LABEL), (62, 83, FUNC)]}),
    
    ("This positive feedback works as the reward circuit [87].",
     {"entities": []}),
    
    ("Gastro-oesophageal reflux18 (17.3)Food allergy/intolerance/sensitivity17 (16.4)Dysbiosis or parasites8 (7.7)Liver and biliary dysfunction and disease6 (5.8)",
     {"entities": []}),
    
    ("Sociodemographic characteristicsn (%)Patient Sex (n = 851) Female618 (72.6) Male233 (27.4)Patient Age (n = 835) Up to 5 years21 (2.5) 6–12 years21 (2.5) 13–17 years10 (1.2) 18–25 years56 (6.7) 26–35 years129 (15.5) 36–45 years169 (20.2) 46–55 years163 (19.5) 56–65 years161 (19.3) 66–75 years68 (8.1) 76–85 years28 (3.4) 86 years and over9 (1.1)",
     {"entities": []}),
    
    ("The study rigorously followed international ethical recommendations for medical research and was conducted under the ethical principles stipulated in the Declaration of Helsinki.",
     {"entities": []}),
    
    ("olycystic ovarian syndrome (PCOS)9 (17.7)Endometriosis6 (11.7)Fibroids and other benign tumours3 (5.9)",
     {"entities": []}),
    
    ("Another orally bioavailable compound, LBP1, showed anti-allodynic and anti-hyperalgesic effects in a rat model of neuropathic pain without catalepsy [92].",
     {"entities": [(38, 42, PHYS)]}),
    
    ("Stress-induced GABA release in the BLA and behavior in the FST were thus compared in C57 and DBA bearing a selective 5-HT depletion in mPFC.",
     {"entities": [(15, 19, NT), (35, 38, LABEL), (117, 121, NT), (135, 139, LABEL)]}),
   #180 
    ("The apparatus was a circular open field, 60cm in diameter and 20cm in height.",
     {"entities": []}),
    
    ("The microdialysis probe was connected to a CMA/100 pump (Carnegie Medicine, Stockholm, Sweden) through PE-20 tubing and an ultra-low torque dual channel liquid swivel (Model 375/D/22QM, Instech Laboratories, Inc., Plymouth Meeting, PA) to allow free movement.",
     {"entities": []}),

    ("Data on the effect of restraint stress on 5-HT release in mpFC and GABA release in BLA were statistically analyzed by repeated-measures analysis of variance (ANOVA) with 2 between factors",
     {"entities": [(42, 46, NT), (58, 62, LABEL), (67, 71, NT), (83, 86, LABEL)]}),
    
    ("Effects of strain (C57 sham, DBA sham) and of selective prefrontal cortical serotonin (5-HT) depletion in the medial prefrontal cortex (mpFC) of C57 mice.",
     {"entities": [(56, 75, LABEL), (77, 85, NT), (87, 91, NT), (110, 134, LABEL), (136, 140, LABEL)]}),
    
    ("Twenty-four human participants completed the behavioral paradigm in the MRI scanner (12 females, 12 males; age range: 18–30).",
     {"entities": []}),
    
    ("Recent findings of the increased periaqueductal gray (PAG) and inverse deactivation of VMPFC with higher punishments of unfairness are consistent with reactive aggression response.",
     {"entities": [(33, 52, LABEL), (54, 57, LABEL), (87, 92, LABEL), (151, 179, FUNC)]}),
    
    ("Regional homogeneity (ReHo) measures the temporal synchronization of the time series of an area's nearest neighbors (Zang et al., 2004).",
     {"entities": [(117, 121, PER), (130, 134, "DATE")]}),
      
    ("Cover stories are always a challenge in social decision-making research that employs game paradigms.",
     {"entities": []}),
    
    ("Together, SPECT, PET, and genetic fMRI studies suggest that brain DA is involved in obesity.",
     {"entities": [(60, 65, LABEL), (66, 68, NT), (84, 91, FUNC)]}),
    
    ("Often dozens of potent opioid pills were prescribed for fairly minor to moderate and short-lived, acute pain (e.g., tooth extraction, minor surgery).",
     {"entities": []}),
 #190   
    ("Presently, there is no established effective method of preventing PPSP after thoracic surgery.",
     {"entities": []}),
    
    ("In comparison, a recent smaller study reported a significant risk reduction using a combination of pregabalin and ketamine, with an infusion of ketamine (0.1 mg/kg/hr) for 48 hrs after surgery in cardiac surgery patients.",
     {"entities": []}),
    
    ("Characteristics of the study population of ASD surgery patients were presented overall and by chronic and nonchronic preoperative opioid use.",
     {"entities": []}),
    
    ("The samples were intervertebral disc NP cells obtained from patients undergoing discectomy prior to surgery for lumbar interbody fusion or lumbar disc herniation.",
     {"entities": []}),
    
    ("The package could be obtained from the open website (http://www.bioconductor.org/packages/release/bioc/html/limma.html)",
     {"entities": []}),
    
    ("For example, while the morphine pathway operates across at least two cell types6, mechanisms of intermediate shuttling between cells are unexplored and transport proteins need to be identified.",
     {"entities": []}),
    
    ("The brain systems that generate and apply reappraisal strategies include the prefrontal, dorsal anterior cingulate (dACC), and inferior parietal cortices (Ochsner et al., 2012).",
     {"entities": [(23, 64, FUNC), (77, 87, LABEL), (89, 114, LABEL), (116, 120, LABEL), (127, 153, LABEL), (155, 162, PER), (171, 175, "DATE")]}),
    
    ("The lethal effects of mu-opioid agonists are primarily due to respiratory depression via their actions in brainstem respiratory nuclei, specifically the pre-Bötzinger complex and the parabrachial nucleus.",
     {"entities": [(22, 40, PHYS), (62, 84, FUNC), (105, 133, LABEL), (152, 173, LABEL), (182, 202, LABEL)]}),
    
    ("Theorists from disparate disciplines assume that in tasks such as the IGT, where participants make repeated choices between two or more alternatives with differing outcomes, healthy individuals attempt to maximize net rewards over time",
     {"entities": []}),
    
    ("The only hint I can give you, and the most important thing to note is this: Out of these four decks of cards, there are some that are worse than others, and to win you should try to stay away from bad decks.",
     {"entities": []}),
#200    
    ("Tobacco use history appears to influence harm perceptions. Cigarette only users, polytobacco users, and e-cigarette only users were less likely to indicate that e-cigarettes cause health problems or addiction than never users.",
     {"entities": []}),
    
    ("Research reported in this publication was supported, in part, by the National Heart, Lung, and Blood Institute (NHLBI) of the National Institutes of Health (NIH) and FDA Center for Tobacco Products under Award Numbers P50HL120163 and U54HL120163.",
     {"entities": []}),
    
    ("CertaintyWhether the decision-maker is certain that their hypothetical decision is the same as would be their real-world decisionA high degree of certainty about a hypothetical decision makes it more likely to be consistent with a real decisionReview [50–52]Empirical [26, 53–55]Salience of/ Concern with the DecisionAmount of importance placed on hypothetical decisionGreater engagement/concern associated with greater consistencyEmpirical [20, 22, 31, 56–59]",
     {"entities": []}),
    
    ("For example, considerable work has examined delay discounting, i.e. the rate at which a good (or a health benefit) decreases in value depending on the amount of delay in receiving it.",
     {"entities": []}),
    
    ("Smoking causes health problemsSmokeless tobacco causes health problemsE-cigarettes cause health problemsAgreeDisagreePaAgreeDisagreePaAgreeDisagreePaTotal N (%)1049 (92.3)87 (7.7)947 (83.4)189 (16.6)618 (54.4)518 (45.6)",
     {"entities": []}),
    
    ("Neonatal rodent models support these findings by showing that repetitive acute pain during the first week of life can lead to negatively altered locomotor activity (65)",
     {"entities": []}),
    
    ("NP survives in a special ecological niche containing no distribution of blood vessels and nerves in which the osmotic pressure is significantly higher than that of plasma, enabling proteoglycans to be present in high concentrations2,3.",
     {"entities": [(0, 2, LABEL), (181, 194, PHYS)]}),
    
    ("It was reported that proteoglycan biglycan induced CXCL13 expression and aggravated lupus nephritis in mice through TLR2/4 on macrophages and dendritic cells58.",
     {"entities": [(51, 57, PHYS), (116, 122, PHYS)]}),
    
    ("This approach also allowed us to calculate the two‐dimensional association rate (k on) for interactions between μ‐ORs, that is, the formation of dimers, which we estimated to be 0.020±0.004 μm2 molecule−1 s−1. The estimated k on and k off",
     {"entities": [(112, 117, PHYS)]}),
    
    ("The NRS was positively associated with the relative expression of CCL5 (Pearson Rho = 0.951, P < 0.001) (Fig. 8F) and OPRL1 (Pearson Rho = 0.946, P < 0.001) (Fig. 8G).",
     {"entities": [(66, 70, PHYS)]}),
#210
    ("Expression of CCL5 and OPRL1 can sensitively and specifically predict NRS through the receiver operating characteristic curve",
     {"entities": [(14, 18, PHYS), (23, 28, PHYS)]}),
    
    ("Rates of benzodiazepine prescriptions increased with age, with the highest rates in the 65 to 80 year cohort.",
     {"entities": []}),
    
    ("begin{document}$$\frac{(\overline{{RR}}{}_{{last}{semester}2017}\,-\,{\overline{{RR}}}_{{first}{semester}2010})",
     {"entities": []}),
        
    ("setlength{\oddsidemargin}{-69pt}",
     {"entities": []}),
    
    ("The association (Kon) and dissociation (Koff) values were calculated using the Prism model.",
     {"entities": []}),
    
    ("Another 34±1 % of the receptors showed normal diffusion, that is, Brownian motion.",
     {"entities": []}),
    
    ("Compound 8 showed slower photobleaching in comparison to compound 9, consistent with the known photophysical properties of Cy5 and Cy3, respectively.",
     {"entities": []}),
    
    ("Central vein catheterization is a challenge in infants even in experienced hands.",
     {"entities": []}),
    
    ("A parallel is often drawn with pharmaceutical trials, where prior to definitive trials, considerable preparatory research involves many ‘hypothetical’ elements, including animal models, pilot participants (e.g. patients, clinicians who may differ from the ultimate target group), hypothetical decisions (i.e. would you participate in a study like this?) and pilot settings (e.g. laboratories).",
     {"entities": []}),
 #220   
    ("As a multidisciplinary field that studies how personal, organizational, technological, and systemic factors affect access to, quality, and cost of health-care [1], health services research often seeks to design complex interventions [2] to encourage changes in behaviour and decision making among actors (patients, providers, decision makers) within the system.",
     {"entities": []}),
    
    ("A health science librarian helped us develop an initial search strategy that included all target articles and involved keyword and titles searches for ‘decision making or behaviour’, ‘hypothetical situations’, and ‘real-world situations’, including synonyms, relevant Medical Subject Headings (MeSH) headings, etc.",
     {"entities": []}),
    
    ("Methodology",
     {"entities": []}),
    
    ("Perceptions of Addiction N (%)Smoking is addictive/difficult to quitSmokeless tobacco is addictive/difficult to quitE-cigarettes are addictive/ difficult to quitAgreeDisagreePaAgreeDisagreePaAgreeDisagreePaTotal N (%)1042 (91.7)94 (8.3)947 (83.4)189 (16.6)735 (64.7)401 (35.3)Gender0.0020.0190.28 Male573 (50.4)511 (89.2)62 (10.8)463 (80.8)110 (19.2)362 (63.2)211 (36.8) Female563 (49.6)531 (94.3)32 (5.7)484 (86.0)79 (14.0)373 (66.3)190 (33.7)Race/Ethnicity0.090.0010.015 White/Caucasian973 (88.4)900",
     {"entities": []}),
    
    ("i always freak out before a speech, always... this is the part where i'm supposed to ask my gp for zoloft or roofies but nooo,",
     {"entities": []}),
    
    ("generic xanax and adderall look way too alike. oh no what have i done...?",
     {"entities": []}),
    
    ("There’s nothing like an intimate setting and having to be honest and speak publicly … I think I still start feeling warm and get red in the face when it’s my turn to talk, but now that I’m one of those people that have been here awhile … I don’t feel quite so looked at or judged...",
     {"entities": []}),
    
    ("So, I took myself off of the Percocets, switched myself to the Suboxone [buprenorphine/naloxone]... and made it work until I could get in ...",
     {"entities": []}),
    
    ("and made it work until I could get in … So, I guess I tried to play my own doctor and tried to do what was right.",
     {"entities": []}),
    
    ("I told [the midwife] right away. I had some in my system, and I actually did it on purpose … She goes, ‘I found Subutex [buprenorphine] in your system.",
     {"entities": []}),
#230    
    ("Furthermore inter-ministerial consensus was needed to pilot MMT because as a controlled substance methadone could only be distributed according to special measures dictated by relevant government agencies.",
     {"entities": []}),
    
    ("Thus, when this strategy was first introduced, it was called needle social marketing—increasing the commercial availability and accessibility of needles in combination with health education about safe injecting practices and, in some cases, provision of free needles.",
     {"entities": []}),
    
    ("The traditional strategy for controlling HIV transmission through commercial sex workers has been the development of stricter laws to prevent risky behaviours,16 accompanied by raids on suspected sex establishments by public security officials.",
     {"entities": []}),
    
    ("HIV-related knowledge improved substantially, and the rate of bacterial sexually transmitted diseases fell.",
     {"entities": []}),
    
    ("The prevalence of gonorrhoea fell from about 26% at baseline to 4% after intervention, and the prevalence of chlamydia fell from about 41% to 26%.",
     {"entities": []}),
    
    ("•Free drugs to HIV-infected pregnant women to prevent mother-to-child transmission, and HIV testing of newborn babies.",
     {"entities": []}),
    
    ("•Free schooling for AIDS orphans.•Care and economic assistance to the households of people living with HIV/AIDS.",
     {"entities": []}),
    
    ("V041—COLORECTAL—Benign",
     {"entities": []}),
    
    ("V042—COLORECTAL—Benign",
     {"entities": []}),
    
    ("TAMIS WITH TECHNIQUE OF STABILIZATION OF THE PNEUMORRECT WITH GLOVE INTERPOSED AS A RESERVOIR",
     {"entities": []}),
    
    ("V045—COLORECTAL—Benign",
     {"entities": []}),
    
    ("KIDNEY MASS AND SIGMOID DIVERTICULAR STENOSIS: TWO FINE PROCEDURES AT THE SAME TIME",
     {"entities": []}),
    
    ("Kudo Department of Surgery, Kasai City Hospital, KASAI CITY, Japan",
     {"entities": []}),
    
    ("Gastrointestinal Surgery, Hospital Clinic Barcelona, BARCELONA, Spain",
     {"entities": []}),
    
    ("General and Emergency Surgery, ASST Monza—Desio Hospital, DESIO, Italy",
     {"entities": []}),
    
    ("General Surgery, Complejo Hospitalario Toledo, TOLEDO, Spain; 2General Surgery, Hospital tres culturas, TOLEDO, Spain",
     {"entities": []}),
    
    ("Central Military Emergency University Hospital, BUCHAREST, Romania",
     {"entities": []}),
    
    ("V107—HEPATO-BILIAIRY & PANCREAS—Pancreas",
     {"entities": []}),
    
    ("V128—HERNIA-ADHESIONS—Abdominal wall hernia",
     {"entities": []}),
    
    ("V158—ROBOTICS & NEW TECHNIQUES—Basic and Technical research",
     {"entities": []}),
    
    ("The differences in devaluation sensitivity of ST and Non-ST rats in Experiment 2 are consistent with our prior study using illness-induced outcome devaluation after limited training (Nasser et al., 2015).",
     {"entities": [(183, 189, PER), (192, 202, "DATE")]}),
    
    ("Yet, other factors can impact instrumental devaluation sensitivity, including the amount of reinforcer experience (Adams, 1982)",
     {"entities": [(115, 119, PER), (122, 126, "DATE")]}),
    
    ("While we do not observe the emergence of a non-preferred lever approach in GT rats under devalued relative to valued conditions, others have (Morrison et al., 2015).",
     {"entities": [(142, 150, PER), (159, 163, "DATE")]}),
    
    ("The countries included were identified by the World Naturopathic Federation as having sufficient infrastructure within the naturopathic profession to facilitate recruitment while also permitting global geographical distribution.",
     {"entities": []}),
    
    ("F. Antonakopoulos1, P. Athanasopoulos1, A. Ioannidis1, M. Konstantinidis2, K. Konstantinidis11General Surgery, Athens Medical Center, MAROUSI, ATHENS, Greece; 2Medical School of Athens, National Kapodistrian University of Athens, ATHENS, Greece",
     {"entities": []}),
    
    ("B. Bascuas Rodrigo1, J. Bellido Luque1, C. Dominguez Sanchez1, A. Bellido2, J. Gomez2, J.M. Suarez2, I. Sanchez-Matamoros Martin1, A. Nogales Muñoz1, F. Oliva Mompean11General Surgery, SAS, SEVILLA, Spain; 2General Surgery, Quiron Salud, SEVILLA, Spain",
     {"entities": []}),
    
    ("We present the case of a 31-year-old woman, BMI 40 kg/m2, with previous laparoscopic gastric sleeve and posterior reintervention using open approach.",
     {"entities": []}),
    
    ("F. Ferrara, F. Fiori, D. Gentile, D. Gobatti, M. Stella Department of Surgery, ASST Santi Paolo e Carlo, MILAN, Italy",
     {"entities": []}),
    
    ("M.V. Sosa1, M.P. Fernández2, A. Senent3, I. Alarcón4, L. Tallón3, J. Tinoco3, F.J. Padillo3, S. Morales-Conde41Servicio de Cirugía General y Digestiva,",
     {"entities": []}),
    
    ("J. Trébol1, A.M. Rodríguez1, A.B. Sánchez-Casado1, A. García-Plaza1, J.I. González-Muñoz1, A. Carabias-Orgaz2, L. Muñoz-Bellvis11General and Digestive Tract",
     {"entities": []}),
    
    ("The patient is the put in supine position with a 15° anti-trendelemburg angle. Three robotic trocars (two 8 mm and one 12 mm) are placed and the robot docking is made from the patient left shoulder.",
     {"entities": []}),
    
    ("The patient was placed in a supine position, with 15° anti-Trendelenburg inclination. The trocars were positioned according with the Intuitive indication for the upper quadrants surgery.",
     {"entities": []}),
    
    ("The placement of the patient on the operating table should be in decubitus, with right lateral inclination, at 20-30° on the horizontal surface.",
     {"entities": []}),
    
    ("The major presenting symptoms were abdominal pain (82.86%), nausea (77.14%), and vomiting (65.71%). Abdominal computed tomography scan with contrast (82.86%) was commonly used for confirmation of diagnosis.",
     {"entities": []}),
    
    ("1Inselspital, Radiation Oncology, Bern, Switzerland; 2Kantonsspital Baden, Radiology, Baden, Switzerland; 3Paul Scherrer Institute, Center for Proton Therapy, Villigen PSI West, Switzerland",
     {"entities": []}),
    
    ("A retrospective cross-sectional study was conducted on 152 patients with T1DM, aged between 1 and 18 years, who were followed up at the Second Pediatric Clinic Cluj-Napoca",
     {"entities": []}),
    
    ("Regional Institute of Gastroenterology and Hepatology, CLUJ-NAPOCA, Romania; 2Anesthesiology-Surgical Propedeutics, University of Agricultural Sciences and Veterinary Medicine, CLUJ-NAPOCA, Romania; 3Radiology, Regional Institute of Gastroenterology and Hepatology, CLUJ-NAPOCA, Romania; 4Urology, Training and Research Center, Prof. Dr. Sergiu Duca, CLUJ-NAPOCA, Romania; 5General Surgery, Training and Research Center, Prof. Dr. Sergiu Duca, CLUJ-NAPOCA, Romania",
     {"entities": []}),
    
    ("D. Munteanu, C. Popa, I.C. Puia, A. Munteanu, N. al Hajjar Surgery, Regional Institute of Gastroenterology and Hepatology, O. Fodor, CLUJ-NAPOCA, Romania",
     {"entities": []}),
    
    ("All statistical analyses were conducted using SPSS software, version 23.0 (IBM Corp., Armonk, NY, USA). A p-value < 0.05 was considered to be significant81.",
     {"entities": []}),
    
    ("Psychopathy also predicted reduced response in the amygdala and dACC (Figure 2), although dACC activity was significantly correlated with Factor 2, but not Factor 1 (Supplementary Table 2).",
     {"entities": [(51, 59, LABEL), (64, 68, LABEL), (90, 94, LABEL)]}),
    
    ("The dACC has also previously been shown to be an important node for orchestrating interactions between widespread cortical networks in service of moral judgment.52",
     {"entities": [(4, 8, LABEL)]}),
    
    ("While the evidence to date shows that the OFC/vmPFC plays a key role in reward processing (Bartra et al., 2013",
     {"entities": [(42, 45, LABEL), (46, 51, LABEL), (91, 97, PER), (106, 110, "DATE"), (72, 89, FUNC)]}),
    
    ("This includes OFC/vmPFC activity, which can vary with probability contingencies, effort and the temporal delay between response and outcome (Haber & Knutson, 2010).",
     {"entities": [(14, 17, LABEL), (18, 23, LABEL), (141, 146, PER), (149, 156, PER), (158, 162, "DATE"), (54, 79, FUNC)]}),
    
    ("Additionally, the region of the ventral striatum where overlapping activation between reward and loss anticipation resided is considered to be part of the NAcc core (Xia et al., 2017).",
     {"entities": [(32, 48, LABEL), (155, 164, LABEL), (166, 169, PER), (178, 182, "DATE"), (86, 92, FUNC), (97, 114, FUNC)]}),
    
    ("This is the first time for a meta‐analysis to detect amygdala activation during both reward and loss anticipation, as this region is typically associated with loss processing.",
     {"entities": [(53, 61, LABEL), (85, 91, FUNC), (96, 113, FUNC), (159, 174, FUNC)]}),
    
    ("There is a report that self-esteem is associated with hippocampal volume and the cortisol response to a psychosocial stress [30].",
     {"entities": [(54, 65, LABEL), (81, 98, PHYS), (104, 123, FUNC)]}),
    
    ("The cluster size was determined through a Monte Carlo simulation using AFNI’s AlphaSim program (http://afni.nimh.nih.gov/afni/doc/manual/AlphaSim) with 10,000 iterations.",
     {"entities": []}),
    
    ("L. Dorsal MPFC",
     {"entities": [(3 ,14, LABEL)]}),
    
    ("In a follow up study to our identification of risk coding neurons in the OFC we identified an error-related signal in OFC neurons related to risk, namely a risk prediction error (O’Neill and Schultz, 2013).",
     {"entities": [(73, 76, LABEL), (118, 121, LABEL), (179, 186, PER), (191, 197, PER), (200, 204, "DATE"), (94, 107, FUNC), (156, 177, FUNC)]}),
    
    ("A previous work including a food-related task discovered decreased reward sensitivity associated with alterations in the putamen activity after acute stress induction (Born et al., 2010).",
     {"entities": [(121, 128, LABEL), (168, 172, PER), (181, 185, "DATE")]}),
    
    ("The prefrontal cortex is related to cognitive control and goal-directed behaviors [32].",
     {"entities": [(4, 21, LABEL), (46, 53, FUNC), (58, 81, FUNC)]}),
    
    ("The orbitofrontal cortex (OFC) contributes to emotion-based learning and decision making [36,37] and is proposed to be a key region in negative urgency [1].",
     {"entities": [(4, 24, LABEL), (26, 29, LABEL), (46, 68, FUNC), (73, 88, FUNC), (135, 151, FUNC)]}),
    
    ("The mPFC projects to the VTA and the NAcc.",
     {"entities": [(4, 8, LABEL), (25, 28, LABEL), (37, 41, LABEL)]}),
    
    ("The DP receives inputs from the PBN and the RMTg.",
     {"entities": [(4, 6, LABEL), (32, 35, LABEL), (44, 48, LABEL)]}),
    
    ("There is a dopaminergic projection from the VTA to the Dorsal Raphe (DRN).",
     {"entities": [(11, 23, NT), (44, 47, LABEL), (55, 67, LABEL), (69, 72, LABEL)]}),
    
    ("The hindbrain receives inputs from many regions.",
     {"entities": [(4, 13, LABEL)]}),
    
    ("The risky option comprised equal probabilities of a prize (£6, £9, or £12) or £0.",
     {"entities": []}),
    
    ("Five participants did not enter into state 1, 21 participants did not enter into state 2, 22 participants did not enter into state 3, 19 did not enter into state 4 and 33 did not enter into state 5.",
     {"entities": []}),
    
    ("On average, participants spent 39.53 percent of their time in state 1 (s.d. = 27.54), 16.55 percent of their time in state 2 (s.d. = 16.59), 16.02 percent of their time in state 3 (s.d. = 15.72), 15.53 of their time in state 4 (s.d. = 17.06) and 12.37 percent of the time is state 5 (s.d. = 16.15).",
     {"entities": []}),
    
    ("The dwell time on average was 20.65 (s.d. = 26.37) for state 1, 10.96 (s.d. = 10.52) for state 2, 10.93 (s.d. = 8.35) for state 3, 11.90 (s.d. = 11.37) for state 4 and 10.76 (s.d. = 11.19) for state 5. Table 3.Percent of time spent in each CCN stateState 1 (%)State 2 (%)State 3 (%)State 4 (%)State 5 (%)1st analysis34.7417.9817.9217.1412.",
     {"entities": []}),
    
    ("Insula, Dorsal Anterior Cingulate, Thalamus (45,9,-3), (-3,-27,-3), (-9,21,24)",
     {"entities": [(0, 6, LABEL), (8, 33, LABEL), (35, 43, LABEL)]}),
    
    ("We therefore aimed to develop a task that effectively probed emotional facial recognition. The Emotion Recognition Task (ERT) included in the CANTAB battery (Cambridge Cognition Ltd) has proven to be a promising task examining emotion recognition in clinical populations.",
     {"entities": []}),
    
    ("There are a number of batteries that include a limited number of affective tasks in predominately “cold” cognitive test batteries (e.g., CANTAB; www.cambridgecognition.com, MATRICS; www.matricsinc.org, CogState; www.cogstate.com, WebNeuro; www.brainresource.com).",
     {"entities": []}),
    
    ("The amygdala has been reported to be related to life satisfaction [27] and to be correlated with the dorsal MPFC while trying to increase positive emotion [53].",
     {"entities": [(4, 12, LABEL), (101, 112, LABEL), (48, 65, FUNC), (129, 154, FUNC)]}),
    
    ("In the positive word condition, the HLS group showed significantly increased functional connectivity of the dorsal MPFC with various regions including the left amygdala, left insula, and bilateral TPJ, whereas the LLS group revealed it only with the left PCC.",
     {"entities": [(108, 119, LABEL), (160, 168, LABEL), (175, 181, LABEL), (197, 200, LABEL), (255, 258, LABEL)]}),
    
    ("Participants were asked to respond as accurately and as quickly as possible. Four different types of distractors were possible: (1) a disgusting picture (e.g., of vomit, wounds, or spiders) at the location where the target letter would subsequently be presented, called the disgust condition; (2) a neutral picture presented at the target location, called the neutral ipsilateral condition; (3) a picture displaying a couple in an erotic situation displayed on the contralateral side of the screen relative to the target location, called the erotic condition; and (4) a neutral picture presented on the contralateral side of the screen, called the neutral contralateral condition (Figure 1).",
     {"entities": []}),

    ("Subjects completed a pre-scan questionnaire (see Supplementary Note 7 for an English version) and a practice block with a trackball outside the scanner to make sure the instructions and procedures were clear.",
     {"entities": []}),
    
    ("Pre-testing of our messages also revealed that women found the messages clearer and more persuasive than did men.",
     {"entities": []}),
    
    ("Statistical analyses of behavioral data were performed using R software (www.r-project.org).",
     {"entities": []}),
    
    ("In addition, the context effect observed here was not due to reward-frequency bias the subjects experienced in the pre-fMRI session (S2 Fig).",
     {"entities": []}),
    
    ("Recent studies show that several subcortical brain regions in the septum and the striatum contain populations of neurons that signal the graded level of reward uncertainty 56, 57.",
     {"entities": [(33, 58, LABEL), (66, 72, LABEL), (81, 89, LABEL), (153, 171, FUNC)]}),
    
    ("On the other hand, injections in the amygdala and the medio-lateral septum, which projects directly and indirectly to the PVN, did not alter basal ACTH levels, but reduced stress-induced ACTH (Neumann et al., 2000a).",
     {"entities": [(37, 45, LABEL), (54, 74, LABEL), (122, 125, LABEL), (147, 151, PHYS), (172, 191, FUNC)]}),
    
    ("Demographic characteristics of sample (N = 200), stratified by age, IQ, gender, and ethnicity for the standardization of the EMOTICOM neuropsychological test battery.",
     {"entities": []}),
    
    ("Task 15: Ultimatum Game",
     {"entities": []}),
    
    ("As a summary of the state of the literature to date, a recently published meta-analysis of structural and functional neuroimaging studies in OCD examined data from VBM studies enrolling 928 patients vs. 942 controls, and fMRI studies of inhibitory control enrolling 287 patients and 284 controls (Norman et al., 2016).",
     {"entities": [(297, 303, PER), (312, 316, "DATE")]}),
    
    ("Full list of neuropsychological tasks with outcome measures which are included in the EMOTICOM neuropsychological test battery.",
     {"entities": []}),
    
    ("In this paper we have presented data from 200 participants' performance to demonstrate that these requirements are met by the EMOTICOM neuropsychological test battery.",
     {"entities": []}),
    
    ("This focus on highly motivated subjects may explain why the study found activation overlapping with economic reward-related signals.",
     {"entities": []}),
    
    ("Our specific question was to what extent adACC/dmPFC responses are differentially controlled by the prevailing excitatory CS+ > US association verses the temporary inhibitory CS+ > noUS association governed by successful avoidance.",
     {"entities": [(41, 46, LABEL), (47, 52, LABEL)]}),
    
    ("We hypothesized that individuals exhibiting greater aversive discounting in the form of greater avoidance of immediate losses would display greater adACC/dmPFC activation to a CS+ threat.",
     {"entities": [(148, 153, LABEL), (154, 159, LABEL), (52, 72, FUNC)]}),
    
    ("Participants were not informed about US omission.",
     {"entities": []}),
    
    ("Although it is not possible to directly assess dopaminergic activity using functional MRI (fMRI), dopamine-related quantities such as reward prediction errors (14) are observed in BOLD activity within the SN/VTA (15, 16).",
     {"entities": [(47, 59, NT), (205, 207, LABEL), (208, 211, LABEL), (98, 106, NT), (134, 158, FUNC)]}),
    
    ("BOLD activity from anatomically defined SN/VTA is extracted and denoised (removing movement, breathing, and pulsatile artifacts) in real time.",
     {"entities": [(40, 42, LABEL), (43, 46, LABEL)]}),
    
    ("Subjects (n = 43) gambled more when options were presented against a background of low compared to high endogenous SN/VTA activity.",
     {"entities": [(115, 117, LABEL), (118, 121, LABEL)]}),
    
    ("We also found no interaction between risky option value (i.e., £6, £9, or £12) and activity [F(1.957, 82.208) = 0.493, P = 0.61], further supporting an association between low endogenous SN/VTA activity and a value-independent increase in risk taking.",
     {"entities": [(187, 189, LABEL), (190, 193, LABEL), (227, 250, FUNC)]}),
    
    ("Variability (i.e., SD) in SN/VTA BOLD activity was uncorrelated with the difference in risk taking between low and high activity across subjects (Spearman ρ = −0.19, P = 0.29).",
     {"entities": [(26, 28, LABEL), (29, 32, LABEL)]}),
    
    ("Changes in EC secreted factors following TGF-β1 stimulation also affects Th1 T-cell activation as shown in reduction in the levels of IFN-g.",
     {"entities": [(11, 30, PHYS), (41, 47, PHYS), (73, 83, PHYS), (134, 139, PHYS)]}),
    
    ("We report uptake of BSA into specific cell populations, mostly glia, within the hippocampus, temporal cortex and white matter, followed by prominent and long-lasting astro-glyial activation without apparent neuronal cell loss or hippocampal sclerosis.",
     {"entities": [(20, 23, PHYS), (80, 91, LABEL), (93, 108, LABEL), (113, 125, LABEL), (166, 178, PHYS),  (229, 240, LABEL)]}),
    
    ("Interestingly, in control, but not in architecture students, reaction times during the first repetition of the target were correlated with activation in multiple brain regions (cuneus, lingual gyrus, inferior parietal lobule, insula, and anterior cingulate cortex).",
     {"entities": [(177, 183, LABEL), (185, 198, LABEL), (200, 224, LABEL), (226, 232, LABEL), (238, 263, LABEL)]}),
    
    ("What we do know is that DA is released within the spinal cord during stepping activity, increases motor output, and modulates sensory transmission.",
     {"entities": [(24, 26, NT), (50, 61, LABEL), (88, 110, FUNC), (116, 146, FUNC)]}),
    
    ("By examining intrinsic and synaptic properties we show that DA acts on several ion channels to increase excitability.",
     {"entities": [(60, 62, NT), (79, 91, PHYS), (95, 116, FUNC)]}),
    
    ("b-wright@northwestern.edu",
     {"entities": []}),
    
    ("The striatum consists of GABAergic projection neurons and various types of interneurons.",
     {"entities": [(4, 12, LABEL), (25, 34, NT)]}),
    
    ("Our findings suggest that coding of movement by TANs in both regions overlaps to a larger degree than previously assumed, considering the segregation in the cortex-basal ganglia- thalamus-cortex circuits.",
     {"entities": [(157, 163, LABEL), (164, 177, LABEL), (179, 187, LABEL), (188, 194, LABEL)]}),
    
    ("Yet the differences in response patterns support the notion that the TANs in the dorsal and ventral striatum have distinct functions in associative tasks.",
     {"entities": [(81, 87, LABEL), (92, 108, LABEL)]}),
    
    ("These recordings demonstrated the existence of grid cells in the entorhinal cortex of this bat species.",
     {"entities": [(65, 82, LABEL)]}),
    
    ("These interactions involve the responsiveness of non-neuronal cells to classical neurotransmitters (e.g., glutamate and monoamines) and hormones (e.g., glucocorticoids), as well as the secretion and responsiveness of neurons and glia to low levels of inflammatory cytokines, such as interleukin IL-1, IL-6, and TNFα,",
     {"entities": [(71, 98, NT), (106, 115, NT), (120, 130, NT), (136, 144, PHYS), (152, 167, PHYS), (251, 273, PHYS), (283, 294, PHYS)]}),
    
    ("In the primary motor cortex (M1), several movement parameters are encoded in parallel.",
     {"entities": [(7, 27, LABEL), (29, 31, LABEL)]}),
    
    ("We were also able to characterize the complete population somatotopic tuning curve in different parts of M1.",
     {"entities": [(105, 107, LABEL)]}),
    
    ("Using calcium imaging and whole cell recordings accompanied by pharmacological agents, we explored persistent activity in the rat somatosensory cortex.",
     {"entities": [(130, 150, LABEL)]}),
    
    ("This activity is dependent on carbachol (CCh), an acetylcholine receptor agonist.",
     {"entities": [(30, 39, PHYS), (41, 44, PHYS), (50, 63, NT), (64, 80, PHYS)]}),
    
    ("Also alterations in GABA-A receptor subunits in the amygdala and hippocampus were observed in adulthood following juvenile stress.",
     {"entities": [(20, 44, PHYS), (52, 60, LABEL), (65, 76, LABEL)]}),
    
    ("Certain computations in the brain, such as identifying the direction of an approaching predator, must be completed fast and reliably.",
     {"entities": [(28, 33, LABEL)]}),
    
    ("The accessory olfactory bulb (AOB) is the first relay of sensory information originating from the vomeronasal organ (VNO), where pheromones are detected by vomeronasal receptors.",
     {"entities": [(4, 28, LABEL), (30, 33, LABEL), (98, 115, LABEL), (117, 120, LABEL), (129, 139, NT), (156, 177, LABEL)]}),
    
    ("VNO neurons project to the glomerular layer of the AOB, providing the main input to the AOB mitral cells.",
     {"entities": [(0, 3, LABEL), (27, 54, LABEL), (88, 91, LABEL)]}),
    
    ("Lockwood et al. (2016) showed that the subgenual anterior cingulate cortex (sgACC) was associated with reward learning only when individuals acted in a prosocial context, and this region signals a prosocial prediction error.",
     {"entities": [(0, 8, PER), (17, 21, "DATE"), (39, 74, LABEL), (76, 81, LABEL), (103, 118, FUNC), (187, 223, FUNC)]}),
    
    ("Consistent with the growing focus on the ACC, Apps et al. (2016) presented a model based on vicarious motivation and error processing whereby a specific region of ACC gyrus (ACCg) is involved in costs, benefits and errors during social interactions.",
     {"entities": [(41, 44, LABEL), (46, 50, PER), (59, 63, "DATE"), (163, 172, LABEL), (174, 178, LABEL), (229, 248, FUNC)]}),
    
    ("Participants were then asked to select the charity of their choice from a list including the following charities: British Red Cross, Save the Children Fund, Oxfam, The Salvation Army, Cancer Research UK and Macmillan Cancer Support.",
     {"entities": []}),
    
    ("Individual variation in the beta-weights of this dACC/MCC cluster was negatively associated with the amount of money obtained for oneself compared to that gained for charity (r(16) = −0.512, P = 0.030).",
     {"entities": [(49, 53, LABEL), (54, 57, LABEL), (101, 137, FUNC)]}),
    
    ("However, four regions (middle temporal gyrus, thalamus, post-central gyrus and precuneus) were engaged during stage 2 in GLM#2 which featured no parametric predictors, see Supplementary Information 6.",
     {"entities": [(23, 44, LABEL), (46, 54, LABEL), (56, 74, LABEL), (79, 88, LABEL)]}),
    
    ("We thus test for altered Blood-Oxygenation-Level-Dependent (BOLD) reactivity in PG and AD subjects with respect to both gains and losses in a LA network of interest (NOI) encompassing the regions of interest (ROIs) DLPFC, ventro-lateral prefrontal cortex (VLPFC), orbito-frontal cortex (OFC), amygdala, insula, VMPFC, striatum, midbrain, and dorsal raphe nucleus (DRN).",
     {"entities": [(215, 220, LABEL), (222, 254, LABEL), (256, 261, LABEL), (264, 285, LABEL), (287, 290, LABEL), (293, 301, LABEL), (303, 309, LABEL), (311, 316, LABEL), (318, 326, LABEL), (328, 336, LABEL), (342, 362, LABEL), (364, 367, LABEL)]}),
    
    ("In an exploratory supplemental analysis, two tailed Pearson's correlations were used to correlate task performance with demographic measures such as age, IQ and years of education.",
     {"entities": []}),
    
    ("of the visual angle for the behavioral taskErotic M(s.d.)Neutral M(s.d.)t-valueP-valueη2Error0.06(0.067)0.05(0.05)2.270.0260.05RT594.62(64.39)587.16(63.21)3.300.0010.10Mean gaze3.64(2.06)3.43(1.8)3.360.0010.11s.d. gaze0.51(0.62)0.39(0.42)3.300.0030.09",
     {"entities": []}),
    
    ("In the control condition, participants are asked to identify the age of a face (child, young adult, middle aged, elderly).",
     {"entities": []}),
    
    ("There are two conditions; one condition is a no lose condition whereby participants either win (£0.50 presented as 50p) or fail to win (0p)",
     {"entities": []}),
    
    ("Participants must learn, through sampling the circles, which of the two is the better option, with probabilities (unknown to participants) set at 70%/30%.",
     {"entities": []}),
    
    ("Task 7: The Monetary Incentive Reward (MIR) Task",
     {"entities": []}),
    
    ("The VTA regulates reward prediction error.",
     {"entities": [(4, 7, LABEL), (18, 41, FUNC)]}),
    
    ("The DP is a novel regulator of aversive behaviors.",
     {"entities": [(4, 6, LABEL), (31, 49, FUNC)]}),
    
    ("The midbrain and the hindbrain coordinate autonomic functions.",
     {"entities": [(4, 12, LABEL), (21, 30, LABEL), (42, 61, FUNC)]}),
    
    ("That is, both users and non-users wore significantly more sunscreen during the week following the session than during the week prior to the session [users: Mpre-scanning = 4.05, SDpre-scanning = 2.48, Mpost-scanning = 4.89, SDpost-scanning = 2.47, t(18) = 2.45, P = 0.012; non-users: (Mpre-scanning = 0, SDpre-scanning = 0, Mpost-scanning = 1.33, SDpost-scanning = 2.22, t(17) = 2.54, P = 0.010; Figure 2]. The increase in sunscreen use was not significantly different for users vs non-users t(35) = 0.79, p = 0.22.",
     {"entities": []}),
    
    ("Users and non-users alike also reported greater intentions to wear more sunscreen after the scan than before the scan [users: Mpre-scanning = 4.26, SDpre-scanning = 2.96, Mpost-scanning = 5.89, SDpost-scanning = 1.73, t(18) = 3.21, P = 0.002; non-users: Mpre-scanning = 0, SDpre-scanning = 0, Mpost-scanning = 4.00, SDpost-scanning = 2.85, t(17) = 5.96, P < 0.001].",
     {"entities": []}),
    
    ("The difference between Whygain and Whyloss was significant; that is, there was greater MPFC activity during Whygain relative to Whyloss messages in the whole sample [M = 0.25, SD = 0.63; t(34) = 2.31, P = 0.041].",
     {"entities": [(87, 91, LABEL)]}),
    
    ("In the spinal cord, MMP-9 inhibition blocks morphine-induced phosphorylation of NMDA receptors, ERK1/2, and cAMP response element binding proteins, and behavioral signs of morphine withdrawal (Liu et al., 2010).",
     {"entities": [(7, 18, LABEL), (20, 25, PHYS), (80, 84, PHYS), (108, 146, PHYS), (152, 191, FUNC), (193, 196, PER), (205, 209, "DATE")]}),
    
    ("This is the only observation regarding MMPs in the nucleus accumbens following nicotine exposure; another laboratory has examined these enzymes in the hippocampus and mPFC following nicotine CPP.",
     {"entities": [(39, 43, PHYS), (51, 68, LABEL), (151, 162, LABEL), (167, 171, LABEL)]}),
    
    ("Gelatinase activity was increased in NAcore of cocaine-extinguished compared with yoked-saline control rats, and 15 min of cue-induced reinstatement caused a further increase",
     {"entities": [(0, 19, PHYS), (37, 43, LABEL), (123, 148, FUNC)]}),
    
    ("No increases in MMP activity were measured in the dorsal striatum or accumbens shell after 15 min of cue-induced reinstatement",
     {"entities": [(16, 19, PHYS), (51, 65, LABEL), (69, 84, LABEL), (101, 126, FUNC)]}),
    
    ("Neither the enduring increase in gelatinase activity after extinction nor the increase elicited by 15 min of cue-induced reinstatement were accompanied by a change in NAcore protein content of MMP-2 or MMP-9, or the MMP-2/9 inhibitory protein TIMP-2",
     {"entities": [(33, 52, PHYS), (109, 134, FUNC), (167, 173, LABEL), (193, 198, PHYS), (202, 207, PHYS), (216, 223, PHYS), (243, 249, PHYS)]}),
    
    ("The intensity of cue-induced relapse is correlated with the induction of transient synaptic potentiation (t-SP) at glutamatergic synapses on medium spiny neurons (MSNs) in the nucleus accumbens core (NAcore) and requires spillover of glutamate from prefrontal cortical afferents.",
     {"entities": [(17, 36, FUNC), (115, 128, NT), (176, 198, LABEL), (200, 206, LABEL), (234, 243, NT), (249, 268, LABEL)]}),
    
    ("The nucleus accumbens core (NAcore) serves as a portal whereby cue-induced activity in cortical and limbic projections initiates goal directed behaviors, including drug seeking",
     {"entities": [(4, 26, LABEL), (28, 34, LABEL), (48, 83, FUNC), (87, 95, LABEL), (100, 106, LABEL), (129, 152, FUNC), (164, 176, FUNC)]}),
    
    ("Vascular compression of the trigeminal nerve has been accepted as the most common cause of classic trigeminal neuralgia (cTN) by the International Headache Society, the International Association for the Study of Pain, and the European Academy of Neurology.",
     {"entities": [(28, 44, LABEL), (91, 119, FUNC), (121, 124, FUNC)]}),
    
    ("During exposure of the facial nerve, the cisternal segment of the trigeminal nerve was exposed from its point of entry into the pons (ie, the root entry point of the nerve).",
     {"entities": [(23, 35, LABEL), (41, 82, LABEL), (128, 132, LABEL)]}),
    
    ("Coronal SSFP image demonstrates the left superior cerebellar artery (white arrowhead) contacting the left trigeminal nerve (black arrow).",
     {"entities": [(36, 67, LABEL), (101, 122, LABEL)]}),
    
    ("Exclusion criteria included those patients with a history of right- or left-sided facial pain, tic convulsif (ie, TN and HFS), or any prior surgery involving the trigeminal nerve.",
     {"entities": [(82, 93, FUNC), (95, 108, FUNC), (114, 124, FUNC), (162, 178, LABEL)]}),
    
    ("The rostromedial tegmental nucleus (RMTg), a GABAergic afferent to midbrain dopamine (DA) neurons, has been hypothesized to be broadly activated by aversive stimuli.",
     {"entities": [(4, 34, LABEL), (36, 40, LABEL), (45, 54, NT), (67, 75, NT), (77, 79, NT), (148, 164, FUNC)]}),
    
    ("We further found that valence-encoding RMTg neurons preferentially project to the DA-rich VTA versus other targets, and excitotoxic RMTg lesions greatly reduce aversive stimulus-induced inhibitions in VTA neurons",
     {"entities": [(22, 38, FUNC), (39, 43, LABEL), (82, 84, NT), (90, 93, LABEL), (120, 131, PHYS), (132, 136, LABEL), (160, 177, FUNC), (201, 204, LABEL)]}),
    
    ("RMTG neurons synapse onto tyrosine hydroxylase (TH) positive neurons in the VTA and substantia nigra, and electrical stimulation of the RMTg dramatically suppresses DA neuron firing",
     {"entities": [(0, 4, LABEL), (26, 46, PHYS), (48, 50, PHYS), (76, 79, LABEL), (84, 100, LABEL), (136, 140, LABEL), (154, 181, FUNC)]}),
    
    ("Recently, Romanov et al. (2017) [368] provided evidence of numerous novel neuronal phenotypes of hypothalamic cells using single cell RNA-Seq and DropSeq technologies,",
     {"entities": [(10, 17, PER), (26, 30, "DATE"), (97, 109, LABEL)]}),
    
    ("To address the paucity of genetic markers of the RMTg, we evaluated a transcription factor previously identified in the mouse RMTg: FoxP1 (Lahti et al. 2016).",
     {"entities": [(49, 53, LABEL), (126, 130, LABEL), (132, 137, PHYS)]}),
    
    ("In the same surgery, the mice were implanted bilaterally with chronic indwelling optic fibers (50-um core) aimed at the VTA (AP -3.1, ML +1.3, DV ?4.8 from dura, 10° angle).",
     {"entities": [(120, 123, LABEL)]}),
    
    ("With respect to opiate drugs, heroin administration leads to long-term alterations in gene expression in the NAc shell.",
     {"entities": [(16, 28, PHYS), (30, 51, FUNC), (109, 118, LABEL)]}),
    
    ("In addition to structural changes, opiate exposure also results in a change in synapse physiology of neurons in the ventral-tegmental area (Saal et al, 2003), hippocampus (Pu et al, 2002), and NAc (Dong et al, 2007).",
     {"entities": [(35, 51, FUNC), (116, 138, LABEL), (140, 144, PER), (152, 156, "DATE"), (159, 170, LABEL), (172, 174, PER), (182, 186, "DATE"), (193, 196, LABEL), (198, 202, PER), (210, 214, "DATE")]}),
    
    ("Recently, we found that re-exposure to heroin-conditioned cues results in acute synaptic depression of pyramidal neurons in the ventral mPFC",
     {"entities": [(39, 62, FUNC), (80, 99, PHYS), (103, 120, PHYS), (128, 140, LABEL)]}),
    
    ("A second set of mEC slides was stained for amyloid or the norepinephrine transporter (NET) with 10 min pretreatment in 80% formic acid, followed by 10 min incubation in a 0.3 N sodium hydroxide, 0.9% hydrogen peroxide solution, a block in 10% normal donkey serum with 0.05% Tween-20 and overnight incubation with the 4G8 antibody (1:1000, Convance) or a mouse anti-NET antibody (1:1000, NET05-2; MAb Technologies).",
     {"entities": [(16, 19, LABEL), (43, 50, PHYS), (58, 84, PHYS), (86, 89, PHYS)]}),
    
    ("We extended these findings to investigate additional locus coeruleus-innervated regions affected in Alzheimer's disease.",
     {"entities": [(53, 68, LABEL), (100, 119, FUNC)]}),
    
    ("Locus coeruleus activity and adrenergic receptor signaling in the hippocampus contribute to spatial learning",
     {"entities": [(0, 15, LABEL), (29, 58, PHYS), (66, 77, LABEL), (92, 108, FUNC)]}),
    
    ("DREADDs have been used to selectively activate locus coeruleus neurons and modulate rodent behaviour",
     {"entities": [(0, 7, PHYS), (47, 62, LABEL), (84, 100, FUNC)]}),
    
    ("We next examined the effects of locus coeruleus activation on reversal learning.",
     {"entities": [(32, 47, LABEL), (62, 79, FUNC)]}),
    
    ("Additionally, TgF344-AD rats had reduced locus coeruleus fibre density in the dentate gyrus and norepinephrine levels in the hippocampus.",
     {"entities": [(41, 56, LABEL), (78, 91, LABEL), (96, 110, NT), (125, 136, LABEL)]}),
    
    ("Abnormally low levels of forebrain norepinephrine have been reported in Alzheimer's disease",
     {"entities": [(25, 34, LABEL), (35, 49, NT), (72, 91, FUNC)]}),
    
    ("Notably, spatial reversal learning depends on long term depression within the hippocampus, and locus coeruleus electrical stimulation can induce long term depression in the dentate gyrus",
     {"entities": [(9, 34, FUNC), (46, 66, PHYS), (78, 89, LABEL), (95, 110, LABEL), (145, 165, PHYS), (173, 186, LABEL)]}),
    
    ("One of the most striking features of the locus coeruleus is the widespread efferent network, constituting the sole source of central nervous system noradrenaline, with axonal projections being found in all regions and layers of cortex (Levitt and Moore, 1978).",
     {"entities": [(41, 56, LABEL), (125, 147, LABEL), (148, 161, NT),  (202, 234, LABEL), (236, 242, PER), (247, 252, PER), (254, 258, "DATE")]}),
    
    ("Recordings from locus coeruleus have shown that these neurons have both tonic and phasic firing patterns, believed to have differential effects on behavior performance, arousal, and attention",
     {"entities": [(16, 31, LABEL), (147, 167, FUNC), (169, 176, FUNC), (182, 191, FUNC)]}),
    
    ("Thus locus coeruleus pairing might have just enhanced overall arousal and behavioral engagement, rather than have specifically promoted behaviorally-relevant plasticity.",
     {"entities":  [(4, 19, LABEL), (62, 69, FUNC), (74, 95, FUNC), (136, 168, FUNC)]}),
    
    ("Here we examined how animals behaviorally respond to a switch in reward on an auditory task.",
     {"entities": []}),
    
    ("To examine how animals responded to a change in reward contingency, we trained 20 rats on an auditory recognition go/no-go task.",
     {"entities": []}),
    
    ("Previous studies in rodents and primates indicate that locus coeruleus is activated during behavioral conditioning and particularly sensitive to switches of reward",
     {"entities": [(55, 70, LABEL), (91, 114, FUNC), (145, 163, FUNC)]}),
    
    ("Central a2-adrenoceptors and the pontine lateral parabrachial nucleus (LPBN) are involved in the control of sodium and water intake.",
     {"entities": [(0, 24, PHYS), (33, 69, LABEL), (71, 75, LABEL), (108, 131, FUNC)]}),
    
    ("Noradrenaline is an important neurotransmitter involved in the essential control of body fluid balance.",
     {"entities": [(0, 13, NT), (84, 102, FUNC)]}),
    
    ("In the hindbrain, important inhibitory mechanisms for the control of water and NaCl intake have been demonstrated in the lateral parabrachial nucleus (LPBN) (14-20)",
     {"entities": [(7, 16, LABEL), (58, 90, FUNC), (121, 149, LABEL), (151, 155, LABEL)]}),
    
    ("The LPBN is reciprocally connected to forebrain areas implicated in the maintenance of blood pressure and body fluid homeostasis, such as the paraventricular nucleus of the hypothalamus, the central nucleus of the amygdala, and the median preoptic nucleus.",
     {"entities": [(4, 8, LABEL), (38, 47, LABEL), (72, 101, FUNC), (106, 128, FUNC), (142, 185, LABEL), (191, 222, LABEL), (232, 255, LABEL)]}),
    
    ("The LPBN is also richly interconnected with medullary regions, which include the area postrema (AP) and the medial portion of the nucleus of the solitary tract (mNTS)",
     {"entities": [(4, 8, LABEL), (44, 61, LABEL), (81, 94, LABEL), (96, 98, LABEL), (108, 159, LABEL), (161, 165, LABEL)]}),
    
    ("Therefore, the LPBN may integrate and relay taste and visceral signals that ascend from the AP/mNTS to the forebrain areas involved in the control of fluid and electrolyte balance",
     {"entities": [(15, 19, LABEL), (24, 70, FUNC), (92, 94, LABEL), (95, 99, LABEL), (107, 116, LABEL), (151, 179, FUNC)]}),
    
    ("These results suggested that serotonergic mechanisms in the LPBN play an important inhibitory role in modulation of sodium appetite.",
     {"entities": [(29, 41, NT), (60, 64, LABEL), (102, 131, FUNC)]}),
    
    ("Contrary to a2-adrenoceptors located in the forebrain, the activation of a2-adrenoceptors in the LPBN increases sodium and water intake and reduces renal excretion, without changing arterial pressure (2,38,39).",
     {"entities": [(12, 28, PHYS), (44, 53, LABEL), (73, 89, PHYS), (97, 101, LABEL), (102, 135, FUNC), (148, 163, FUNC), (182, 199, FUNC)]}),
    
    ("Respiratory depression is primarily mediated by mu-opioid receptors 6,7, which are widely expressed throughout the brainstem respiratory network",
     {"entities": [(0, 22, FUNC), (48, 67, PHYS), (115, 144, LABEL)]}),
    
    ("We sought to determine whether there is a subregion of the PBN where mu-opioid receptor agonists depress respiratory rate.",
     {"entities": [(59, 62, LABEL), (69, 96, PHYS), (97, 121, FUNC)]}),
    
    ("In four adult animals, the tPBN was functionally identified and then marked by injection of a fluorescent tracer (700nl, 5% Red Retrobeads, Lumafluor Inc, USA).",
     {"entities": [(27, 31, LABEL)]}),
    
    ("To determine the contribution of the tPBN to systemic opioid-induced respiratory depression we injected naloxone into the tPBN during continuous IV infusion of the potent mu-agonist remifentanil.",
     {"entities": [(37, 41, LABEL), (54, 60, PHYS), (69, 91, FUNC), (104, 112, PHYS), (122, 126, LABEL), (171, 194, PHYS)]}),
    
    ("This experimental protocol allowed us to estimate the contributions of the tPBN versus non-tPBN areas to inspiratory and expiratory phase duration",
     {"entities": [(75, 79, LABEL), (87, 95, LABEL), (121, 146, FUNC)]}),
    
    ("The tPBN injections also did not affect the LC: Numerous enkephalin receptors on LC dendrites37 and the involvement of the LC in multiple regulatory functions including arousal and nociception54 make the LC a theoretical target",
     {"entities": [(4, 8, LABEL), (44, 46, LABEL), (57, 77, PHYS), (81, 83, LABEL), (123, 125, LABEL), (169, 176, FUNC), (181, 192, FUNC)]}),
    
    ("We evaluated the contributions of the hindbrain parabrachial nucleus (PBN) to systemic Ex4-induced hypophagia,",
     {"entities": [(48, 68, LABEL), (70, 73, LABEL), (87, 90, PHYS), (99, 109, FUNC)]}),
    
    ("Recently, we reported that direct PBN microinjections of Ex4 and the GLP-1R antagonist exendin-(9-39) (Ex9) respectively suppressed and increased food intake",
     {"entities": [(34, 37, LABEL), (57, 60, PHYS), (69, 75, PHYS), (87, 94, PHYS), (103, 106, PHYS), (136, 157, FUNC)]}),
    
    ("Systemic and local opioid administration in the tPBN also depressed respiratory drive.",
     {"entities": [(19, 25, PHYS), (48, 52, LABEL), (68, 85, FUNC)]}),
    
    ("Time to administer: 12 min",
     {"entities": []}),
    
    ("Time to administer: 5 min",
     {"entities": []}),
    
    ("Time to administer: 20 min",
     {"entities": []}),
    
    ("Time to administer: 25 min",
     {"entities": []}),
    
    ("Political attitudes vary with physiological traits",
     {"entities": []}),
    
    ("The divergence between analyses lies below 0.1 percent, suggesting that the divergence between analyses is minor and the k-means clustering yielded stable results in our dataset.",
     {"entities": []}),
    
    ("Post-processing of non-noise ICs in GIFT consisted of despiking, detrending (linear, cubic and quadratic), regression of the Friston 24 motion parameters and a low pass filter (0.15 Hz).",
     {"entities": []}),
    
    ("regions of interest using a high-model order group independent component analysis (ICA) implemented with the group ICA of fMRI toolbox (GIFT) toolbox (http://mialab.mrn.org/software/gift/) using the infomax algorithm",
     {"entities": []}),
    
    ("Brain networks and static connectivity.",
     {"entities": []}),
    
    ("Target letters were presented for 10 ms against a dark gray background, and participants were instructed to respond as quickly and accurately as possible.",
     {"entities": []}),
    
    ("The distracting images were presented for a variable duration and elicited participants’ eye gaze to shift away from the cued target location, resulting in poorer performance on the task, which was to identify by button press whether a white target letter was an ‘E’ or an ‘F’.",
     {"entities": []}),
    
    ("attention allocation toward task irrelevant, yet intrinsically relevant, information (e.g. erotic distractors)",
     {"entities": []}),
    
    ("Timing of behavioral experiment. A trial starts with a fixation cross. The fixation cross is followed by an arrow indicating the location of the next target letter ‘E’ or ‘F’ presented 5.9° of visual angle left or right from the center.",
     {"entities": []}),
    
    ("Behavioral and eyetracking data. Mean reaction times, percent errors, gaze distance and standard deviation of the gaze distance (s.d.). Asterisks (*) indicate a significant difference at P < 0.05.",
     {"entities": []}),
    
    ("The current fMRI study adopted a modified PIF paradigm to investigate whether and how people spread inequality to uninvolved strangers.",
     {"entities": []}),
    
    ("We thus tested the ability of CeA neurons to concurrently control cervical-mandibular muscles.",
     {"entities": [(30, 33, LABEL), (66, 93, FUNC)]}),
    
    ("Enhanced predatory efficiency upon CeA stimulation was mirrored by analyses of electromyogram recordings.",
     {"entities": [(0, 29, FUNC), (35, 38, LABEL)]}),
    
    ("Optogenetic activation of CeA led mice to pursue, bite, and restrain moving artificial prey independently of internal state",
     {"entities": [(26, 29, LABEL), (42, 48, FUNC), (50, 54, FUNC), (60, 91, FUNC)]}),
    
    ("We investigated in greater depth the reticular circuitry mediating CeA control over craniofacial musculatures.",
     {"entities": [(37, 46, LABEL), (67, 70, LABEL), (84, 109, FUNC)]}),
    
    ("Based on the above, we reasoned that both optical and tonic depolarization of PCRt VGat-neurons should attenuate the potential for mice to successfully hunt insect prey.",
     {"entities": [(78, 82, LABEL), (83, 87, PHYS), (152, 168, FUNC)]}),
    
    ("The periaqueductal gray matter (PAG) is a major CeA target previously implicated in predatory attacks",
     {"entities": [(4, 30, LABEL), (32, 35, LABEL), (48, 51, LABEL), (84, 101, FUNC)]}),
    
    ("To assess the functional relevance of these CeA=>PAG projections, VGat-ires-Cre mice were transfected with non-Cre-dependent ChR2",
     {"entities": [(44, 47, LABEL), (49, 52, LABEL), (66, 70, PHYS)]}),
    
    ("In other words we predicted that this treatment would mimic the effects of activating PAG VGlut2-neurons during prey pursuit",
     {"entities": [(86, 89, LABEL), (90, 94, PHYS), (112, 124, FUNC)]}),
    
    ("From the series of studies above we inferred that different CeA downstream targets mediate craniofacial control vs. prey pursuit.",
     {"entities": [(60, 63, LABEL), (91, 111, FUNC), (116, 128, FUNC)]}),
    
    ("One area of the brain in which AVP likely exerts profound behavioral effects is the amygdala.",
     {"entities": [(31, 34, PHYS), (58, 76, FUNC), (84, 99, LABEL)]}),
    
    ("Thus, LA involvement in the processing of CS-US association changes over the course of the formation and the long-term maintenance of this information.",
     {"entities": [(6, 8, LABEL), (28, 59, FUNC)]}),
    
    ("The CeA functions as an integrative hub that converts emotionally-relevant sensory information about the external and internal environment into behavioral and physiological responses.",
     {"entities": [(4, 7, LABEL), (45, 94, FUNC), (159, 182, FUNC)]}),
##TRAINED TO HERE
    ("Opioid agonists are most often used in the management of sickle cell pain, especially in adults.",
     {"entities": [(0, 15, PHYS), (43, 73, FUNC)]}),
    
    ("Two donors in the PLDRH required conversion to an open due to bleeding and large graft size (Open conversion rate :  6.",
     {"entities": []}),
    
    ("Our analysis was based on  7 8 consecutive cases of living liver donor, who underwent right hepatectomy, of which  4 3 underwent ODRH and  3 5 PLDRH.",
     {"entities": []}),
    
    ("Conclusions: Robotic approach do not decrease complications in elderly population.",
     {"entities": []}),
    #
    ("Namely, two new classes of M 1-selective PAMs have been developed.",
     {"entities": [(27, 30, PHYS), (41, 45, PHYS)]}),
     
    ("Testing of novel muscarinic allosteric modulators in animal models of human diseases has shown their good efficacy.",
      {"entities": [(18, 50, PHYS), (71, 85, FUNC)]}),
     
    ("M 1 receptors play a critical role in cognitive processes [ 7].",
      {"entities": [(0, 3, PHYS), (38, 57, FUNC)]}),
    
    ("Thus, positive allosteric modulation of M 1 receptors appears to be the way to treat cognitive deficits in Alzheimer’s disease or schizophrenia [ 8 3].",
     {"entities": [(6, 36, PHYS), (41, 53, PHYS), (85, 103, FUNC), (107, 126, FUNC), (131, 143, FUNC)]}),
   
    ("Thus, selective positive modulation of M 4 receptors may provide a novel treatment strategy of psychotic symptoms in schizophrenia that are considered to result from dopaminergic hyperactivity [ 8 3].",
     {"entities": [(39, 52, PHYS), (95, 131, FUNC), (166, 178, NT)]}),
    
    ("Huntington’s disease results from increased transmission at glutamatergic corticostriatal synapses that may be attenuated by the cholinergic system.",
     {"entities": [(0, 20, FUNC), (60, 73, NT), (74, 89, LABEL), (129, 140, NT)]}),
    
    ("The M 5-selective NAM of acetylcholine ML 3 7 5 (Figure  9) [ 8 8] has effectively prevented cocaine self-administration and the development of addiction in rats [ 8 9].",
     {"entities": [(4, 7, PHYS), (25, 38, NT), (94, 120, FUNC), (129, 153, FUNC)]}),
    
    ("You arrange for home health to come and check on him daily for a few weeks.",
     {"entities": []}),

    ("Two days following discharge, Mr. Jones presents at the emergency department (ED) with SOB and hypoxia.",
     {"entities": []}),
    
    ("He asks about treatment and palliation options.",
     {"entities": []}),
    
    ("Maybe you could just tell him the best case scenario and really stress to him that the medications will help? ",
     {"entities": []}),
    
    ("Cytokines have been suggested to play a role in the pathogenesis of depressive disorders, as they suppress the negative feedback mechanism of the hypothalamic-pituitary-adrenal axis by causing desensitization of glucocorticoid receptors.",
     {"entities": [(0, 9, PHYS), (68, 88, FUNC), (146, 181, LABEL)]}),
    
    ("Although these approaches seem very promising, implementing the CRISPR/Cas9 system for BCR editing remains challenging in many regards (Table 1).",
     {"entities": [(64, 75, PHYS), (87, 98, FUNC)]}),
    
    ("On the one hand, some limitations are due to the CRISPR/Cas9 technology itself, such as low cutting and recombination efficiencies, potent cell cycle disruption and off-target mutations to meet clinical criteria.",
     {"entities": [(49, 60, PHYS), (139, 160, FUNC), (165, 185, FUNC)]}),
    
    ("Mature B cells initially express mostly IgM and IgD immunoglobulins, through an alternative splicing mechanism of the constant exons.",
     {"entities": [(7, 14, PHYS), (40, 43, PHYS), (48, 67, PHYS), (80, 110, FUNC)]}),
    
    ("One of the most promising concepts is the editing of the endogenous BCR with the CRISPR/Cas9 system in order to modify its specificity.",
     {"entities": [(42, 71, FUNC), (81, 92, PHYS)]}),
    
    ("NF-κB acts on many immune cells, and its constitutive activation leads to an increase inflammation in inflammatory and autoimmune diseases, such as MS (Yan and Greer, 2008).",
     {"entities": [(0, 5, PHYS), (77, 98, FUNC), (102, 138, FUNC)]}),
    
    ("Many studies have reported the activation of NF-κB in the brain tissue of MS patients (Gveric et al.,",
     {"entities": [(45, 50, PHYS), (58, 70, LABEL)]}),
    
    ("Approximately 20% of genome-wide MS susceptibility variants fall within and/or proximal to NF-κB signaling genes, including NFKB1 or p105/p50 and TNFRSF1A (TNFR1), which cause decreased expression of the negative regulators of NF-κB (De Jager et al.,",
     {"entities": [(91, 96, PHYS), (124, 129, PHYS), (133, 137, PHYS), (138, 141, PHYS), (146, 154, PHYS), (156, 161, PHYS), (176, 232, FUNC), (234, 242, PER)]}),
    
    ("In this way, thanks to MR, we may use the information provided by genotyping to address the question whether changes in the level of expression of the gene of interest represent causal influences on the disease, in the hope that this will then point to biological pathways of pathogenic relevance.",
     {"entities": [(124, 143, FUNC), (151, 167, PHYS)]}),
    
    ("p38a signaling in astrocytes critically regulates specific subsets of cytokines (TNFα, IL-6) and chemokines (CXCL1, CXCL2, CXCL10, CCL2, CCL4).",
     {"entities": [(0, 4, PHYS), (40, 79, FUNC), (81, 85, PHYS), (87, 91, PHYS), (97, 107, PHYS), (109, 114, PHYS), (116, 121, PHYS), (123, 129, PHYS), (131, 135, PHYS), (137, 141, PHYS)]}),
    
    ("The result is that without the astroglial barrier an elevated number of macrophages/microglia in the CNS contributes to an increase in the upregulation of chemokines and cytokines leading to an uncontrolled inflammation.",
     {"entities": [(72, 83, PHYS), (84, 93, PHYS), (101, 104, LABEL), (139, 179, FUNC), (194, 219, FUNC)]}),
    
    ("Xk,Zj, for each of the k = 5 genes, has been sampled from a normal multivariable distribution with means equal to the vector of the 5 i-e associations β^Xk,Zj and covariance matrix equal to the covariance matrix between gene expressions in that specific tissue.",
     {"entities": []}),
    
    ("X,Zj has been sampled from a normal distribution with mean equal to β^X,Zj and standard deviation equal to se(β^X,Zj).",
     {"entities": []}),
    
    ("In the last column the IVW estimate and its 95% confidence intervals obtained via bootstrap are also reported.",
     {"entities": []}),
    
    ("According to this criterion CCL2 gene in MEDU and NFKB1 gene in CRBL turned out statically significant.",
     {"entities": [(28, 32, PHYS), (50, 55, PHYS), (64, 68, PHYS)]}),
    
    ("NFKB1 variants were found to be associated in GWASs with MS, and, in particular, two variants were found to increase gene expression (Housley et al.,",
     {"entities": [(0, 5, PHYS), (108, 132, FUNC), (134, 141, PER)]}),
    
    ("mice knockout for the inhibitor of p50, IκBα, are characterized by the constitutive activation of NF-κB in microglia/macrophages during EAE, developing an exacerbated EAE disease course with enhanced inflammatory infiltration and demyelination in the CNS",
     {"entities": [(22, 38, FUNC), (40, 44, PHYS), (98, 103, PHYS), (107, 116, PHYS), (117, 128, PHYS), (200, 225, FUNC), (230, 243, FUNC), (251, 254, LABEL)]}),
    
    ("If astrocytes-mediated response leads to increased abnormal levels of p50, or elevated levels of CCL2, then a dysregulated immune response could start.",
     {"entities": [(3, 31, PHYS), (60, 73, FUNC), (87, 101, FUNC), (123, 138, FUNC)]}),
    
    ("We preliminarily explored whether ghrelin could provide useful guidance for the early diagnosis and treatment of DTMs.",
     {"entities": [(34, 41, PHYS), (100, 117, FUNC)]}),
    
    ("showed that ghrelin was lower in tumors than in adjacent normal tissue, and ghrelin levels were negatively correlated with the degree of differentiation.",
     {"entities": [(12, 19, PHYS), (76, 83, PHYS)]}),
    
    ("Therefore, it is possible that there is no difference in serum ghrelin levels between cancer patients and the healthy population.",
     {"entities": [(63, 70, PHYS)]}),
    
    ("The activities of both histone methyltransferases (HMT) and DNA methyltransferases (DNMT) depend on intracellular SAM levels, which vary according to the nutrient availability of serine and methionine.",
     {"entities": [(23, 49, PHYS), (51, 54, PHYS), (60, 82, PHYS), (84, 88, PHYS), (114, 117, PHYS), (179, 185, PHYS), (190, 200, PHYS)]}),
    
    ("The mitochondrial protein VDAC1, is a key regulator of metabolic and energy homeostasis that contributes to the metabolic phenotype of cancer cells [38].",
     {"entities": [(26, 31, PHYS), (55, 87, FUNC)]}),
    
    ("Furthermore, recently we demonstrated that VDAC1 oligomers mediate the release of mitochondrial DNA fragments [43].",
     {"entities": [(43, 48, PHYS), (71, 109, FUNC)]}),
    
    ("The importance of VDAC1 in cell energy and metabolism homeostasis is reflected in its over-expression in many cancers [44,45].",
     {"entities": [(18, 23, PHYS), (27, 65, FUNC), ]}),
    
    ("In addition, HDAC1 and HDAC2 activities were shown to be regulated by post-translation modifications (PTMs) [94].",
     {"entities": [(13, 18, PHYS), (23, 28, PHYS), (70, 100, FUNC)]}),
    
    ("Demonstration of these changes upon VDAC1 depletion requires further investigation using complicated studies.",
     {"entities": [(36, 41, PHYS)]}),
    
    ("To investigate the protective effects of pemafibrate against NASH, we used the STAM mouse model (induced NASH in male C57BL/6J strain)18.",
     {"entities": []}),
    
    ("First, we examined the morphological conversion accompanying EMT.",
     {"entities": [(61, 64, FUNC)]}),
    
    ("Compared to the total number of genes which are deregulated during EMT, the BMP signature genes account for only a small fraction of gene expression changes.",
     {"entities": [(67, 70, FUNC), (76, 79, PHYS)]}),
    
    ("Glutamate is a nonessential amino acid neurotransmitter responsible for most excitatory synaptic transmission in the central nervous system.",
     {"entities": [(0, 9, NT), (77, 109, FUNC), (117, 139, LABEL)]}),
    
    ("Repeated high doses of methamphetamine (10 mg/kg x 4, every 2 hours) decrease GLT-1 in striatum and hippocampus (Althobaiti et al.,",
     {"entities": [(78, 82, PHYS), (87, 95, LABEL), (100, 111, LABEL), (113, 123, PER)]}),
    
    ("There is also clinical evidence for alcohol-dependent EAAT2 regulation.",
     {"entities": [(54, 59, PHYS)]}),
    
    ("In hippocampus and cerebellum, synapses are less likely to be bounded by astrocytic processes, perhaps magnifying the importance of neuronal EAATs.",
     {"entities": [(3, 14, LABEL), (19, 29, LABEL), (141, 146, PHYS)]}),
    
    ("MMP-9 inhibition blocks behavioral sensitization to ethanol and associated brain changes in ΔFosB in PFC and NAc",
     {"entities": [(0, 5, PHYS), (24, 48, FUNC), (92, 97, PHYS), (101, 104, LABEL),  (109, 112, LABEL)]}),
    
    ("These results are in line with NAC acting more as a relapse prevention medication rather than cocaine cessation treatment.",
     {"entities": [(31, 34, PHYS), (94, 121, FUNC)]}),
    
    ("There are 3 clinical trials for NAC with cannabis dependence and 6 for nicotine use or dependence.",
     {"entities": [(32, 35, PHYS), (41, 60, FUNC), (71, 97, FUNC)]}),
    
    ("We explored the impact of attenuating H3Q5dop accumulation in the VTA on drug-induced transcriptional programs that may be responsible for cocaine seeking",
     {"entities": [(38, 45, PHYS), (66, 69, LABEL), (73, 110, FUNC), (139, 154, FUNC)]}),
    
    ("Nicotine was recently shown to activate neurons in the hindbrain that synthesize GLP-1.",
     {"entities": [(0, 8, PHYS), (29, 47, FUNC), (55, 64, LABEL), (70, 86, FUNC)]}),
    
    ("Cholinergic neurons in the mHb co-release glutamate, are the major source of excitatory transmission in the IPn, and have a key role in controlling nicotine intake.",
     {"entities": [(0, 11, NT), (27, 30, LABEL), (42, 51, NT), (108, 111, LABEL), (136, 163, FUNC)]}),
    
    ("TCF7L2 immunofluorescence colocalized with tdTomato-positive and tdTomato-negative cells in the mHb (Fig. 1d), which suggests that TCF7L2 is expressed by both cholinergic and non-cholinergic cells.",
     {"entities": [(0, 6, PHYS), (96, 99, LABEL), (131, 137, PHYS), (159, 170, NT)]}),
    
    ("Robust activity of galactosidase was detected in the mHb of BAT-GAL mice, in which expression of galactosidase is controlled by TCF7L2",
     {"entities": [(19, 32, PHYS), (53, 56, LABEL), (83, 110, FUNC), (128, 134, PHYS)]}),
    
    ("Hence, TCF7L2 is robustly expressed and functionally active in habenular cholinergic neurons that regulate nicotine intake",
     {"entities": [(7, 13, PHYS), (63, 72, LABEL), (73, 84, NT), (107, 122, FUNC)]}),
    
    ("Next, we investigated the role of TCF7L2 in regulating the motivational properties of nicotine.",
     {"entities": [(34, 40, PHYS), (59, 94, FUNC)]}),
    
    ("Next, we used the CRISPR-Cas9 system to investigate the role of TCF7L2 in the mHb in regulating nicotine intake.",
     {"entities": [(64, 70, PHYS), (78, 81, LABEL), (96, 111, FUNC)]}),
    
    ("Hence, nicotine is unlikely to stimulate excitatory transmission in the IPn by a mechanism that involves TCF7L2 activation.",
     {"entities": [(7, 15, PHYS), (31, 64, FUNC), (72, 75, LABEL), (105, 111, PHYS)]}),
 
    ("We focused on EB3 and SRC because they have been shown to mediate microtubule-actin cross talk necessary for structural synaptic plasticity in other brain regions",
     {"entities": [(14, 17, PHYS), (22, 25, PHYS), (66, 94, FUNC), (149, 162, LABEL)]}),
    
    ("The localization of α6β2∗ nAChRs on dopaminergic neurons suggests they may play a significant role in nicotine reward and contribute to nicotine-mediated neuroprotection against PD (Quik and Wonnacott, 2011).",
     {"entities": [(20, 25, PHYS), (26, 33, PHYS), (36, 48, PHYS), (102, 117, FUNC), (136, 169, FUNC)]}),
    
    ("It also improves cognition and attention (Newhouse et al.,",
     {"entities": [(17, 26, FUNC), (31, 40, FUNC), (42, 50, PER)]}),
    
    ("β2-containing (β2∗) nAChRs are among the most nicotine-sensitive subtypes in the brain, responding to agonist concentrations in the 0.",
     {"entities": [(0, 13, PHYS), (15, 17, PHYS), (46, 64, FUNC), (81, 86, LABEL), (102, 109, PHYS)]}),
    
    ("α6β2∗ nAChRs are selectively expressed in dopaminergic neurons of the bed nucleus of the stria terminalis (BNST) and substantia nigra pars compacta (SNc) as well as neurons in the retina, superior colliculus (Champtiaux et al.,",
     {"entities": [(0, 5, PHYS), (42, 54, NT), (70, 105, LABEL), (107, 111, LABEL), (117, 147, LABEL), (149, 152, LABEL), (180, 186, LABEL), (187, 207, LABEL), (209, 219, PER)]}),
    
    ("Next, we sought to examine the strains’ pain responses following morphine administration using a modified murine paradigm for OIH [14].",
     {"entities": [(65, 88, FUNC), (126, 129, FUNC)]}),
    
    ("Strains exhibit divergent morphine-dependent analgesic and allodynic/hyperalgesic profiles with corresponding changes in MOR-1K gene expression.",
     {"entities": [(45, 68, FUNC), (121, 127, PHYS)]}),
    
    ("A timeline of chronic morphine administration and the assessments of pain behavior and gene expression are shown.",
     {"entities": [(22, 30, PHYS), (69, 82, FUNC)]}),
    
    ("Interestingly, MOR-1K gene expression levels for both 129S6 and CXB7/ByJ mice returned to near-baseline levels following the cessation of morphine treatment on day 5, suggesting that the observed differences were indeed morphine-dependent.",
     {"entities": [(15, 21, PHYS)]}),
    
    ("The observed correlation between strain-specific pain profiles and MOR-1K gene expression levels suggests that MOR-1K contributes to OIH in genetically susceptible mice.",
     {"entities": [(67, 73, PHYS), (111, 117, PHYS), (133, 136, FUNC)]}),
    
    ("Within the OIH murine paradigm, we found that sustained i.t.",
     {"entities": [(11, 14, FUNC)]}),
    
    ("Taken together all these results suggest that the resolution of opioid-induced hyperalgesia is not due to a rapid extinction of pronociceptive systems, but is rather due to a counter-adaptation by inhibitory systems dependent on endogenous opioid release.",
     {"entities": [(64, 70, PHYS), (79, 91, FUNC), (128, 150, FUNC), (229, 246, NT)]}),
    
    ("First, it seems that opioid-induced pronociceptive activity may persist long after cessation of opioid administration.",
     {"entities": [(21, 27, PHYS), (36, 49, FUNC), (96, 102, PHYS)]}),
    
    ("Actually, these data support the critical role of microglia not only in opioid-induced hyperalgesia and tolerance but also in long-term pain sensitization observed after brief exposure to opioid.",
     {"entities": [(50, 59, PHYS), (72, 78, PHYS), (87, 99, FUNC), (104, 113, FUNC), (136, 154, FUNC), (188, 194, PHYS)]}),
    
    ("These adaptive modifications range from the receptors modulation and uncoupling with G protein to the hyper-activation of the cAMP-pathway, and so of the AC, with consequent increase of the proteins CREB (cAMP response element-binding protein) and fos.",
     {"entities": [(85, 94, PHYS), (126, 138, PHYS), (174, 198, FUNC), (199, 203, PHYS), (205, 242, PHYS), (248, 251, PHYS)]}),
    
    ("Low COMT activity also increases opioid receptors and enhances opioid analgesia and adverse effects in some cancer [198, 199].",
     {"entities": [(0, 8, PHYS), (23, 49, PHYS), (54, 79, FUNC), (84, 99, FUNC)]}),
    
    ("On the contrary, the SVM model can be over-fitted to the data and thus loose generalizability.",
     {"entities": []}),
    
    ("At the neurotransmitter level, decades of research have supported the role of the opioid system in the neurobiology of placebo analgesic effects.",
     {"entities": [(82, 88, PHYS), (127, 144, PHYS)]}),
    
    ("Muscimol provides an efficient, reversible inactivation effect and was chosen based on the results of previous studies70–73.",
     {"entities": [(0, 8, PHYS), (43, 62, FUNC)]}),
    
    ("Because the expression of inducible transcription factor proteins peaks at approximately 1 hour after stimulus induction and fades by 3–4 hours31, rats were perfused 1 h after the last behavioral test.",
     {"entities": [(26, 56, PHYS)]}),
    
    ("This hypothesis is based the spinal cord and brainstem pain-signaling neurons project via the parabrachial and solitary nuclei to densely innervate the hypothalamus.",
     {"entities": [(29, 40, LABEL), (45, 54, LABEL), (55, 69, FUNC), (94, 106, LABEL), (111, 119, LABEL), (130, 147, FUNC), (152, 164, LABEL)]}),
    
    ("Data were acquired from a commercial database (Celera Discovery System, CDS) were used to select SNPs spaced at 2–5 kb intervals throughout each gene region plus 4–6 kb upstream and 4–6 kb downstream of each gene.",
     {"entities": []}),
    
    ("In order to illustrate the method, however, we show the results for the galanin-2 receptor.",
     {"entities": [(72, 90, PHYS)]}),
    
    ("Morphine can bind to μ (mu) opioid receptor (MOR), δ (delta) opioid receptor (DOR) and κ (kappa) opioid receptor (KOR).",
     {"entities": [(0, 8, PHYS), (21, 43, PHYS), (45, 48, PHYS), (51, 76, PHYS), (78, 81, PHYS), (87, 112, PHYS), (114, 117, PHYS)]}),
    
    ("The multiple action sites of morphine in the brain decrease the effectiveness of morphine due to development of tolerance, physical dependence, and addiction.",
     {"entities": [(29, 37, PHYS), (45, 50, LABEL), (81, 89, PHYS), (112, 121, FUNC), (123, 142, FUNC), (148, 157, FUNC)]}),
    
    ("Expression of MOR is also reported in the habenula—interpeduncular nucleus (IPN) pathway; suggesting the potential role of MOR in mediating the positive and negative effect of opioids, which needs to be further investigated (Gardon et al.,",
     {"entities": [(14, 17, PHYS), (42, 50, LABEL), (51, 74, LABEL), (76, 79, LABEL), (123, 126, PHYS), (144, 172, FUNC), (176, 183, PHYS), (225, 231, PER)]}),
    
    ("Although the distribution of the oprm1 gene and protein in the whole tissue has been demonstrated in larval zebrafish (Bretaud et al.,",
     {"entities": [(33, 38, PHYS), (119, 126, PER)]}),
    
    ("Next, to identify brain regions sensitive to morphine, we examined the effect of acute (20-min) morphine exposure on oprm1, cfos and npas4a gene expression in the brain by in situ hybridization and real-time PCR.",
     {"entities": [(45, 53, PHYS), (96, 104, PHYS), (117, 122, PHYS), (124, 128, PHYS), (133, 139, PHYS), (163, 168, LABEL)]}),
    
    ("Some cells expressing mmp9 were also found in the medulla oblongata.",
     {"entities": [(22, 26, PHYS), (50, 67, LABEL)]}),
    
    ("Expression of Slc17a7 gene in the brain of zebrafish.",
     {"entities": [(14, 21, PHYS), (34, 52, LABEL)]}),
    
    ("Number of npas4 mRNA expressing cells in control and morphine-treated fish.",
     {"entities": [(10, 20, PHYS), (53, 61, PHYS)]}),
    
    ("These studies suggest the distribution of DOR in the telencephalon is well-conserved across vertebrate species, which could be a center for reward (Charbogne et al.,",
     {"entities": [(42, 45, PHYS), (53, 66, LABEL)]}),
    
    ("On the other hand, in situ hybridization is a sensitive method that allows detail anatomical localization, but the analysis of signal intensity is semi-quantitative.",
     {"entities": []}),
    
    ("In the habenula, oxycodone induced downregulation of oprm1 and npas4a expression.",
     {"entities": [(7, 15, LABEL), (17, 26, PHYS), (35, 49, FUNC), (53, 48, PHYS), (63, 69, PHYS)]}),
    
    ("Although there are no reports on the regulation of CXCR3 in the parabrachial nucleus of rodents, a reduced neuronal activity was reported in the previous study (Hashimoto et al.,",
     {"entities": [(51, 56, PHYS), (64, 84, LABEL), (99, 124, FUNC)]}),
    
    ("The animal study was reviewed and approved by Animal Ethics Committee of Monash University (ethics approval number: MARP/2017/049).",
     {"entities": []}),
    
    ("Following hybridization, the sections were washed and blocked with 2% normal sheep serum.",
     {"entities": []}),
    
    ("To standardize sections with different background intensity, all the section were changed to gray mode using adobe illustrator software CS5.",
     {"entities": []}),
    
    ("However, the sample size in this study is comparable to that in the previous study on neuronal activity quantification in zebrafish (Lau et al.,",
     {"entities": [(133, 136, PER)]}),
    
    ("While for the semi-quantitative analysis of oprm1 and npas4a mRNA, staining density was subjectively scored on a five-point scale as follows + + + (high), + + (moderate), + (low), and – (absent).",
     {"entities": [(44, 49, PHYS), (54, 65, PHYS)]}),
    
    ("Photomicrographs showing expression of oprm1 genes in sagittal (A,B) and coronal sections (C–H) of zebrafish brain.",
     {"entities": [(39, 44, PHYS), (99, 114, LABEL)]}),
    
    ("The effect of morphine on the oprd1 gene expression was further morphologically assessed via in situ hybridization (ISH).",
     {"entities": [(14, 22, PHYS), (30, 35, PHYS) ]}),
    
    ("In short, unbiased sampling was applied such that each location along the tissue section axis had an equal probability of being included in the sample and all locations in the plane of section (excluding the set guard zones)",
     {"entities": []}),
    
    ("The design-based stereological approach that was used in this study to estimate total number of biological particles (terminal axon boutons) included the application of the 3-D optical fractionator probe applied within a known volume of a defined region of interest (ROI; each nuclei).",
     {"entities": []}),
    
    ("All brain slices of one batch per animal were processed simultaneously under the same conditions.",
     {"entities": []}),
    
    ("The protocol was adapted from previous publications [35], [36].",
     {"entities": []}),
    
    ("Animals were placed, facing the wall, at 1 of 4 start locations (north, south, east or west) and allowed to swim to the visible platform for a maximum of 60 seconds.",
     {"entities": []}),
    
    ("The number of stained cells in 6 sections was counted bilaterally, and, as every 12th section was used, this number was multiplied by 12.",
     {"entities": []}),
    
    ("To determine cell survival and proliferation, cells were plated in triplicate in multiple sets of 12-well culture plates.",
     {"entities": []}),
    
    ("Cell proliferation was quantified by electronically counting cell numbers (Z2, Beckman Coulter, Villepinte, France).",
     {"entities": []}),
    
    ("The result was not statistically significant (p > .05)",
     {"entities": []}),
    
    ("One-Way ANOVA revealed F(2,32)=1.203, p > .05",
     {"entities": []}),
    
    ("There was a large effect of stimulation of the nucleus of darkschewitz (p < .01, **)",
     {"entities": [(47, 70, LABEL)]}),
    
    ("Logistic regression analysis showed no difference between the two lines (p=.2384)",
     {"entities": []}),
    
    ("In the object recognition test, animals of both groups detected novelty, with longer exploration durations of the novel object vs the familiar ones (vehicle: t11 = −2.",
     {"entities": []}),
    
    ("For details of procedures, please refer to Material and Methods S1.",
     {"entities": []}),
    
    ("05, ## p<.05",
     {"entities": []}),
    
    ("Accordingly, blood flow measurements with PET have been used to investigate color discrimination tasks in rhesus monkeys [36].",
     {"entities": []}),
    
    ("Custom-made chromatoscope consisting of the following parts: (a) an optical construction with a connection site for an optical fibre and a white colored reflector shield, (b) a tripod for precise and reproducible positioning above the animal eyes, (c) a filter holder with groove to insert Wratten Kodak filters, Blue (i) and Yellow (ii) as well as an impermeable film for monocular stimulation, (d) a 150 W light source, which produces luminosity with a color temperature of about 3200 K and 20 lumens/watt, (e) an optical fibre, which is guiding the light to the connector at the optical construction (a).",
     {"entities": []}),
    
    ("However, using the uncorrected data and increasing the threshold cluster size in SPM (showing only areas where at least 10 or 20 adjacent voxels are active) did not change the significant results shown in Fig 8 indicating that the observed activations are real.",
     {"entities": []}),
    
    ("Very recently, real-time imaging of brain activity under visual stimulation in freely moving rats using functional ultrasound has been performed [49].",
     {"entities": []}),
    
    ("However, its adaptability and application for our present study design using a steady stimulation may not be feasible.",
     {"entities": []}),
    
    ("Furthermore, in the evolutional trend genetic changes refined the downstream neural circuitry that more efficiently extract color from other sensory information over many generations.",
     {"entities": []}),
    
    ("Table C: Original data (Standardized Uptake Values).",
     {"entities": []}),
    
    ("Five minutes later, isoflurane application was completely switched off.",
     {"entities": []}),
    
    ("No further processing filter was needed because the minor artifacts of the imaging system were small in comparison with the recorded field potential.",
     {"entities": []}),
    
    ("8 mm, FOV 37 mm × 37 mm, matrix 256 × 256, RARE factor 8, and number of averages four.",
     {"entities": []}),
###TRAINED TO HERE
    ("Genetic ablation and optogenetics revealed that the DP/DTT→DMH pathway drives thermogenic, hyperthermic, and cardiovascular sympathetic responses to psychosocial stress without contributing to basal homeostasis.",
     {"entities": [(52, 54, LABEL), (55, 58, LABEL), (59, 62, LABEL), (71, 89, FUNC), (91, 103, FUNC), (109, 145, FUNC), (149, 168, FUNC)]}),
    
    ("AAAS is a partner of HINARI, AGORA, OARE, CHORUS, CLOCKSS, CrossRef and COUNTER.",
     {"entities": []}),
    
    ("Although the corticolimbic circuits that process stress and emotions are undetermined, the PVT and MD thalamic nuclei, which provide stress inputs to the DP/DTT, constitute a fear stress circuit involving the amygdala (30, 31).",
     {"entities": [(13, 35, LABEL), (41, 68, FUNC), (91, 94, LABEL), (99, 117, LABEL), (125, 146, FUNC), (154, 156, LABEL), (157, 160, LABEL), (175, 186, FUNC), (209, 217, LABEL)]}),
    
    ("In panic disorder, glutamatergic inputs to the DMH to develop the panic-prone state (32) may be provided from the DP/DTT.",
     {"entities": [(19, 32, NT), (47, 50, LABEL), (66, 83, FUNC), (114, 116, LABEL), (117, 120, LABEL)]}),
    
    ("Imagine you are standing in your office and all of a sudden a man walks in and attacks you with a knife.",
     {"entities": []}),
    
    ("Police officers are trained to deal with acute threat and to inhibit their automatic action tendencies in order to optimize adequate response capacity.",
     {"entities": []}),
    
    ("When a stimulus or a situation is perceived to be threatening, the brain activates many neuronal circuits to adapt to the demand, the most well-known being the autonomic nervous system (ANS).",
     {"entities": [(67, 72, LABEL), (73, 105, FUNC), (160, 184, LABEL), (186, 189, LABEL)]}),
    
    ("Before addressing these questions, I first describe the phenomenology of freezing and fight-or-flight reactions as well as the psychophysiological and neural mechanisms associated with these threat-related defensive states.",
     {"entities": []}),
    
    ("Freezing, a state of parasympathetic dominance.",
     {"entities": []}),
    
    ("For instance, negatively valenced and highly arousing pictures elicit sympathetic changes such as galvanic skin responses [9] and pupil dilation [76].",
     {"entities": []}),
    
    ("In a visual discrimination, paradigm subjects had to indicate whether the target was tilted to the left or to the right with respect to the upright position.",
     {"entities": []}),
    
    ("After a variable time interval, the target pulled a phone or a gun (cue), upon which the participant had to respond as fast as possible by shooting (go) or withholding (no-go), respectively.",
     {"entities": []}),
    
    ("Finally, building on animal models, research in human developmental and clinical samples has provided starting points for investigating the role of freezing in the development of psychopathology.",
     {"entities": []}),
    
    ("Step-down reaction periods and error times were higher, and step-down latency was lower, in the model, NC, and NRSF shRNA groups than in the normal group at all time points (all P < 0.003",
     {"entities": []}),
    
    ("Note: NC, negative control; NRSF, neuron-restrictive silencer factor; d, day; *P < 0.05",
     {"entities": []}),
    
    ("A laser Doppler flow meter (PeriFlux 5000, Perimed, Stockholm, Sweden) was used to measure regional CBF in the cortex.",
     {"entities": []}),
    
    ("After anesthesia was administered (chloral hydrate 350 mg/kg), a midline incision was made on the neck.",
     {"entities": []}),
    
    ("Subsequently, a portion of the tissue was removed and stored at −80°C for use in quantitative real-time polymerase chain reaction (qRT-PCR) and western blotting.",
     {"entities": []}),
    
    ("Sections were then incubated with diaminobenzidine (DBA) for 1~2 mins, rinsed again 3 times with PBS (2 mins/rinse), re-dyed for 1 min with hematoxylin, dehydrated, mounted, and sealed.",
     {"entities": []}),
    
    ("Apoptotic cells were quantified in rat brain tissues according to the instructions of the DeadEndTM fluorescence labeling TUNEL detection kit (Promega Corp., Madison, WI, USA).",
     {"entities": []}),
    
    ("In all cases, rats were experimentally naive at the start of experiments, and were habituated to housing conditions and experimenter handling for ⩾1 week before the start of experimental manipulations.",
     {"entities": []}),
    
    ("The time that rats spent in the two compartments was recorded as the pre-conditioning baseline, and rats were assigned supersac solution in one compartment and water solution in the other compartment.",
     {"entities": []}),
    
    ("Elevated plus-maze (Experiment 3): The elevated plus-maze (EPM) test was used to test anxiety-like behavior in conditions previously described.",
     {"entities": []}),
    
    ("These lighting conditions produce % open arm times of 15–20% in our lab, consistent with the literature for EPM results observed in genetically heterogeneous rats (in results reported below, mean % open arm time is approximately equal to 14%).",
     {"entities": []}),
    
    ("Samples of protein (15 μg) were subjected to SDS-polyacrylamide gel electrophoresis on 10% acrylamide gels by using a Tris/Glycine/SDS buffer system (Bio-Rad), followed by electrophoretic transfer to polyvinylidene difluoride membranes (GE Healthcare, Piscataway, NJ, USA).",
     {"entities": []}),
    
    ("Rats (n=48) were trained to self-administer 10% w/v ethanol versus water in a two-lever operant situation during 30-min self-administration sessions, as described above, for a period of 18 days.",
     {"entities": []}),
    
    ("Four days following the EPM test, rats were allowed to explore an apparatus with three chambers that differ in the visual (wall pattern) and tactile (floor composition) cues.",
     {"entities": []}),
    
    ("Injection of KOP receptor agonists stimulates the release of CRF and glucocorticoids",
     {"entities": [(13, 25, PHYS), (35, 64, FUNC), (69, 84, FUNC)]}),
    
    ("Lipopolysaccharide (LPS), rotenone, dimethyl sulfoxide (DMSO), and ATP were purchased from Sigma-Aldrich (St. Louis, MO, USA).",
     {"entities": []}),
    
    ("SPSS Rel 15 (SPSS Inc., Chicago, IL, USA) was used to conduct all the statistical analyses.",
     {"entities": []}),
    
    ("0 (Media Cybernetics, Silver Spring, MD, USA).",
     {"entities": []}),
    
    ("Initially, the start area was connected to the goal area via a doorway and underpass.",
     {"entities": []}),
    
    ("On T2, the doorway was blocked and the goal area was only accessible through the underpass (underpass task).",
     {"entities": []}),
    
    ("On trial 1 (T1), the reward-paired chamber was accessible through the doorway and underpass.",
     {"entities": []}),
    
    ("To enter the orgy, the mice would have to dig through this bedding (dig task).",
     {"entities": []}),
    
    ("To characterize functional connections from the AON to the pPC, we obtained whole-cell recordings from neurons in the pyramidal cell layer.",
     {"entities": [(48, 51, LABEL), (59, 62, LABEL), (118, 138, LABEL)]}),
    
    ("These data indicate that although AON axons reach the pPC, their projection density as well as their connection probability is much lower than for the aPC.",
     {"entities": [(34, 37, LABEL), (54, 57, LABEL), (151, 154, LABEL)]}),
    
    ("Enhanced TH activity could elucidate the increase observed in dopamine levels within several brain areas.",
     {"entities": [(9, 11, PHYS), (62, 70, NT), (85, 104, LABEL)]}),
    
    ("Therefore, since tryptophan hydroxylase is the enzyme responsible for the synthesis of serotonin, a TPH immunohistochemistry was carried out in the hypothalamic area to clarify the SQE mechanism that induced an elevation in the serotonin levels.",
     {"entities": [(17, 39, PHYS), (74, 96, FUNC), (100, 103, PHYS), (148, 165, LABEL), (211, 244, FUNC)]}),
    
    ("Their ligands include low molecular weight hormones such as GH-RH, but mainly polypeptide hormones such as glucagon, calcitonin, and secretin.",
     {"entities": [(60, 65, PHYS), (78, 98, PHYS), (107, 115, PHYS), (117, 127, PHYS), (133, 141, PHYS)]}),
    
    ("Regarding its receptors, there is an age-dependent increase in protein and mRNA levels of group II mGlu receptor proteins (mGluR2 and mGluR3).",
     {"entities": [(14, 23, PHYS), (51, 86, FUNC), (90, 121, PHYS), (123, 129, PHYS), (134, 139, PHYS)]}),
    
    ("Oxytocin (OT) receptors are present in the CNS, with oxytocinergic neurons presenting widespread projections and modulating synaptic transmission and network activity in the hippocampus (Arsenijevic et al., 1995; Mairesse et al., 2015).",
     {"entities": [(0, 8, PHYS), (10, 12, PHYS), (43, 46, LABEL), (53, 66, NT), (113, 145, FUNC), (150, 166, FUNC), (174, 185, LABEL), (187, 198, PER), (207, 211, "DATE")]}),
    
    ("Age-related reduction in OT binding was reported in the caudate putamen, the olfactory tubercle, and the ventromedial hypothalamic nucleus of 20-month old rats.",
     {"entities": [(25, 27, NT), (56, 71, LABEL), (77, 95, LABEL), (105, 138, LABEL)]}),
    
    ("In the (4) substantia nigra, dopamine D2, opioid κ and cannabinoid CB1 receptors are also depleted with age, while angiotensin AT1 receptor levels are increased.",
     {"entities": [(11, 27, LABEL), (29, 40, PHYS), (42, 48, PHYS), (56, 81, PHYS), (91, 108, FUNC), (116, 140, PHYS)]}),
    
    ("3 cells/section), OT (1. 0 ",
     {"entities": []}),
    
    ("3 cells/section) (Fig. 7b,e), APC (3. 1 ± 1.",
     {"entities": []}),
    
    ("4 cells/section) (Fig. 7e, upper left panel), orbitofrontal cortex (2. 0 ",
     {"entities": [(46, 66, LABEL)]}),
    
    ("2 cells/section) (Fig. 7e, upper middle panel), medial prefrontal cortex (0.",
     {"entities": [(48, 72, LABEL)]}),
    
    ("All PD(s)/PI(s) must have an eRA Commons account. ",
     {"entities": []})
]
