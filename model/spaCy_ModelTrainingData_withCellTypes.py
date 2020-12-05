#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:02:03 2020

@author: smith
"""
LABEL = "REGION"
CIT = "CITATION"
NT = "NEUROTRANSMITTER"
PHYS = "PHYSIO"
FUNC = "FUNCTION"
CELL = "CELLTYPE"


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
     {"entities": [(19, 22, LABEL), (23, 41, FUNC), (74, 92, FUNC)]}),
    
    ("After learning, the reward memory is stored in the PFC and NAcc",
     {"entities": [(51, 54, LABEL), (59, 63, LABEL), (20, 43, FUNC)]}),
    
    ("Peters et al",
     {"entities": [(0, 12, CIT)]}),

    ("Enhancing activity in PL increases fear and drug-seeking",
     {"entities": [(22, 24, LABEL), (25, 39, FUNC), (44, 56, FUNC)]},
     ),
       
    ("The neural circuit that underlies this approach behavior has been widely studied and involves the VTA and NAcc",
     {"entities": [(98, 101, LABEL), (106, 110, LABEL), (39, 56, FUNC)]},
     ),
  
    ("while activity in IL decreases fears and drug-seeking",
     {"entities": [(18, 20, LABEL), (21, 36, FUNC), (41, 53, FUNC)]}),

    ("In a series of experiments in the 1950s, Olds and Milner (1954) found that rats will press a lever to self-stimulate the VTA to NAcc pathway at an even faster rate than to obtain food.",
     {"entities": [(121, 124, LABEL), (128, 132, LABEL), (41, 63, CIT)]}),
 
    ("there is also evidence that OFC signals aversive stimuli",
     {"entities": [(28, 32, LABEL), (32, 56, FUNC)]}),
    
    ("Taken together, these findings suggest both IL/PL and OFC coordinate the interaction between threat- and reward-related stimuli",
     {"entities": [(44, 46, LABEL), (47, 49, LABEL), (54, 57, LABEL), (73, 127, FUNC)]}),
    
    ("function of PFC is involved, but via divergent projections to the NAcc rather than to the amygdala",
     {"entities": [(12, 15, LABEL), (66, 70, LABEL), (90, 96, LABEL)]}),
    
    ("The ARC has important implications in the control of glucose homeostasis, including the regulation of food intake and energy balance",
     {"entities": [(4, 7, LABEL), (42, 72, FUNC), (88, 132, FUNC)]}),
    
    ("Activation of AgRP and NPY neurons have been reported to promote anabolic processes that lead to a markedly increase of food intake",
     {"entities": [(14, 18, NT), (23, 26, NT), (27, 34, CELL), (57, 83, FUNC), (108, 131, FUNC)]}),
        
    ("On the contrary, activation of POMC neurons favours catabolic processes, reducing appetite and food intake, whereas their inhibition increases feeding (Shin et al. 2017)",
     {"entities": [(31, 35, NT), (36, 43, CELL), (52, 71, FUNC), (73, 106, FUNC), (133, 150, FUNC), (152, 168, CIT)]}),
    
    ("Recently, a new population of neurons in the ARC have been discovered",
     {"entities": [(30, 37, CELL), (45, 48, LABEL)]}),

    ("Finally, the ARC also possesses glucosensing neurons (Wang et al. 2004; Spanswick et al. 1997",
     {"entities": [(13, 16, LABEL), (54, 70, CIT), (72, 93, CIT), (32, 44, PHYS), (45, 52, CELL)]}),
    
    ("Stimulation of projections to the lateral hypothalamus (AgRP→LHN projections) promotes feeding (Steculorum et al. 2016)",
     {"entities": [(34, 54, LABEL), (56, 60, LABEL), (61, 65, LABEL), (96, 118, CIT), (78, 94, FUNC)]}),

    ("while activation of the projections to the anterior bed nucleus of the stria terminalis (AgRP→aBNST6vl projections) mediate the activation of BAT-Mstn expression",
     {"entities": [(43, 87, LABEL), (89, 93, LABEL), (94, 102, LABEL), (116, 138, FUNC), (142, 151, PHYS)]}),
    
    ("In fact, a recent study has reported that an increase of NPY from the ARC decreases the sympathetic outflow that controls",
     {"entities": [(57, 60, NT), (70, 73, LABEL), (74, 107, FUNC)]}),
    
    ("The VMH is a key brain region involved in glucose regulation and energy homeostasis in mammals (Chowdhury et al. 2017).",
     {"entities": [(4, 7, LABEL), (96, 117, CIT), (42, 60, FUNC), (65, 83, FUNC)]}),
    
    ("In particular, the VMH has a crucial role in detecting hypoglycemic events and initiating the physiological counterregulatory signaling",
     {"entities": [(19, 22, LABEL), (45, 74, FUNC), (79, 135, FUNC)]}),
   #### 
    ("A subset of VMH neurons expresses the leptin receptor (Elmquist et al. 1998).",
     {"entities": [(12, 15, LABEL), (38, 44, NT), (45, 53, PHYS), (55, 75, CIT)]}),
    
    ("SF1 neurons in the VMH are required for maintenance of normal glucose and energy metabolism.",
     {"entities": [(0, 3, NT), (19, 22, LABEL), (40, 69, FUNC), (74, 91, FUNC)]}),
    
    ("Leptin is a hormone predominantly made in adipose cells that helps to regulate energy balance by i) inhibiting hunger, ii) stimulating glucose uptake.",
     {"entities": [(0, 6, NT), (42, 55, CELL), (79, 93, FUNC), (100, 117, FUNC), (123, 149, FUNC)]}),

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
     {"entities": [(81, 90, NT), (114, 117, LABEL), (119, 135, CIT)]}),
    
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
     {"entities": [(109, 112, LABEL), (117, 120, LABEL), (151, 165, CIT), (69, 88, FUNC)]}),
    
    ("The SCN is a small region of the hypothalamus, situated directly above the optic chiasm.",
     {"entities": [(4, 7, LABEL), (33, 45, LABEL), (75, 87, LABEL)]}),
    
    ("As previously mentioned, it is well known for regulating many different body functions in a 24-h cycle (circadian rhythms).",
     {"entities": [(46, 102, FUNC), (104, 121, FUNC)]}),
    
    ("In addition, studies of electrical stimulation of the SCN have also induced hyperglycemia, which was prevented by the use of sympathetic blockers or denervation (Yi et al. 2010).",
     {"entities": [(54, 57, LABEL), (162, 176, CIT), (68, 89, FUNC), (125, 145, PHYS)]}),
    
    ("This suggests a sympathetic mediation of the effects due to SCN activation.",
     {"entities": [(60, 63, LABEL), (16, 37, FUNC)]}),
    
    ("The integration of information related to the body’s energy homeostasis does not occur solely in the hypothalamus. For example, meal-related satiety information is conveyed to the nucleus of the tractus solitarius (NTS) in the medulla.",
     {"entities": [(101, 113, LABEL), (180, 213, LABEL), (227, 234, LABEL), (53, 71, FUNC)]}),
###TESTED TO HERE    
    ("Some NTS neurones are glucose sensitive, while others express POMC, leptin receptors or the MC4R.",
     {"entities": [(5, 8, LABEL), (9, 17, CELL), (22, 29, PHYS), (62, 66, NT), (68, 84, PHYS), (92, 96, PHYS)]}),
    
    ("The NTS also sends a dense projection to the LHN, reinforcening its contribution in the control of body energy (Williams et al. 2001)",
     {"entities": [(4, 7, LABEL), (45, 48, LABEL), (112, 132, CIT), (88, 110, FUNC), ]}),
    
    ("Notably, we demonstrated that RAB39B is an abundant protein in dopaminergic neurons in the SNpc, the neuronal subtype selectively lost in PD.",
     {"entities": [(30, 36, PHYS), (63, 83, CELL), (91, 95, LABEL)]}),
    
    ("MC4R is localized in the thalamus, hypothalamus, and hippocampus among other brain and peripheral sites [20, 21].",
     {"entities": [(0, 4, PHYS), (25, 33, LABEL), (35, 47, LABEL), (53, 64, LABEL)]}),
    
    ("SIM1 homozygous knockout mice fail to properly form at least the paraventricular (PVH), supraoptic (SON), and anterior periventricular (aPV) hypothalamic nuclei and die perinatally [24].",
     {"entities": [(0, 4, PHYS), (65, 80, LABEL), (82, 85, LABEL), (88, 98, LABEL), (100, 103, LABEL), (110, 134, LABEL), (136, 139, LABEL)]}),
   
    ("We next explored the contribution of BRS3 in SIM1-expressing neurons, which are predominantly in the paraventricular nucleus of the hypothalamus (PVH).",
     {"entities": [(37, 41, PHYS), (45, 49, PHYS), (61, 68, CELL), (101, 144, LABEL)]}),
    
    ("BRS3 deletion in SIM1-expressing neurons impaired insulin tolerance and increased insulin levels.",
     {"entities": [(0, 4, PHYS), (17, 21, PHYS), (33, 40, CELL), (41, 67, PHYS), (72, 96, FUNC)]}),
    
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
     {"entities": [(52, 56, LABEL), (80, 85, LABEL), (87, 112, CIT)]}),
    
    ("Right, Confocal image of virally labeled mCbN axons in the vlPAG.",
     {"entities": [(41, 45, LABEL), (59, 64, LABEL)]}),
    
    ("Example injection site of CTb-GFP in the vlPAG.",
     {"entities": [(41, 46, LABEL)]}),
    
    ("Low magnification image of mCbN labeled axons in vlPAG.",
     {"entities": [(27, 31, LABEL), (49, 54, LABEL)]}),
    
    ("Even the vlPAG, however, is heterogeneous, as pharmacological activation of the vlPAG elicits freezing, bradycardia, and anti-nociception (Bandler et al., 2000).",
     {"entities": [(9, 14, LABEL), (80, 85, LABEL), (139, 159, CIT), (94, 137, FUNC)]}),
    
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
     {"entities": [(4, 7, LABEL), (35, 39, NT), (40, 47, CELL), (68, 77, LABEL), (82, 91, LABEL), (102, 116, FUNC), (142, 145, LABEL), (147, 164, LABEL), (166, 169, LABEL), (176, 196, LABEL), (198, 200, LABEL)]}),
    
    ("Similar to an antidepressive effect, rewarding potency of DRN 5-HT neurons has been studied by using several lines of genetically-modified mice.",
     {"entities": [(14, 35, FUNC), (58, 61, LABEL), (62, 66, NT), (67, 74, CELL)]}),
    
    ("We examined the rewarding potency of optogenetic manipulation of DRN 5-HT neurons using an adeno-associated virus (AAV) expressing optogenetic actuators",
     {"entities": [(65, 68, LABEL), (69, 73, NT), (74, 81, CELL)]}),
    
    ("We found that the optogenetic activation of DRN 5-HT neurons and 5-HT projections from the DRN to VTA strongly reinforced nose-poke self-stimulation behavior and induced conditioned place preference.",
     {"entities": [(44, 47, LABEL), (48, 52, NT), (53, 60, CELL), (65, 69, NT), (91, 94, LABEL), (98, 101, LABEL), (111, 157, FUNC), (170, 198, FUNC)]}),
    
    ("Optogenetic Activation of 5-HT Neuron Terminals in the VTA is Responsible for Reinforcement of Nose-Poke Behavior but not in the LH, CeA, NAc, or Ventral Pallidum (VP).",
     {"entities": [(26, 30, NT), (31, 37, CELL), (55, 58, LABEL), (78, 113, FUNC), (129, 131, LABEL), (133, 136, LABEL), (138, 141, LABEL), (146, 162, LABEL), (164, 166, LABEL)]}),
    
    ("In this study, we examined the involvement of the VTA, LH, NAc, CeA, and VP.",
     {"entities": [(50, 53, LABEL), (55, 57, LABEL), (59, 62, LABEL), (64, 67, LABEL), (73, 75, LABEL)]}),
    
    ("In summary, our data provide direct evidence that selective stimulation of DRN 5-HT neurons projecting to the VTA was sufficient for reinforcing effect and conditioned place preference.",
     {"entities": [(75, 78, LABEL), (79, 83, NT), (84, 91, CELL), (110, 113, LABEL), (133, 151, FUNC), (156, 184, FUNC)]}),

    ("Adiponectin (ADPN) is a plasma protein that belongs to the complement 1q family and it is secreted by adipose tissue [1,2].",
     {"entities": []}),
   
    ("However, ADPN was found to modulate glucose metabolism in hippocampal neurons, increasing glucose uptake, glycolysis, and ATP production rates [27].",
     {"entities": [(27, 54, FUNC), (58, 69, LABEL), (70, 77, CELL)]}),
   
    ("In both humans and laboratory animals, kappa opioid receptor (KOR) activation produces depressive and anxiety-like effects.",
     {"entities": [(39, 51, NT), (87, 122, FUNC)]}),
   
    ("The brain stem contains the midbrain, pons, and medulla in the caudal fossa.",
     {"entities": [(4, 14, LABEL), (28, 36, LABEL), (38, 42, LABEL), (48, 55, LABEL), (63, 75, LABEL)]}),
   
    ("Therefore, we planned to inject retrograde tracer cholera toxin B subunit (CB) into the CSF-contacting nucleus.",
     {"entities": [(88, 110, LABEL)]}),
    
    ("The generic category of diffuse gliomas (DG) includes two distinct tumor entities: tumors derived from oligodendrocyte precursor cells – OPCs (OligoPDTs) versus those derived from stem cells (SCDTs).",
     {"entities": [(103, 134, CELL), (137, 141, CELL), (180, 190, CELL), (192, 197, CELL)]}),
    
    ("In particular, NPY neurons in the Arc play a critical role in the control of energy homeostasis.",
     {"entities": [(15, 18, NT), (19, 26, CELL), (34, 37, LABEL), (66, 95, FUNC)]}),
    
    ("In addition, NAc dysfunction is associated with many mental disorders,",
     {"entities": [(13, 16, LABEL), (48, 69, FUNC)]}),
    
    ("The median number of whole-brain labeled neurons to the NAc subnuclei was 9,518.",
     {"entities": [(41, 48, CELL), (56, 59, LABEL)]}),
    
    ("The 75 brain regions could be grouped into nine major brain areas, including the isocortex, olfactory areas (OLF), hippocampal formation (HPF), cortical subplate (CTXsp), striatum (STR), pallidum (PAL), and thalamus (TH).",
     {"entities": [(81, 90, LABEL), (92, 107, LABEL), (109, 112, LABEL),  (115, 136, LABEL), (138, 141, LABEL), (144, 161, LABEL), (163, 168, LABEL), (171, 179, LABEL), (181, 184, LABEL), (187, 195, LABEL), (203, 211, LABEL), (213, 215, LABEL)]}),
    
    ("Summary of Distribution of Input Neurons to Subregions of NAcC and NAcS",
     {"entities": [(58, 62, LABEL), (67, 71, LABEL)]}),

    ("The critical cardiovascular features include hypotension and paradoxical sinus bradycardia, heart block, or sinus arrest after sympathetic excitation.",
     {"entities": []}),
    
    ("The neuropeptide oxytocin is mainly produced in the hypothalamic paraventricular (PVN) and supraoptic nuclei (SON), and it is released from magnocellular cells by axonal and somatodendritic release.",
     {"entities": [(17, 25, NT), (52, 64, LABEL), (65, 80, LABEL), (82, 85, LABEL), (91, 108, LABEL), (110, 113, LABEL)]}),
    
    ("The VTA projects primarily to NAcc/PFC and receives input from the lateral hypothalamus that detects the presence of food reward (Schultz, 1998).",
     {"entities": [(4, 7, LABEL), (30, 34, LABEL), (35, 38, LABEL), (67, 87, LABEL), (130, 143, CIT), (93, 128, FUNC)]}),
    
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
     {"entities": []}),
    
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
     {"entities": [(22, 28, CELL)]}),
    
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
     {"entities": [(0, 4, PHYS), (64, 88, LABEL), (90, 110, CIT)]}),
    
    ("Moreover, Margolis et al. (2006) found that KORs inhibit VTA dopamine neurons that project to the mPFC and basolateral amygdala, but not those that project to the NAc.",
     {"entities": [(10, 32, CIT), (44, 48, PHYS), (49, 56, FUNC), (57, 60, LABEL), (61, 69, NT), (70, 77, CELL)]}),
    
    ("Furthermore, the activation of KOR decreases the amplitude of excitatory (Margolis et al., 2005) and inhibitory (Ford et al., 2007) postsynaptic currents into midbrain dopamine neurons.",
     {"entities": [(31, 34, PHYS), (35, 72, FUNC), (74, 95, CIT), (113, 130, CIT), (159, 167, LABEL), (168, 176, NT), (177, 184, CELL)]}),
    
    ("How do KORs modulate dopamine signaling to elaborate motivated behaviors and when does it result in a sensitized compulsive behavior?",
     {"entities": [(7, 11, PHYS), (21, 29, NT)]}),
    
    ("AE and JF wrote the first draft of the manuscript with input from MA.",
     {"entities": []}),
    
    ("The work of the authors cited in this review has been supported by FONDECYT grant numbers: 1110352 and 1150200 to MA; 1141088 to JF; DIPOG grant 391340281 to JF; FONDECYT Postdoctoral fellow 3170497 to JC and 3190843 to AE.",
     {"entities": []}),
  #130  
    ("An earlier onset of OCD symptoms is observed in men compared with women (Mathis et al., 2011), with women showing more prevalence of contamination and cleaning symptoms (Labad et al., 2008).",
     {"entities": [(73, 92, CIT), (170, 188, CIT)]}),
    
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
    
    ("Chapman (2016) reported that somatostatin has a marked antinociceptive function",
     {"entities": [(0, 14, CIT), (22, 34, NT)]}),
    
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
    
    ("Oh et al., found that subcutaneous injection of CCL5 in mice produced allodynia 32.",
     {"entities": [(0, 10, CIT), (41, 45, PHYS), (62, 71, FUNC)]}),
    
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
     {"entities": [(0, 19, CELL), (27, 44, LABEL), (46, 50, LABEL), (63, 66, LABEL), (79, 109, FUNC)]}),
      
    ("The VTA dopaminergic neurons project back to NAcc, where they stimulate cholinergic neurons.",
     {"entities": [(4, 7, LABEL), (8, 28, CELL), (45, 49, LABEL), (72, 91, CELL)]}),
    
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
     {"entities": [(117, 34, CIT)]}),
      
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
     {"entities": [(23, 64, FUNC), (77, 87, LABEL), (89, 114, LABEL), (116, 120, LABEL), (127, 153, LABEL), (155, 175, CIT)]}),
    
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
     {"entities": [(183, 202, CIT)]}),
    
    ("Yet, other factors can impact instrumental devaluation sensitivity, including the amount of reinforcer experience (Adams, 1982)",
     {"entities": [(115, 126, CIT)]}),
    
    ("While we do not observe the emergence of a non-preferred lever approach in GT rats under devalued relative to valued conditions, others have (Morrison et al., 2015).",
     {"entities": [(142, 163, CIT)]}),
    
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
     {"entities": [(42, 45, LABEL), (46, 51, LABEL), (91, 110, CIT), (72, 89, FUNC)]}),
    
    ("This includes OFC/vmPFC activity, which can vary with probability contingencies, effort and the temporal delay between response and outcome (Haber & Knutson, 2010).",
     {"entities": [(14, 17, LABEL), (18, 23, LABEL), (141, 162, CIT), (54, 79, FUNC)]}),
    
    ("Additionally, the region of the ventral striatum where overlapping activation between reward and loss anticipation resided is considered to be part of the NAcc core (Xia et al., 2017).",
     {"entities": [(32, 48, LABEL), (155, 164, LABEL), (166, 182, CIT), (86, 92, FUNC), (97, 114, FUNC)]}),
    
    ("This is the first time for a meta‐analysis to detect amygdala activation during both reward and loss anticipation, as this region is typically associated with loss processing.",
     {"entities": [(53, 61, LABEL), (85, 91, FUNC), (96, 113, FUNC), (159, 174, FUNC)]}),
    
    ("There is a report that self-esteem is associated with hippocampal volume and the cortisol response to a psychosocial stress [30].",
     {"entities": [(54, 65, LABEL), (81, 98, PHYS), (104, 123, FUNC)]}),
    
    ("The cluster size was determined through a Monte Carlo simulation using AFNI’s AlphaSim program (http://afni.nimh.nih.gov/afni/doc/manual/AlphaSim) with 10,000 iterations.",
     {"entities": []}),
    
    ("L. Dorsal MPFC",
     {"entities": [(3 ,14, LABEL)]}),
    
    ("In a follow up study to our identification of risk coding neurons in the OFC we identified an error-related signal in OFC neurons related to risk, namely a risk prediction error (O’Neill and Schultz, 2013).",
     {"entities": [(58, 65, CELL), (73, 76, LABEL), (118, 121, LABEL), (179, 204, CIT), (94, 107, FUNC), (122, 129, CELL), (156, 177, FUNC)]}),
    
    ("A previous work including a food-related task discovered decreased reward sensitivity associated with alterations in the putamen activity after acute stress induction (Born et al., 2010).",
     {"entities": [(121, 128, LABEL), (168, 185, CIT)]}),
    
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
     {"entities": [(33, 58, LABEL), (66, 72, LABEL), (81, 89, LABEL), (113, 120, CELL), (153, 171, FUNC)]}),
    
    ("On the other hand, injections in the amygdala and the medio-lateral septum, which projects directly and indirectly to the PVN, did not alter basal ACTH levels, but reduced stress-induced ACTH (Neumann et al., 2000a).",
     {"entities": [(37, 45, LABEL), (54, 74, LABEL), (122, 125, LABEL), (147, 151, PHYS), (172, 191, FUNC)]}),
    
    ("Demographic characteristics of sample (N = 200), stratified by age, IQ, gender, and ethnicity for the standardization of the EMOTICOM neuropsychological test battery.",
     {"entities": []}),
    
    ("Task 15: Ultimatum Game",
     {"entities": []}),
    
    ("As a summary of the state of the literature to date, a recently published meta-analysis of structural and functional neuroimaging studies in OCD examined data from VBM studies enrolling 928 patients vs. 942 controls, and fMRI studies of inhibitory control enrolling 287 patients and 284 controls (Norman et al., 2016).",
     {"entities": [(297, 316, CIT)]}),
    
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
     {"entities": [(20, 23, PHYS), (63, 67, CELL), (80, 91, LABEL), (93, 108, LABEL), (113, 125, LABEL), (166, 178, CELL), (207, 220, CELL), (229, 240, LABEL)]}),
    
    ("Interestingly, in control, but not in architecture students, reaction times during the first repetition of the target were correlated with activation in multiple brain regions (cuneus, lingual gyrus, inferior parietal lobule, insula, and anterior cingulate cortex).",
     {"entities": [(177, 183, LABEL), (185, 198, LABEL), (200, 224, LABEL), (226, 232, LABEL), (238, 263, LABEL)]}),
    
    ("What we do know is that DA is released within the spinal cord during stepping activity, increases motor output, and modulates sensory transmission.",
     {"entities": [(24, 26, NT), (50, 61, LABEL), (88, 110, FUNC), (116, 146, FUNC)]}),
    
    ("By examining intrinsic and synaptic properties we show that DA acts on several ion channels to increase excitability.",
     {"entities": [(60, 62, NT), (79, 91, PHYS), (95, 116, FUNC)]}),
    
    ("b-wright@northwestern.edu",
     {"entities": []}),
    
    ("The striatum consists of GABAergic projection neurons and various types of interneurons.",
     {"entities": [(4, 12, LABEL), (25, 34, NT), (46, 53, CELL)]}),
    
    ("Our findings suggest that coding of movement by TANs in both regions overlaps to a larger degree than previously assumed, considering the segregation in the cortex-basal ganglia- thalamus-cortex circuits.",
     {"entities": [(48, 52, CELL), (157, 163, LABEL), (164, 177, LABEL), (179, 187, LABEL), (188, 194, LABEL)]}),
    
    ("Yet the differences in response patterns support the notion that the TANs in the dorsal and ventral striatum have distinct functions in associative tasks.",
     {"entities": [(69, 73, CELL), (81, 87, LABEL), (92, 108, LABEL)]}),
    
    ("These recordings demonstrated the existence of grid cells in the entorhinal cortex of this bat species.",
     {"entities": [(65, 82, LABEL)]}),
    
    ("These interactions involve the responsiveness of non-neuronal cells to classical neurotransmitters (e.g., glutamate and monoamines) and hormones (e.g., glucocorticoids), as well as the secretion and responsiveness of neurons and glia to low levels of inflammatory cytokines, such as interleukin IL-1, IL-6, and TNFα,",
     {"entities": [(49, 67, CELL), (71, 98, NT), (106, 115, NT), (120, 130, NT), (136, 144, PHYS), (152, 167, PHYS), (217, 224, CELL), (229, 233, CELL), (251, 273, PHYS), (283, 294, PHYS)]}),
    
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
     {"entities": [(0, 3, LABEL), (4, 11, CELL), (27, 54, LABEL), (88, 91, LABEL), (92, 104, CELL)]}),
    
    ("Lockwood et al. (2016) showed that the subgenual anterior cingulate cortex (sgACC) was associated with reward learning only when individuals acted in a prosocial context, and this region signals a prosocial prediction error.",
     {"entities": [(0, 21, CIT), (39, 74, LABEL), (76, 81, LABEL), (103, 118, FUNC), (187, 223, FUNC)]}),
    
    ("Consistent with the growing focus on the ACC, Apps et al. (2016) presented a model based on vicarious motivation and error processing whereby a specific region of ACC gyrus (ACCg) is involved in costs, benefits and errors during social interactions.",
     {"entities": [(41, 44, LABEL), (46, 63, CIT), (163, 172, LABEL), (174, 178, LABEL), (229, 248, FUNC)]}),
    
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
     {"entities": [(7, 18, LABEL), (20, 25, PHYS), (80, 84, PHYS), (108, 146, PHYS), (152, 191, FUNC), (193, 209, CIT)]}),
    
    ("This is the only observation regarding MMPs in the nucleus accumbens following nicotine exposure; another laboratory has examined these enzymes in the hippocampus and mPFC following nicotine CPP.",
     {"entities": [(39, 43, PHYS), (51, 68, LABEL), (151, 162, LABEL), (167, 171, LABEL)]}),
    
    ("Gelatinase activity was increased in NAcore of cocaine-extinguished compared with yoked-saline control rats, and 15 min of cue-induced reinstatement caused a further increase",
     {"entities": [(0, 19, PHYS), (37, 43, LABEL), (123, 148, FUNC)]}),
    
    ("No increases in MMP activity were measured in the dorsal striatum or accumbens shell after 15 min of cue-induced reinstatement",
     {"entities": [(16, 19, PHYS), (51, 65, LABEL), (69, 84, LABEL), (101, 126, FUNC)]}),
    
    ("Neither the enduring increase in gelatinase activity after extinction nor the increase elicited by 15 min of cue-induced reinstatement were accompanied by a change in NAcore protein content of MMP-2 or MMP-9, or the MMP-2/9 inhibitory protein TIMP-2",
     {"entities": [(33, 52, PHYS), (109, 134, FUNC), (167, 173, LABEL), (193, 198, PHYS), (202, 207, PHYS), (216, 223, PHYS), (243, 249, PHYS)]}),
    
    ("The intensity of cue-induced relapse is correlated with the induction of transient synaptic potentiation (t-SP) at glutamatergic synapses on medium spiny neurons (MSNs) in the nucleus accumbens core (NAcore) and requires spillover of glutamate from prefrontal cortical afferents.",
     {"entities": [(17, 36, FUNC), (115, 128, NT), (176, 198, LABEL), (200, 206, LABEL), (234, 243, NT), (249, 268, LABEL), (141, 161, CELL), (163, 167, CELL)]}),
    
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
     {"entities": [(4, 34, LABEL), (36, 40, LABEL), (45, 54, NT), (67, 75, LABEL), (76, 84, NT), (86, 88, NT), (90, 97, CELL), (148, 164, FUNC)]}),
    
    ("We further found that valence-encoding RMTg neurons preferentially project to the DA-rich VTA versus other targets, and excitotoxic RMTg lesions greatly reduce aversive stimulus-induced inhibitions in VTA neurons",
     {"entities": [(22, 38, FUNC), (39, 43, LABEL), (44, 51, CELL),  (82, 84, NT), (90, 93, LABEL), (120, 131, PHYS), (132, 136, LABEL), (160, 177, FUNC), (201, 204, LABEL)]}),
    
    ("RMTG neurons synapse onto tyrosine hydroxylase (TH) positive neurons in the VTA and substantia nigra, and electrical stimulation of the RMTg dramatically suppresses DA neuron firing",
     {"entities": [(0, 4, LABEL), (5, 12, CELL), (26, 46, PHYS), (48, 68, CELL), (76, 79, LABEL), (84, 100, LABEL), (136, 140, LABEL), (154, 181, FUNC)]}),
    
    ("Recently, Romanov et al. (2017) [368] provided evidence of numerous novel neuronal phenotypes of hypothalamic cells using single cell RNA-Seq and DropSeq technologies,",
     {"entities": [(10, 31, CIT), (74, 82, CELL), (97, 115, CELL)]}),
    
    ("To address the paucity of genetic markers of the RMTg, we evaluated a transcription factor previously identified in the mouse RMTg: FoxP1 (Lahti et al. 2016).",
     {"entities": [(49, 53, LABEL), (126, 130, LABEL), (132, 137, PHYS)]}),
    
    ("In the same surgery, the mice were implanted bilaterally with chronic indwelling optic fibers (50-um core) aimed at the VTA (AP -3.1, ML +1.3, DV ?4.8 from dura, 10° angle).",
     {"entities": [(120, 123, LABEL)]}),
    
    ("With respect to opiate drugs, heroin administration leads to long-term alterations in gene expression in the NAc shell.",
     {"entities": [(16, 28, PHYS), (30, 51, FUNC), (109, 118, LABEL)]}),
    
    ("In addition to structural changes, opiate exposure also results in a change in synapse physiology of neurons in the ventral-tegmental area (Saal et al, 2003), hippocampus (Pu et al, 2002), and NAc (Dong et al, 2007).",
     {"entities": [(35, 51, FUNC), (101, 108, CELL), (116, 138, LABEL), (140, 156, CIT), (159, 170, LABEL), (172, 186, CIT), (193, 196, LABEL), (198, 214, CIT)]}),
    
    ("Recently, we found that re-exposure to heroin-conditioned cues results in acute synaptic depression of pyramidal neurons in the ventral mPFC",
     {"entities": [(39, 62, FUNC), (80, 99, PHYS), (103, 120, CELL), (128, 140, LABEL)]}),
    
    ("A second set of mEC slides was stained for amyloid or the norepinephrine transporter (NET) with 10 min pretreatment in 80% formic acid, followed by 10 min incubation in a 0.3 N sodium hydroxide, 0.9% hydrogen peroxide solution, a block in 10% normal donkey serum with 0.05% Tween-20 and overnight incubation with the 4G8 antibody (1:1000, Convance) or a mouse anti-NET antibody (1:1000, NET05-2; MAb Technologies).",
     {"entities": [(16, 19, LABEL), (43, 50, PHYS), (58, 84, PHYS), (86, 89, PHYS)]}),
    
    ("We extended these findings to investigate additional locus coeruleus-innervated regions affected in Alzheimer's disease.",
     {"entities": [(53, 68, LABEL), (100, 119, FUNC)]}),
    
    ("Locus coeruleus activity and adrenergic receptor signaling in the hippocampus contribute to spatial learning",
     {"entities": [(0, 15, LABEL), (29, 58, PHYS), (66, 77, LABEL), (92, 108, FUNC)]}),
    
    ("DREADDs have been used to selectively activate locus coeruleus neurons and modulate rodent behaviour",
     {"entities": [(0, 7, PHYS), (26, 46, FUNC), (47, 62, LABEL), (63, 70, CELL), (84, 100, FUNC)]}),
    
    ("We next examined the effects of locus coeruleus activation on reversal learning.",
     {"entities": [(32, 47, LABEL), (62, 79, FUNC)]}),
    
    ("Additionally, TgF344-AD rats had reduced locus coeruleus fibre density in the dentate gyrus and norepinephrine levels in the hippocampus.",
     {"entities": [(41, 56, LABEL), (78, 91, LABEL), (96, 110, NT), (125, 136, LABEL)]}),
    
    ("Abnormally low levels of forebrain norepinephrine have been reported in Alzheimer's disease",
     {"entities": [(25, 34, LABEL), (35, 49, NT), (72, 91, FUNC)]}),
    
    ("Notably, spatial reversal learning depends on long term depression within the hippocampus, and locus coeruleus electrical stimulation can induce long term depression in the dentate gyrus",
     {"entities": [(9, 34, FUNC), (46, 66, PHYS), (78, 89, LABEL), (95, 110, LABEL), (145, 165, PHYS), (173, 186, LABEL)]}),
    
    ("One of the most striking features of the locus coeruleus is the widespread efferent network, constituting the sole source of central nervous system noradrenaline, with axonal projections being found in all regions and layers of cortex (Levitt and Moore, 1978).",
     {"entities": [(41, 56, LABEL), (125, 147, LABEL), (148, 161, NT),  (202, 234, LABEL), (236, 258, CIT)]}),
    
    ("Recordings from locus coeruleus have shown that these neurons have both tonic and phasic firing patterns, believed to have differential effects on behavior performance, arousal, and attention",
     {"entities": [(16, 31, LABEL), (54, 61, CELL), (147, 167, FUNC), (169, 176, FUNC), (182, 191, FUNC)]}),
    
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
     {"entities": [(30, 33, LABEL), (34, 41, CELL), (66, 93, FUNC)]}),
    
    ("Enhanced predatory efficiency upon CeA stimulation was mirrored by analyses of electromyogram recordings.",
     {"entities": [(0, 29, FUNC), (35, 38, LABEL)]}),
    
    ("Optogenetic activation of CeA led mice to pursue, bite, and restrain moving artificial prey independently of internal state",
     {"entities": [(26, 29, LABEL), (42, 48, FUNC), (50, 54, FUNC), (60, 91, FUNC)]}),
    
    ("We investigated in greater depth the reticular circuitry mediating CeA control over craniofacial musculatures.",
     {"entities": [(37, 46, LABEL), (67, 70, LABEL), (84, 109, FUNC)]}),
    
    ("Based on the above, we reasoned that both optical and tonic depolarization of PCRt VGat-neurons should attenuate the potential for mice to successfully hunt insect prey.",
     {"entities": [(78, 82, LABEL), (83, 95, CELL), (152, 168, FUNC)]}),
    
    ("The periaqueductal gray matter (PAG) is a major CeA target previously implicated in predatory attacks",
     {"entities": [(4, 30, LABEL), (32, 35, LABEL), (48, 51, LABEL), (84, 101, FUNC)]}),
    
    ("To assess the functional relevance of these CeA=>PAG projections, VGat-ires-Cre mice were transfected with non-Cre-dependent ChR2",
     {"entities": [(44, 47, LABEL), (49, 52, LABEL), (66, 70, PHYS)]}),
    
    ("In other words we predicted that this treatment would mimic the effects of activating PAG VGlut2-neurons during prey pursuit",
     {"entities": [(86, 89, LABEL), (90, 104, CELL), (112, 124, FUNC)]}),
    
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
     {"entities": [(7, 14, CELL), (40, 43, PHYS), (48, 67, PHYS), (80, 110, FUNC)]}),
    
    ("One of the most promising concepts is the editing of the endogenous BCR with the CRISPR/Cas9 system in order to modify its specificity.",
     {"entities": [(42, 71, FUNC), (81, 92, PHYS)]}),
    
    ("NF-κB acts on many immune cells, and its constitutive activation leads to an increase inflammation in inflammatory and autoimmune diseases, such as MS (Yan and Greer, 2008).",
     {"entities": [(0, 5, PHYS), (19, 31, CELL), (77, 98, FUNC), (102, 138, FUNC), (152, 171, CIT)]}),
    
    ("Many studies have reported the activation of NF-κB in the brain tissue of MS patients (Gveric et al.,",
     {"entities": [(45, 50, PHYS), (58, 70, LABEL), (87, 101, CIT)]}),
    
    ("Approximately 20% of genome-wide MS susceptibility variants fall within and/or proximal to NF-κB signaling genes, including NFKB1 or p105/p50 and TNFRSF1A (TNFR1), which cause decreased expression of the negative regulators of NF-κB (De Jager et al., 2018)",
     {"entities": [(91, 96, PHYS), (124, 129, PHYS), (133, 137, PHYS), (138, 141, PHYS), (146, 154, PHYS), (156, 161, PHYS), (176, 232, FUNC), (234, 255, CIT)]}),
    
    ("In this way, thanks to MR, we may use the information provided by genotyping to address the question whether changes in the level of expression of the gene of interest represent causal influences on the disease, in the hope that this will then point to biological pathways of pathogenic relevance.",
     {"entities": [(124, 143, FUNC), (151, 167, PHYS)]}),
    
    ("p38a signaling in astrocytes critically regulates specific subsets of cytokines (TNFα, IL-6) and chemokines (CXCL1, CXCL2, CXCL10, CCL2, CCL4).",
     {"entities": [(0, 4, PHYS), (18, 28, CELL), (40, 79, FUNC), (81, 85, PHYS), (87, 91, PHYS), (97, 107, PHYS), (109, 114, PHYS), (116, 121, PHYS), (123, 129, PHYS), (131, 135, PHYS), (137, 141, PHYS)]}),
    
    ("The result is that without the astroglial barrier an elevated number of macrophages/microglia in the CNS contributes to an increase in the upregulation of chemokines and cytokines leading to an uncontrolled inflammation.",
     {"entities": [(31, 41, CELL), (72, 83, CELL), (84, 93, CELL), (101, 104, LABEL), (139, 179, FUNC), (194, 219, FUNC)]}),
    
    ("Xk,Zj, for each of the k = 5 genes, has been sampled from a normal multivariable distribution with means equal to the vector of the 5 i-e associations β^Xk,Zj and covariance matrix equal to the covariance matrix between gene expressions in that specific tissue.",
     {"entities": []}),
    
    ("X,Zj has been sampled from a normal distribution with mean equal to β^X,Zj and standard deviation equal to se(β^X,Zj).",
     {"entities": []}),
    
    ("In the last column the IVW estimate and its 95% confidence intervals obtained via bootstrap are also reported.",
     {"entities": []}),
    
    ("According to this criterion CCL2 gene in MEDU and NFKB1 gene in CRBL turned out statically significant.",
     {"entities": [(28, 32, PHYS), (50, 55, PHYS), (64, 68, PHYS)]}),
    
    ("NFKB1 variants were found to be associated in GWASs with MS, and, in particular, two variants were found to increase gene expression (Housley et al., 1983)",
     {"entities": [(0, 5, PHYS), (108, 132, FUNC), (134, 1154, CIT)]}),
    
    ("mice knockout for the inhibitor of p50, IκBα, are characterized by the constitutive activation of NF-κB in microglia/macrophages during EAE, developing an exacerbated EAE disease course with enhanced inflammatory infiltration and demyelination in the CNS",
     {"entities": [(22, 38, FUNC), (40, 44, PHYS), (98, 103, PHYS), (107, 116, CELL), (117, 128, CELL), (200, 225, FUNC), (230, 243, FUNC), (251, 254, LABEL)]}),
    
    ("If astrocytes-mediated response leads to increased abnormal levels of p50, or elevated levels of CCL2, then a dysregulated immune response could start.",
     {"entities": [(3, 13, CELL), (60, 73, FUNC), (87, 101, FUNC), (123, 138, FUNC)]}),
    
    ("We preliminarily explored whether ghrelin could provide useful guidance for the early diagnosis and treatment of DTMs.",
     {"entities": [(34, 41, PHYS), (100, 117, FUNC)]}),
    
    ("showed that ghrelin was lower in tumors than in adjacent normal tissue, and ghrelin levels were negatively correlated with the degree of differentiation.",
     {"entities": [(12, 19, PHYS), (76, 83, PHYS)]}),
    
    ("Therefore, it is possible that there is no difference in serum ghrelin levels between cancer patients and the healthy population.",
     {"entities": [(63, 70, PHYS)]}),
    
    ("The activities of both histone methyltransferases (HMT) and DNA methyltransferases (DNMT) depend on intracellular SAM levels, which vary according to the nutrient availability of serine and methionine.",
     {"entities": [(23, 49, PHYS), (51, 54, PHYS), (60, 82, PHYS), (84, 88, PHYS), (114, 117, PHYS), (179, 185, PHYS), (190, 200, PHYS)]}),
    
    ("The mitochondrial protein VDAC1, is a key regulator of metabolic and energy homeostasis that contributes to the metabolic phenotype of cancer cells [38].",
     {"entities": [(26, 31, PHYS), (55, 87, FUNC), (135, 147, CELL)]}),
    
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
    
    ("Repeated high doses of methamphetamine (10 mg/kg x 4, every 2 hours) decrease GLT-1 in striatum and hippocampus (Althobaiti et al., 2012)",
     {"entities": [(78, 82, PHYS), (87, 95, LABEL), (100, 111, LABEL), (113, 136, CIT)]}),
    
    ("There is also clinical evidence for alcohol-dependent EAAT2 regulation.",
     {"entities": [(54, 59, PHYS)]}),
    
    ("In hippocampus and cerebellum, synapses are less likely to be bounded by astrocytic processes, perhaps magnifying the importance of neuronal EAATs.",
     {"entities": [(3, 14, LABEL), (19, 29, LABEL), (141, 146, PHYS)]}),
    
    ("MMP-9 inhibition blocks behavioral sensitization to ethanol and associated brain changes in ΔFosB in PFC and NAc",
     {"entities": [(0, 5, PHYS), (24, 48, FUNC), (92, 97, PHYS), (101, 104, LABEL),  (109, 112, LABEL), (132, 140, CELL), (141, 146, PHYS)]}),
    
    ("These results are in line with NAC acting more as a relapse prevention medication rather than cocaine cessation treatment.",
     {"entities": [(31, 34, PHYS), (94, 121, FUNC)]}),
    
    ("There are 3 clinical trials for NAC with cannabis dependence and 6 for nicotine use or dependence.",
     {"entities": [(32, 35, PHYS), (41, 60, FUNC), (71, 97, FUNC)]}),
    
    ("We explored the impact of attenuating H3Q5dop accumulation in the VTA on drug-induced transcriptional programs that may be responsible for cocaine seeking",
     {"entities": [(38, 45, PHYS), (66, 69, LABEL), (73, 110, FUNC), (139, 154, FUNC)]}),
    
    ("Nicotine was recently shown to activate neurons in the hindbrain that synthesize GLP-1.",
     {"entities": [(0, 8, PHYS), (29, 47, FUNC), (55, 64, LABEL), (70, 86, FUNC)]}),
    
    ("Cholinergic neurons in the mHb co-release glutamate, are the major source of excitatory transmission in the IPn, and have a key role in controlling nicotine intake.",
     {"entities": [(0, 19, CELL), (27, 30, LABEL), (42, 51, NT), (108, 111, LABEL), (136, 163, FUNC)]}),
    
    ("TCF7L2 immunofluorescence colocalized with tdTomato-positive and tdTomato-negative cells in the mHb (Fig. 1d), which suggests that TCF7L2 is expressed by both cholinergic and non-cholinergic cells.",
     {"entities": [(0, 6, PHYS), (65, 88, CELL), (96, 99, LABEL), (131, 137, PHYS), (159, 170, NT), (175, 196, CELL)]}),
    
    ("Robust activity of galactosidase was detected in the mHb of BAT-GAL mice, in which expression of galactosidase is controlled by TCF7L2",
     {"entities": [(19, 32, PHYS), (53, 56, LABEL), (83, 110, FUNC), (128, 134, PHYS)]}),
    
    ("Hence, TCF7L2 is robustly expressed and functionally active in habenular noradrenergic neurons that regulate nicotine intake",
     {"entities": [(7, 13, PHYS), (63, 72, LABEL), (73, 94, CELL), (99, 124, FUNC)]}),
    
    ("Next, we investigated the role of TCF7L2 in regulating the motivational properties of nicotine.",
     {"entities": [(34, 40, PHYS), (44, 94, FUNC)]}),
    
    ("Next, we used the CRISPR-Cas9 system to investigate the role of TCF7L2 in the mHb in regulating nicotine intake.",
     {"entities": [(64, 70, PHYS), (78, 81, LABEL), (85, 111, FUNC)]}),
    
    ("Hence, nicotine is unlikely to stimulate excitatory transmission in the IPn by a mechanism that involves TCF7L2 activation.",
     {"entities": [(7, 15, PHYS), (31, 64, FUNC), (72, 75, LABEL), (105, 111, PHYS)]}),
 
    ("We focused on EB3 and SRC because they have been shown to mediate microtubule-actin cross talk necessary for structural synaptic plasticity in other brain regions",
     {"entities": [(14, 17, PHYS), (22, 25, PHYS), (66, 94, FUNC), (149, 162, LABEL)]}),
    
    ("The localization of α6β2∗ nAChRs on dopaminergic neurons suggests they may play a significant role in nicotine reward and contribute to nicotine-mediated neuroprotection against PD (Quik and Wonnacott, 2011).",
     {"entities": [(20, 25, PHYS), (26, 33, PHYS), (36, 56, CELL), (102, 117, FUNC), (136, 169, FUNC)]}),
    
    ("It also improves cognition and attention (Newhouse et al.,",
     {"entities": [(17, 26, FUNC), (31, 40, FUNC), (42, 58, CIT)]}),
    
    ("β2-containing (β2∗) nAChRs are among the most nicotine-sensitive subtypes in the brain, responding to agonist concentrations in the 0.",
     {"entities": [(0, 13, PHYS), (15, 17, PHYS), (46, 64, FUNC), (81, 86, LABEL), (102, 109, PHYS)]}),
    
    ("α6β2∗ nAChRs are selectively expressed in dopaminergic neurons of the bed nucleus of the stria terminalis (BNST) and substantia nigra pars compacta (SNc) as well as neurons in the retina, superior colliculus (Champtiaux et al.,",
     {"entities": [(0, 5, PHYS), (42, 62, CELL), (70, 105, LABEL), (107, 111, LABEL), (117, 147, LABEL), (149, 152, LABEL), (165, 172, CELL), (180, 186, LABEL), (187, 207, LABEL), (209, 227, CIT)]}),
    
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
     {"entities": [(50, 59, CELL), (72, 78, PHYS), (87, 99, FUNC), (104, 113, FUNC), (136, 154, FUNC), (188, 194, PHYS)]}),
    
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
     {"entities": [(29, 40, LABEL), (45, 54, LABEL), (55, 69, FUNC), (70, 77, CELL), (94, 106, LABEL), (111, 119, LABEL), (130, 147, FUNC), (152, 164, LABEL)]}),
    
    ("Data were acquired from a commercial database (Celera Discovery System, CDS) were used to select SNPs spaced at 2–5 kb intervals throughout each gene region plus 4–6 kb upstream and 4–6 kb downstream of each gene.",
     {"entities": []}),
    
    ("In order to illustrate the method, however, we show the results for the galanin-2 receptor.",
     {"entities": [(72, 90, PHYS)]}),
    
    ("Morphine can bind to μ (mu) opioid receptor (MOR), δ (delta) opioid receptor (DOR) and κ (kappa) opioid receptor (KOR).",
     {"entities": [(0, 8, PHYS), (21, 43, PHYS), (45, 48, PHYS), (51, 76, PHYS), (78, 81, PHYS), (87, 112, PHYS), (114, 117, PHYS)]}),
    
    ("The multiple action sites of morphine in the brain decrease the effectiveness of morphine due to development of tolerance, physical dependence, and addiction.",
     {"entities": [(29, 37, PHYS), (45, 50, LABEL), (81, 89, PHYS), (112, 121, FUNC), (123, 142, FUNC), (148, 157, FUNC)]}),
    
    ("Expression of MOR is also reported in the habenula—interpeduncular nucleus (IPN) pathway; suggesting the potential role of MOR in mediating the positive and negative effect of opioids, which needs to be further investigated (Gardon et al.,",
     {"entities": [(14, 17, PHYS), (42, 50, LABEL), (51, 74, LABEL), (76, 79, LABEL), (123, 126, PHYS), (144, 172, FUNC), (176, 183, PHYS), (225, 239, CIT)]}),
    
    ("Although the distribution of the oprm1 gene and protein in the whole tissue has been demonstrated in larval zebrafish (Bretaud et al.,",
     {"entities": [(33, 38, PHYS), (119, 134, CIT)]}),
    
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
     {"entities": [(86, 94, CELL), (133, 144, CIT)]}),
    
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
     {"entities": [(34, 40, CELL)]}),
    
    ("A laser Doppler flow meter (PeriFlux 5000, Perimed, Stockholm, Sweden) was used to measure regional CBF in the cortex.",
     {"entities": []}),
    
    ("After anesthesia was administered (chloral hydrate 350 mg/kg), a midline incision was made on the neck.",
     {"entities": []}),
    
    ("Subsequently, a portion of the tissue was removed and stored at −80°C for use in quantitative real-time polymerase chain reaction (qRT-PCR) and western blotting.",
     {"entities": []}),
    
    ("Sections were then incubated with diaminobenzidine (DBA) for 1~2 mins, rinsed again 3 times with PBS (2 mins/rinse), re-dyed for 1 min with hematoxylin, dehydrated, mounted, and sealed.",
     {"entities": []}),
    
    ("Apoptotic cells were quantified in rat brain tissues according to the instructions of the DeadEndTM fluorescence labeling TUNEL detection kit (Promega Corp., Madison, WI, USA).",
     {"entities": [(0, 15, CELL)]}),
    
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
     {"entities": [(48, 51, LABEL), (59, 62, LABEL), (103, 110, CELL), (118, 138, LABEL)]}),
    
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
     {"entities": [(0, 8, PHYS), (10, 12, PHYS), (43, 46, LABEL), (53, 74, CELL), (113, 145, FUNC), (150, 166, FUNC), (174, 185, LABEL), (187, 211, CIT)]}),
    
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
     {"entities": []}),
    
    ("The Dbi gene encodes the octadecaneuropeptide protein, and is primarily transcribed and released by ependymocytes.",
     {"entities": [(4, 12, PHYS), (25, 53, PHYS), (100, 113, CELL)]}),
    
    ("The blood-brain-barrier is primarily composed of enthothelial cells, which form tight junctions with astrocytes.",
     {"entities": [(49, 67, CELL), (75, 95, FUNC), (101, 111, CELL)]}),
    
    ("Catecholaminergic neurons release monoamines in the ventral striatum (Wise, 1980).",
     {"entities": [(0, 25, CELL), (26, 44, FUNC), (52, 68, LABEL), (70, 80, CIT)]}),
    
    ("Epithelial cells in the choroid plexus are in direct contact with CSF.",
     {"entities": [(0, 16, CELL), (24, 38, LABEL), (66, 69, PHYS)]}),
    
    ("Under a microscope, the fourth ventricle is composed of three cellular layers: (1) the apical epithelial cells facing the CSF, (2) the underlying supporting connective tissue, and (3) the inner layer of endothelial cells with immediate contact with the blood.",
     {"entities": [(24, 40, LABEL), (94, 110, CELL), (122, 125, PHYS), (203, 219, CELL)]}),
    
    ("In MS, CPE cells showed persisting immune activation with immunostaining for T lymphocytes, and VCAM-1 (Guesser et al., 2010).",
     {"entities": [(3, 5, LABEL), (7, 16, CELL), (35, 52, FUNC), (77, 90, CELL), (96, 102, PHYS), (104, 124, CIT)]}),
    
    ("In addition to research focusing on transduction by primary sensory neurons, recent reports have suggested that epidermal cells, particularly keratinocytes, may be responsible for the transduction of certain stimuli.",
     {"entities": [(36, 48, FUNC), (52, 75, CELL), (112, 127, CELL), (142, 155, CELL), (184, 215, FUNC)]}),
    
    ("Other studies have proposed a role for vascular nociceptors in cold pain, suggesting that cold-induced vasoconstriction may begin this process [43].",
     {"entities": [(39, 59, PHYS), (63, 72, FUNC), (90, 119, FUNC)]}),
    
    ("GTG banding analysis was performed according to the standard protocol in peripheral blood lymphocytes.",
     {"entities": [(73, 101, CELL)]}),
    
    ("The cells responsible for an immune response in the brain are microglia and astrocytes (Akiyama et al., 2000a).",
     {"entities": [(29, 44, FUNC), (52, 57, LABEL), (62, 71, CELL), (76, 86, CELL), (88, 109, CIT)]}),
    
    ("In 1994, Akiyama et al. reviewed the contribution of microglial activation to neuroinflammation in AD.",
     {"entities": [(3, 23, CIT), (53, 63, CELL), (78, 101, FUNC)]}),
    
    ("Microglia from AD patients express major histocompatibility complex class II (MHCII) molecules, cyclooxygenase 2 (COX2), and cytokines/chemokines such as monocyte chemotactic protein 1 (Akiyama et al., 2000b).",
     {"entities": [(0, 9, CELL), (35, 76, PHYS), (78, 83, PHYS), (96, 112, PHYS), (114, 118, PHYS), (125, 134, PHYS), (135, 145, PHYS), (154, 184, PHYS), (186, 207, CIT)]}),
    
    ("Within the context of the central nervous system (CNS), PK11195 binds to glial cells, such as astrocytes and microglia.",
     {"entities": [(26, 48, LABEL), (50, 53, LABEL), (56, 63, PHYS), (73, 84, CELL), (94, 104, CELL), (109, 118, CELL)]}),
    
    ("Oligodendrocytes express high levels of myelin basic protein, and are responsible for myelinating axons.",
     {"entities": [(0, 16, CELL), (40, 60, PHYS), (86, 103, FUNC)]}),
    
    ("Ependymal cells are a type of neuroglia that forms the lining of the ventricles.",
     {"entities": [(0, 15, CELL), (30, 39, CELL), (45, 79, FUNC)]}),
    
    ("vGluT2-expressing neurons are primarily found in the hypothalamus and send glutamatergic projections to the lateral habenula.",
     {"entities": [(0, 25, CELL), (53, 65, LABEL), (75, 88, NT), (108, 124, LABEL)]}),
    
    ("Slc1a2 is the gene that encodes for GLT-1 protein, which is responsible for reuptake of glutamate from the synaptic cleft into astrocytes.",
     {"entities": [(0, 6, PHYS), (36, 49, PHYS), (76, 121, FUNC), (127, 137, CELL)]}),
    
    ("Slc17a7 encodes vGluT1 protein in glutamatergic neurons, which are drivers of excitatory transmission.",
     {"entities": [(0, 7, PHYS), (16, 30, PHYS), (34, 55, CELL), (67, 101, FUNC)]}),
    
    ("C-Jun activation is mediated by MEFC2, and is thus highly associated with inflammatory cascades in immune cells such as leukocytes.",
     {"entities": [(0, 5, PHYS), (32, 37, PHYS), (74, 95, FUNC), (99, 111, CELL), (120, 130, CELL)]}),
    
    ("Histaminergic neurons promote wakefullness, by releasing histamine in the ventrolateral preoptic area.",
     {"entities": [(0, 21, CELL), (22, 42, FUNC), (57, 66, NT), (74, 101, LABEL)]}),
    
    ("Orexinergic neurons drive both arousal and motivation, by signaling through OX2R and OX1R, respectively",
     {"entities": [(0, 19, CELL), (20, 53, FUNC), (76, 80, PHYS), (85, 89, PHYS)]}),
    
    ("In particular, astrocytes stimulated to produce NO showed evidence of inhibited mitochondrial respiration (Brown, 1997).",
     {"entities": [(15, 25, CELL), (48, 50, PHYS), (70, 105, FUNC), (107, 118, CIT)]}),
    
    ("Inhibition of Complex I with rotenone or methyl-4-phenyl-1,2,3,6-tetrahydropyridine (MPTP) induces inflammatory changes both in vitro and in vivo.",
     {"entities": [(0, 23, FUNC), (29, 37, PHYS), (41, 83, PHYS), (85, 89, PHYS), (91, 119, FUNC)]}),
    
    ("A separate study that treated human blood monocytes with total mitochondrial extracts found increased IL-8 expression and secretion (Crouser et al., 2009).",
     {"entities": [(36, 51, CELL), (57, 85, PHYS), (92, 131, FUNC), (133, 153, CIT)]}),
    
    ("These molecules are shown in Table 2 and are reviewed below.",
     {"entities": []}),
    
    ("Here, we discuss relevant data, and propose a role for novel cellular mechanisms in neuropsychiatric disease.",
     {"entities": []}),
    
    ("The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.",
     {"entities": []}),
    
    ("There are two more labels related to AD, that is, Healthy Control (HC) and Mild Cognitive Impairment (MCI)",
     {"entities": []}),
    
    ("Therefore, accurate prediction of disease status (i.e., HC, MCI, or AD) becomes very difficult and important for early treatment of the disease.",
     {"entities": []}),
    
    ("Amount of works (Vemuri et al., 2009; Kohannim et al., 2010; Salas-Gonzalez et al., 1973) have focused on how to utilize this, and they suggest that combining them for prediction is better than using any of them independently.",
     {"entities": [(17, 36, CIT), (38, 59, CIT), (61, 88, CIT)]}),
    
    ("In particular, machine learning community has provided powerful classification tools that are used for prediction",
     {"entities": []}),
    
    ("Among well-established porcine behavioral tests such as the open-field test, lesion scoring, and human approach test, the backtest is recognized as a heritable and repeatable measure and a good indicator for assessing coping style in pigs.",
     {"entities": []}),
    
    ("A recent report estimated backtest-trait heritability to be 0.37–0.56 which is quite high for behavioral traits.",
     {"entities": []}),
    
    ("In addition to heritability, a previous publication reported moderate intra-situational consistency and repeatability of the backtest across four test repetitions19.",
     {"entities": []}),
    
    ("HR and LR pigs clearly showed significant differences in the backtest parameters for latency (p = 0.0002), duration (p < 0.0001) and frequency (p < 0.0001).",
     {"entities": []}),
    
    ("P-values were shown to be significant between HR and LR groups.",
     {"entities": []}),
    
    ('Of note, nicotine injection into the DRN has differential effects on behavior in the social interaction test depending on the dose used.', {'entities': [(58, 77, 'FUNCTION'), (9, 17, 'PHYSIO'), (37, 40, 'REGION')]}),
    ('Injection of morphine or the delta receptor agonist (D-Ala2)-Met-enkephalinamide (DALA) into the caudal LS increases in food intake in satiated rats, but LS administration of the broad spectrum opioid receptor agonist MR-2034 (Johnson and Pasternak, 1983) does not affect intake, as shown in Figure 2 (Stanley et al., 1988).', {'entities': [(107, 131, 'FUNCTION'), (194, 217, 'PHYSIO'), (29, 51, 'PHYSIO'), (227, 248, 'CITATION'), (302, 315, 'CITATION'), (97, 106, 'REGION'), (13, 21, 'PHYSIO'), (218, 225, 'PHYSIO'), (82, 86, 'PHYSIO'), (154, 156, 'REGION')]}),
    ('Age differences in MOR binding density were particularly evident in the thalamus, with six out of nine sub-regions showing higher MOR binding density in juvenile compared to adult rats.', {'entities': [(72, 80, 'REGION'), (19, 22, 'PHYSIO'), (130, 133, 'PHYSIO')]}),
    ('Direct estrogen sensitivity\nSoon after the discovery of a second ER isoform (ERβ) in 1996 (82), the absence of direct estrogen feedback to GnRH neurons was challenged by the observations of ERβ mRNA expression (83, 84), ERβ immunoreactivity (85, 86) and 125I-estrogen-binding sites (83) in rodent GnRH neurons.', {'entities': [(254, 275, 'PHYSIO'), (220, 240, 'PHYSIO'), (139, 151, 'CELLTYPE'), (297, 309, 'CELLTYPE'), (65, 75, 'PHYSIO'), (7, 15, 'PHYSIO'), (118, 126, 'PHYSIO'), (190, 198, 'PHYSIO'), (77, 80, 'PHYSIO')]}),
    ('Conversely, secretion of adipokines and lipokines by adipocytes contributes to metabolism regulation.', {'entities': [(64, 100, 'FUNCTION'), (25, 35, 'PHYSIO'), (53, 63, 'CELLTYPE'), (40, 49, 'PHYSIO')]}),
    ('Interestingly, the HbX subtype, which lies at the border between the MHb and LHb, is more transcriptionally similar to other LHb subtypes than MHb subtypes.', {'entities': [(19, 30, 'PHYSIO'), (69, 72, 'REGION'), (77, 80, 'REGION'), (125, 128, 'REGION'), (143, 146, 'REGION')]}),
    ('An increasing number of reports describe large individual variations in the effects of naltrexone in AUD patients (Kiefer et al., 2008; Spanagel and Kiefer, 2008) and pharmacogenetic studies have revealed that genetic factors contribute to individual differences in the ability of naltrexone to reduce ethanol intake (Monterosso et al., 2001; Rubio et al., 2005; Ray et al., 2010; Roman and Nylander, 2005; Moffett et al., 2007; Barr, 2011).', {'entities': [(295, 316, 'FUNCTION'), (136, 155, 'CITATION'), (381, 399, 'CITATION'), (87, 97, 'PHYSIO'), (281, 291, 'PHYSIO'), (429, 433, 'CITATION')]}),
    ('CRF effects on glutamatergic signaling in CRF1+ and CRF1– CeM neurons\nTo assess differences in the functional responsivity of CRF1+ and CRF1– populations to CRF, we tested the effect of CRF (200 nM; 9–12 min) on mEPSCs (Fig. 6I–N).', {'entities': [(15, 28, 'NEUROTRANSMITTER'), (58, 69, 'CELLTYPE'), (42, 46, 'PHYSIO'), (52, 56, 'PHYSIO'), (126, 130, 'PHYSIO'), (136, 140, 'PHYSIO'), (0, 3, 'PHYSIO'), (157, 160, 'PHYSIO'), (186, 189, 'PHYSIO')]}),
    ('However, selective stimulation of glutamatergic VP neurons at 20 Hz produced robust conditioned place avoidance (Tooley et al., 2018).', {'entities': [(84, 111, 'FUNCTION'), (34, 47, 'NEUROTRANSMITTER'), (51, 58, 'CELLTYPE'), (48, 50, 'REGION')]}),
    ('It is a vasoconstrictor and vasodilator via both endothelium-dependent and -independent mechanisms using NO, prostaglandins, endothelin-1, angiotensin, and hydrogen peroxide [892].Reactive Oxygen SpeciesReactive oxygen species are intracellular signaling mediators (second messengers) that regulate vSMC hypertrophy, proliferation, and migration.', {'entities': [(231, 264, 'FUNCTION'), (156, 173, 'PHYSIO'), (299, 315, 'FUNCTION'), (8, 23, 'FUNCTION'), (109, 123, 'PHYSIO'), (317, 330, 'FUNCTION'), (125, 137, 'PHYSIO'), (28, 39, 'FUNCTION'), (49, 60, 'PHYSIO'), (139, 150, 'PHYSIO'), (336, 345, 'FUNCTION'), (105, 107, 'PHYSIO')]}),
    ('In line with these findings, high, aversive doses of nicotine activate the IPN while lower doses fail to do so22, and enhancing nicotine-induced excitation of MHb neurons by overexpressing β4 subunits of the putative low-affinity nAChRs results in CPA to a dose of nicotine that is neutral in control animals18.', {'entities': [(189, 200, 'PHYSIO'), (145, 155, 'FUNCTION'), (53, 61, 'PHYSIO'), (128, 136, 'PHYSIO'), (265, 273, 'PHYSIO'), (163, 170, 'CELLTYPE'), (230, 236, 'PHYSIO'), (75, 78, 'REGION'), (159, 162, 'REGION'), (248, 251, 'FUNCTION')]}),
    ('Unique Glu-GABA Drives of the NAc\nThe medial prefrontal cortex relays taste information from the primary insular cortex, which constitutes the neuronal basis of food intake and energy homeostasis [20].', {'entities': [(161, 195, 'FUNCTION'), (38, 62, 'REGION'), (63, 87, 'FUNCTION'), (97, 119, 'REGION'), (7, 15, 'NEUROTRANSMITTER'), (30, 33, 'REGION')]}),
    ('Conversely, reducing DAergic transmission by lesioning mesocortical DAergic projection neurons (with 6-OH-DOPA) impairs extinction memory formation (Fernandez Espejo, 2003; Morrow et al., 1999) (see summary in Table 2).', {'entities': [(120, 147, 'FUNCTION'), (76, 94, 'CELLTYPE'), (149, 165, 'CITATION'), (55, 67, 'CELLTYPE'), (101, 110, 'PHYSIO'), (21, 28, 'NEUROTRANSMITTER'), (68, 75, 'NEUROTRANSMITTER')]}),
    ('The VP in turn is poised to inhibit the AcbSh through GABAergic or opioidergic input (Harlan et al., 1987; Churchill and Kalivas, 1994) and may drive food intake via this input.', {'entities': [(107, 128, 'CITATION'), (144, 161, 'FUNCTION'), (67, 78, 'NEUROTRANSMITTER'), (54, 63, 'NEUROTRANSMITTER'), (40, 45, 'REGION'), (4, 6, 'REGION')]}),
    ('Importantly, evidence indicates that epigenetic mechanisms are involved in drug addiction.', {'entities': [(37, 58, 'FUNCTION'), (75, 89, 'FUNCTION')]}),
    ('Therefore, our second aim was to compare MOR binding density between intact male and female rats at both juvenile and adult ages.', {'entities': [(41, 44, 'PHYSIO')]}),
    ('In lamprey, the activity of the LHb is regulated by habenula-projecting globus pallidus (GPh).', {'entities': [(52, 71, 'FUNCTION'), (72, 87, 'REGION'), (32, 35, 'REGION'), (89, 92, 'REGION')]}),
    ('The more medial areas of the hypothalamus send aversive signals to the same receivers; thus, high spatial and functional selectivity must exist among the adjacent mesolimbic DA fibers.', {'entities': [(42, 63, 'FUNCTION'), (29, 41, 'REGION'), (163, 173, 'CELLTYPE'), (174, 176, 'NEUROTRANSMITTER')]}),
    ('Importantly, LHb neurons also project to the canonical pain modulating nucleus the periaqueductal gray [14, 15].\n', {'entities': [(45, 70, 'FUNCTION'), (83, 102, 'REGION'), (13, 24, 'CELLTYPE')]}),
    ('Thus, we tested if chemogenetic activation of the MHb ChAT expressing neurons alone is able to induce a conditioned preference or aversion.', {'entities': [(104, 138, 'FUNCTION'), (54, 77, 'CELLTYPE'), (50, 53, 'REGION')]}),
    ('In addition, we determined the percentage of GABA-positive cells using the neuronal marker NeuN. Finally, we examined the degree of colocalization of GABA with calcium-binding proteins calbindin (CB), calretinin (CR) and parvalbumin (PV) (markers for GABAergic interneurons) in the LS neurons.', {'entities': [(160, 184, 'PHYSIO'), (251, 273, 'CELLTYPE'), (45, 64, 'CELLTYPE'), (221, 232, 'PHYSIO'), (201, 211, 'PHYSIO'), (282, 292, 'CELLTYPE'), (185, 194, 'PHYSIO'), (75, 83, 'CELLTYPE'), (91, 95, 'PHYSIO'), (150, 154, 'NEUROTRANSMITTER'), (196, 198, 'PHYSIO'), (234, 236, 'PHYSIO')]}),
    ('In albino rats, Hb size asymmetry was reported with the left MHb being lightly larger than the one in the right one by 5%.', {'entities': [(61, 64, 'REGION'), (16, 18, 'REGION')]}),
    ("This interest is driven largely by the habenula's proposed role in mood and addiction disorders [Bourdy and Barrot, 2012; Hikosaka, 2010; Lammel et al., 2014; Lecca et al., 2014; Proulx et al., 2014].", {'entities': [(67, 95, 'FUNCTION'), (97, 114, 'CITATION'), (39, 47, 'REGION'), (122, 130, 'CITATION')]}),
    ('Furthermore, our high‐resolution imaging approach enabled us to confirm the functional connections between the Hb and the SN/VTA complex in humans, another important structure of the reward and learning system [Montague et al., 1996; Schultz, 2007a, 2007b;', {'entities': [(183, 209, 'FUNCTION'), (234, 241, 'CITATION'), (125, 128, 'REGION'), (111, 113, 'REGION'), (122, 124, 'REGION')]}),
    ('Both nicotinic acetylcholine receptors (nAChR) and muscarinic acetylcholine receptors (mAChR) are expressed in the hippocampus (Parfitt, et al. 2012).', {'entities': [(51, 85, 'PHYSIO'), (5, 38, 'PHYSIO'), (115, 126, 'REGION'), (128, 135, 'CITATION'), (40, 45, 'PHYSIO'), (87, 92, 'PHYSIO')]}),
    ('Nicotine acts in the brain through the neuronal nicotinic acetylcholine receptors (nAChRs), which are ligand-gated ion channels consisting of five membrane-spanning subunits3.', {'entities': [(48, 81, 'PHYSIO'), (0, 8, 'PHYSIO'), (39, 47, 'CELLTYPE'), (83, 89, 'PHYSIO')]}),
    ('Specifically, MOR activation increases anxiety-related behavior in adult mice (Le Merrer et al. 2006).', {'entities': [(29, 63, 'FUNCTION'), (14, 17, 'PHYSIO')]}),
    ('However, the KOP receptor is expressed by several types of neurons in the NAc, including both MSN populations and some interneurons (Oude Ophuis et al. 2014; Tejeda et al. 2017).', {'entities': [(133, 156, 'CITATION'), (158, 176, 'CITATION'), (13, 25, 'PHYSIO'), (119, 131, 'CELLTYPE'), (59, 66, 'CELLTYPE'), (74, 77, 'REGION'), (94, 97, 'CELLTYPE')]}),
    ('However, sensory nerves are linked to the sympathetic and angiotensin signaling and hence substance-P and CGRP do not affect blood pressure at rest in normal conditions.\n', {'entities': [(125, 139, 'FUNCTION'), (90, 101, 'PHYSIO'), (106, 110, 'PHYSIO')]}),
    ('In the mouse hypothalamus, PCSK1n, PEN–LEN, and LEN exist in large (PCSK1nL, PEN–LENL, and LENL) and small forms (PCSK1nS, PEN–LENS, and LENS) [1114].\n', {'entities': [(13, 25, 'REGION'), (77, 85, 'PHYSIO'), (123, 131, 'PHYSIO'), (35, 42, 'PHYSIO'), (68, 75, 'PHYSIO'), (114, 121, 'PHYSIO'), (27, 33, 'PHYSIO'), (91, 95, 'PHYSIO'), (137, 141, 'PHYSIO'), (48, 51, 'PHYSIO')]}),
    ('Supporting this observation, our data indicate that a meso-interpeduncular circuit consisting of a population of VTA DAergic neurons projecting to the ventral IPN exists thereby providing a link between reward and aversion circuits.', {'entities': [(203, 231, 'FUNCTION'), (54, 74, 'REGION'), (117, 132, 'CELLTYPE'), (151, 162, 'REGION'), (113, 116, 'REGION')]}),
    ('Also, electrical stimulation of the dPAG in human patients undergoing neurosurgery evokes feelings of dread accompanied by neurovegetative manifestations that overlap the symptoms of a PA (Table 1).Table 1.Similarities of the symptoms of a panic attack and the effects of electrical stimulation of the periaqueductal gray matter (PAG) in humans and rats.', {'entities': [(302, 328, 'REGION'), (36, 40, 'REGION'), (330, 333, 'REGION')]}),
    ('Some TRH-DE neurons may be TRH-R1 or TRH-R2 positive, because the maps of the distribution of Trhde, Trhr and Trhr2 mRNAs in the brain reveal a partial co-expression of Trhde and one of its receptors (Heuer et al., 2000).', {'entities': [(5, 19, 'CELLTYPE'), (27, 33, 'PHYSIO'), (37, 43, 'PHYSIO'), (94, 99, 'PHYSIO'), (110, 115, 'PHYSIO'), (129, 134, 'REGION'), (169, 174, 'PHYSIO'), (101, 105, 'PHYSIO')]}),
    ('This includes its role in aversion, goal-directed processing, behavioral flexibility and social behavior, all behavioral domains that are dysregulated in MDD.Reward and Aversion\nAppropriate allocation of sensory processing in a real time manner is necessary to detect the salience of a stimulus, so that an individual can react to maximize reward for effort expended (Proulx et al., 2014).', {'entities': [(36, 60, 'FUNCTION'), (62, 84, 'FUNCTION'), (89, 104, 'FUNCTION'), (26, 34, 'FUNCTION'), (154, 157, 'PHYSIO')]}),
    ('Activation of the galanin receptor might lead to hyperpolarization of the presynaptic cells by opening ATP-dependent K+-channels and closing voltage-dependent Ca2+-channels and hence impeding glutamate release and the progression of seizures [46, 47].', {'entities': [(49, 91, 'FUNCTION'), (218, 241, 'FUNCTION'), (18, 34, 'PHYSIO'), (192, 201, 'NEUROTRANSMITTER')]}),
    ("We have hypothesized that the lampreys' striatal subpallium is included in the nuclear amygdala of tetrapods (Loonen and Ivanova, 2015).", {'entities': [(40, 59, 'REGION'), (110, 128, 'CITATION'), (79, 95, 'REGION')]}),
    ('MiR146b inhibits SIRT1, thereby increasing FOXO1 acetylation and favoring obesity.', {'entities': [(32, 60, 'FUNCTION'), (65, 81, 'FUNCTION'), (8, 22, 'FUNCTION'), (0, 7, 'PHYSIO')]}),
    ('For example, the nucleus reuniens receives input from the prefrontal cortex and relays it to the hippocampus (Ito et al. 2015; Hallock et al. 2016).', {'entities': [(127, 146, 'CITATION'), (58, 75, 'REGION'), (17, 33, 'REGION'), (110, 125, 'CITATION'), (97, 108, 'REGION')]}),
    ('All MHb neurons expressed high levels of Slc17a6 and Slc17a7, the genes encoding vesicular glutamate transporters 1 and 2, and Tac2 suggesting that all MHb neurons are glutamatergic and produce the neuropeptide Neurokinin B (Figure 2D, Figure 2—figure supplement 3).', {'entities': [(81, 113, 'PHYSIO'), (168, 181, 'NEUROTRANSMITTER'), (211, 223, 'PHYSIO'), (4, 15, 'REGION'), (152, 163, 'REGION'), (41, 48, 'PHYSIO'), (53, 60, 'PHYSIO'), (127, 131, 'PHYSIO')]}),
    ('Importantly, with the exception of the arcuate nucleus and the PMH, in which Dat mRNA but not DAT protein was found, none of the other neuronal clusters outside the classical dopaminergic brain areas that were positive for tdTom mRNA or TdTOM protein in our study expressed the Dat gene.', {'entities': [(39, 54, 'REGION'), (237, 250, 'PHYSIO'), (175, 187, 'NEUROTRANSMITTER'), (94, 105, 'PHYSIO'), (223, 233, 'PHYSIO'), (77, 85, 'PHYSIO'), (135, 143, 'CELLTYPE'), (278, 286, 'PHYSIO'), (63, 66, 'REGION')]}),
    ('Colocalization of cells expressing GAD mRNAs with NeuN in the LS\nNeuN, a neuronal nuclear protein, serves as a specific marker for the vast majority of neurons in the central and peripheral nervous systems [62,63].', {'entities': [(167, 205, 'REGION'), (35, 44, 'PHYSIO'), (73, 81, 'CELLTYPE'), (152, 159, 'CELLTYPE'), (50, 54, 'PHYSIO'), (65, 69, 'PHYSIO'), (62, 64, 'REGION')]}),
    ('In any case, the preference of trilaminar cells to innervate other GABAergic interneurons points to a more prominent role in the disinhibition of pyramidal cells compared to a minimal contribution to gating of dendritic electrogenesis and burst firing in these same cells (Lovett-Barron et al. 2012;', {'entities': [(200, 234, 'FUNCTION'), (129, 161, 'FUNCTION'), (273, 298, 'CITATION'), (67, 89, 'CELLTYPE'), (31, 47, 'CELLTYPE'), (239, 251, 'FUNCTION')]}),
    ('Elegant reward-biased visual saccade studies conducted in non-human primates, demonstrated that LHb neurons regulate DA driven reward-prediction responses.', {'entities': [(108, 154, 'FUNCTION'), (96, 107, 'CELLTYPE')]}),
    ('Despite this, we now know that GABA receptors are found on most of the neuronal cell types and thus even a subregion-specific manipulation is likely to affect many different cell populations which may have opposing functional effects.', {'entities': [(71, 79, 'CELLTYPE'), (31, 35, 'NEUROTRANSMITTER')]}),
    ('LHb neurons are known to be excited by negative stimuli, including drug-induced negative stimuli [1], [2], [6].', {'entities': [(0, 11, 'CELLTYPE')]}),
    ('Subsequent investigations have demonstrated that extinction-impairing effects are mediated by MORs in the PAG [as shown with the selective MOR antagonist CTAP in the PAG (McNally, 2005; Parsons et al., 2010)].\n', {'entities': [(139, 153, 'PHYSIO'), (171, 178, 'CITATION'), (94, 98, 'PHYSIO'), (154, 158, 'PHYSIO'), (106, 109, 'REGION'), (166, 169, 'REGION')]}),
    ('Once enterochromaffin cells are activated, voltage-gated Ca2+ channels trigger release of serotonin, which excites serotonin-sensitive primary afferent sensory nerves via serotonin receptors at synaptic connections.', {'entities': [(135, 166, 'CELLTYPE'), (71, 99, 'FUNCTION'), (107, 134, 'FUNCTION'), (5, 27, 'CELLTYPE'), (171, 180, 'NEUROTRANSMITTER')]}),
    ('Other central regions are likely involved; for example, TRH increases the activity of lateral hypothalamus orexin neurons, which project to several areas involved in arousal (González et al., 2009; Hara et al., 2009).', {'entities': [(86, 106, 'REGION'), (107, 121, 'CELLTYPE'), (166, 173, 'FUNCTION'), (56, 59, 'PHYSIO')]}),
    ('Only one significant difference between control, resilient, and vulnerable individuals was found in the BLA of vulnerable individuals; ENK mRNA levels were decreased in vulnerable rats compared to control and resilient rats.', {'entities': [(135, 143, 'PHYSIO'), (104, 107, 'REGION')]}),
    ('The difficulty in demonstrating consistent changes in GABAA receptor function in dependent animals results, at least in part, from the complex changes in the production of different GABAA receptor subunits induced by chronic alcohol administration and withdrawal.', {'entities': [(54, 68, 'PHYSIO'), (182, 196, 'PHYSIO')]}),
    ('As suggested by Wallman and Winawer,181 although the density of many retinal neurons is highest in the central retina, the absolute numbers of neurons are higher in the periphery, simply because the peripheral retina is very large in comparison to the fovea.', {'entities': [(199, 216, 'REGION'), (69, 84, 'CELLTYPE'), (103, 117, 'REGION'), (143, 150, 'CELLTYPE'), (252, 257, 'REGION')]}),
    ('Interestingly, this cluster also expresses the μ opioid receptor, among others.', {'entities': [(47, 64, 'PHYSIO')]}),
    ('The dorsal pallium gives rise to the majority of the mammalian cerebral neocortex (Medina and Abellán, 2009).', {'entities': [(63, 81, 'REGION'), (83, 101, 'CITATION'), (4, 18, 'REGION')]}),
    ('Some projections also originate from the vlLH (Cullinan and Záborszky, 1991).', {'entities': [(47, 69, 'CITATION'), (41, 45, 'REGION')]}),
    ('Neurochemical profiles are further altered during dependence, with plasticity mechanisms in the DS/NAc potentiating striatonigral circuits driving compulsive drug-seeking behavior (indicated by the raised pie wedge).', {'entities': [(139, 179, 'FUNCTION'), (116, 129, 'REGION'), (99, 102, 'REGION'), (96, 98, 'REGION')]}),
    ('Presynaptically, GABAB heteroreceptors inhibit the release of glutamate, indirectly by reducing calcium influx and directly by inhibiting neurotransmitter release at the level of the SNARE complex.', {'entities': [(127, 162, 'FUNCTION'), (39, 71, 'FUNCTION'), (87, 110, 'FUNCTION'), (17, 38, 'PHYSIO'), (183, 196, 'PHYSIO')]}),
    ('Overall, these optogenetic studies have yielded compelling information regarding specific populations of neurons in the LHb that are implicated in the emergence of depressive behaviors following stress.', {'entities': [(151, 201, 'FUNCTION'), (105, 112, 'CELLTYPE'), (120, 123, 'REGION')]}),
    ('Since the activity of this neuronal population is linked to thermal and mechanical hypersensitivity in persistent pain models (see above), it is tempting to speculate that the CCI-produced PDYN and KOP receptor gene expression changes may contribute to the increased pain sensitivity.', {'entities': [(239, 283, 'FUNCTION'), (60, 99, 'FUNCTION'), (198, 210, 'PHYSIO'), (27, 35, 'CELLTYPE'), (189, 193, 'PHYSIO')]}),
    ('The predominant nAChR subtypes in mammalian brain that have been heavily implicated in regulating the addictive properties of nicotine are those containing α4 and β2 subunits (denoted α4β2* nAChRs)4,5,6,7,8.', {'entities': [(87, 134, 'FUNCTION'), (16, 30, 'PHYSIO'), (163, 174, 'PHYSIO'), (44, 49, 'REGION'), (156, 158, 'PHYSIO')]}),
    ('However, this subunit is not necessarily involved in nicotine withdrawal.', {'entities': [(53, 72, 'FUNCTION')]}),
    ('To validate Gq-DREADD activation of VP neurons, we injected mice with either CNO or Veh and immunostained for expression of the immediate-early gene product Fos 2 h afterward.', {'entities': [(22, 46, 'FUNCTION'), (12, 21, 'PHYSIO'), (77, 80, 'PHYSIO'), (84, 87, 'PHYSIO'), (157, 160, 'PHYSIO')]}),
    ('It is also supported by studies using transgenic animals, showing that genetically modified rats overexpressing the NPY gene are less susceptible to seizures while deletion of the NPY gene results in increased susceptibility to seizures [16, 17].', {'entities': [(149, 157, 'FUNCTION'), (228, 236, 'FUNCTION'), (116, 119, 'PHYSIO'), (180, 183, 'PHYSIO')]}),
    ('Methylene is commercially supplied as 100 mg blue liquid in 10 mL vials containing 10 mg/mL. Each vial costs about $11 US.', {'entities': []}),
    ('The numbers in the lower triangle represent the correlation coefficient.', {'entities': []}),
    ('In the midbrain, the PAG, deep gray layer of the superior colliculus (DpG), and deep mesencephalic nucleus (DpMe) received clear innervations from ARC POMC neurons.\n\n', {'entities': [(26, 68, 'REGION'), (114, 141, 'FUNCTION'), (80, 106, 'REGION'), (151, 163, 'CELLTYPE'), (7, 15, 'REGION'), (108, 112, 'REGION'), (21, 24, 'REGION'), (70, 73, 'REGION'), (147, 150, 'REGION')]}),
    ('This case represents a unique presentation of T-cell mediated HES with a lymphocytic variant for multiple reasons.', {'entities': [(73, 84, 'CELLTYPE'), (46, 52, 'CELLTYPE'), (62, 65, 'FUNCTION')]}),
    ('Despite rating their baseline communication skills highly, this seasoned group of clinicians had improvement in their knowledge and comfort with managing patients with CNMP after participating in the curriculum.', {'entities': []}),
    ('Results: The follow‐up period of 45 of these patients ranged from 0.5 to 12 years (mean 4.6 years).', {'entities': []}),
    ('The objetive of this study is to evaluate tolerance and acute side effects in patients who suffer DIPG, and are under ambulatory treatment with Nimotuzumab and Vinorelbine.\n\n', {'entities': []}),
    ('Results: From September 1993 to December 2010, 110 children were treated with RT.', {'entities': []}),
    ('Utox positive for heroin, cocaine, benzodiazepines, and cannabinoids.', {'entities': []}),
    ('Her final pathology revealed a microscopic high-grade serous adenocarcinoma in the left fallopian tube wall without evidence of metastatic disease.', {'entities': [(88, 107, 'REGION'), (128, 146, 'FUNCTION'), (61, 75, 'CELLTYPE')]}),
    ('The current study investigated (a) mean level differences in coping strategy, social support and quality of life between Caucasians and immigrants and (b) whether the impact of coping and social support on quality of life was moderated by ethnicity.\n\n', {'entities': []}),
    ('Methods: A retrospective survey was done with the 42 cases of fungemia in our hospital from Jan 2002 to Jan 2011\n\nResults: 40 cases candida fungemia accounted for 95.2% in 42 fugemia.', {'entities': []}),
    ('However, due our sample size our conclusions are limited.', {'entities': []}),
    ('UNCOMMON SEPSIS FOLLOWING PANCREATIC SURGERY\nArvind Kalyan Sundaram\n1,2; Carey C. Thomson1,2.', {'entities': []}),
    ('We have also shown that on the basis of projection targets the forebrain-projecting neurons include: cells that project to the cerebral cortex and basal forebrain (mesocorticolimbic; 6.6%), other neurons whose axons almost exclusively innervate the cerebral cortex (mesocortical; 6.6%), or the basal forebrain, AcbC and CPu (mesolimbic; 40%), and mesostriatal neurons that extensively innervate the CPu (6.6%; Figure 8).', {'entities': [(347, 367, 'CELLTYPE'), (164, 181, 'CELLTYPE'), (127, 142, 'REGION'), (147, 162, 'REGION'), (249, 264, 'REGION'), (294, 309, 'REGION'), (266, 278, 'CELLTYPE'), (325, 335, 'CELLTYPE'), (63, 72, 'REGION'), (84, 91, 'CELLTYPE'), (196, 203, 'CELLTYPE'), (311, 315, 'REGION'), (320, 323, 'REGION'), (399, 402, 'REGION')]}),
    ('Logistic binary regression was used to compute the odds ratios (OR) for Rb.\n\n', {'entities': []}),
    ('Results: Internal service evaluation has been completed.', {'entities': []}),
    ('The importance of assembling a multidisciplinary team of professionals, the challenges of operating a large initiative, and the complexities of implementation will be discussed.\n\n', {'entities': []}),
    ('Following the expression of the two membrane-tagged proteins of mtdTomato or EmGFP, ARC POMC neurons and their axonal fibers exhibited red fluorescence, whereas NTS POMC neurons were green.', {'entities': [(88, 100, 'CELLTYPE'), (165, 177, 'CELLTYPE'), (64, 73, 'PHYSIO'), (77, 82, 'PHYSIO'), (84, 87, 'REGION'), (161, 164, 'REGION')]}),
    ('Urine toxicology screen was positive only for marijuana.', {'entities': []}),
    ('We aimed to identify key concepts related to HSCT for SCA interest; decision‐making factors; educational material needs, and options for improving consultation services and informed consent.\n\n', {'entities': []}),
    ('We followed the Institutional Protocol to prevent bleeding and/or thrombosis, specific for each patient.', {'entities': []}),
    ('Median follow‐up for living patients is 29 months (3‐46).', {'entities': []}),
    ('Our objectives are that following the intervention, participating faculty will be able to goal-set to improve teaching skills and identify teaching strengths and weaknesses in order to deliver effective feedback on teaching skills.\n\n', {'entities': []}),
    ('Despite the generally poor axonal recovery from LINCs filled during ex vivo hippocampal recordings, we found that, collectively, local axons reached all layers of CA1 (Figure 1d, Figure 2b,c, Figure 2—figure supplement 3), suggesting a potentially broad impact of LINCs on neurons in the region.', {'entities': [(149, 166, 'REGION'), (76, 87, 'REGION'), (273, 280, 'CELLTYPE')]}),
    ('Secondly, 7 sets of parents who had lost a child to cancer within the last 1‐10 years.', {'entities': []}),
    ('MRI of the brain showed high T2- weighted signal in the both putamina of the basal ganglia, with low T1-weighted signal in the left putamen.', {'entities': [(61, 90, 'REGION'), (132, 139, 'REGION'), (11, 16, 'REGION')]}),
    ('Medical College of Wisconsin, Milwaukee, WI.', {'entities': []}),
    ('Results: Nine patients (5 male and 4 female) with GIST were enrolled in this study.', {'entities': []}),
    ('By hospital day two, his arm pain and fevers had resolved, and he was discharged home without further incident.\n\n', {'entities': []}),
    ('These findings suggest that online lifestyle support can be implemented in coordination with primary care medicine.\n\n\n', {'entities': []}),
    ('All patients received iv alkaline hydration, at least twice of the daily fluid maintenance.', {'entities': []}),
    ('In addition to consideration of alternative causes of muscle weakness, workup should include EMG and muscle biopsy.', {'entities': []}),
    ('To date, there are few published educational models for Internal Medicine residency programs.', {'entities': []}),
    ('Subjects with lymphoma had increased sensory symptoms, vibratory impairment, and deep tendon reflex decrements while subjects with ALL had worse strength deficits.', {'entities': [(81, 110, 'FUNCTION'), (27, 53, 'FUNCTION'), (55, 75, 'FUNCTION'), (14, 22, 'CELLTYPE')]}),
    ('We aimed to determine the features of subgroups according to immunophenotype, the correlation between clinical and other laboratory and their effects on prognosis retrospectively.\n\n', {'entities': []}),
    ('Methods: Patients with a history of chemotherapy, cranial radiation, or neurosurgery for a CNS tumor at ≤21 years who were at least 2 years after diagnosis were administered the 25‐minute Cogstate computer battery (5 tasks measuring neurocognitive functioning; see table) in the Yale Pediatric Oncology Clinic.', {'entities': []}),
    ('However, this relationship was confounded by the level of NIH funding.', {'entities': []}),
    ('Focus groups uniformly sorted quality into low, moderate and high quality feedback based on three criteria: specificity, quantitative ratings, actionable, Low quality feedback was nonspecific, moderate feedback had at least some specificity and high quality feedback included specificity plus either some aspect of quantification or was actionable.', {'entities': []}),
    ('On the contrary, the green fluorescence associated with DOR was often weak, which required amplification with eGFP-specific antibodies for proper visualization.', {'entities': [(110, 114, 'PHYSIO'), (56, 59, 'PHYSIO')]}),
    ('Although the input patterns for POMC neurons in the ARC and NTS are very different, we did observe several brain areas that served as the common input sources for both groups of POMC neurons.', {'entities': [(32, 44, 'CELLTYPE'), (178, 190, 'CELLTYPE'), (52, 55, 'REGION'), (60, 63, 'REGION')]}),
    ('Lastly we would like to educate all internists about the importance of early recognition and management, as well as the consequences of ischemic priapism.\n\n', {'entities': []}),
    ('MEASURES OF SUCCESS (DISCUSS QUALITATIVE AND/OR QUANTITATIVE METRICS WHICH WILL BE USED TO EVALUATE PROGRAM/INTERVENTION): Prior to start of recruitment and randomization, we asked PCPs for feedback on a draft of the clinical progress report we had designed for MAINTAIN-PC.', {'entities': []}),
    ('We defined a current program user as a participant with a log-in in past 28\xa0days.', {'entities': []}),
    ('Pleural effusion in myeloma can occur due to several mechanisms.', {'entities': [(0, 16, 'FUNCTION'), (20, 27, 'CELLTYPE')]}),
    ('ED visits were categorized, by discharge diagnosis, into non-emergent, primary care treatable, ED care needed but preventable, ED care needed and not preventable, and mental health-related visits, based on the NYU algorithm.', {'entities': []}),
    ('Results: Out of 67 patients, 40 had a progression and 27 a relapse.', {'entities': []}),
    ('EVALUATION: We used paired pre/post surveys to assess residents’ self-rated preparedness for communication challenges during outpatient ACP discussions before and after GOCARE.', {'entities': []}),
    ('CT head and basic laboratory results were unremarkable.', {'entities': []}),
    ('Paired t‐test and independent sample t‐tests were used to compare BMI z‐scores within and in‐between groups respectively.\n\n', {'entities': []}),
    ('He was discharged to subacute rehab after 30\xa0days of inpatient care and received ceftriaxone for a total of 12\xa0weeks.', {'entities': []}),
    ('DESCRIPTION: After reviewing clinical empathy literature and drawing on similar exercises used in other venues, teaching exercises were piloted in a one-hour session to each successive group of residents.', {'entities': []}),
    ("Results: Of the 67 patients operated for Wilms' tumor over a period of two years (2012‐2103).", {'entities': []}),
    ('Standardized assessment is compelling for several reasons.', {'entities': []}),
    ('University of California, San Diego, San Diego, CA.', {'entities': []}),
    ('It is a rare disease.', {'entities': []}),
    ('However, the current knowledge of 5-HT3R expression patterns in the CNS is somewhat limited and insufficient for understanding the functional diversity of 5-HT3Rs.', {'entities': [(155, 162, 'PHYSIO'), (34, 40, 'PHYSIO'), (68, 71, 'REGION')]}),
    ('NB cells were treated with perifosine and everolimus to inhibit the PI3K/AKT/MTOR pathway.\n\n', {'entities': [(56, 89, 'FUNCTION'), (27, 37, 'PHYSIO'), (42, 52, 'PHYSIO'), (0, 8, 'CELLTYPE')]}),
    ('OS and EFS were 98.5% and 86%.', {'entities': []}),
    ('There was prominent mitosis.', {'entities': []}),
    ('Validation in an independent cohort is ongoing.\n\n', {'entities': []}),
    ('The results of these classifications are also listed in Table 2.', {'entities': []}),
    ('A number of histone trimethylation states, among which H3K4me3, are linked to active gene expression, whereas the relationship between H3K27me3 and transcriptional status appears less unambiguous [24, 25].', {'entities': [(12, 34, 'PHYSIO'), (78, 100, 'FUNCTION'), (148, 170, 'FUNCTION'), (135, 143, 'PHYSIO')]}),
    ('For GWAS datasets, we adapted the principle components used in the original studies.', {'entities': []}),
    ('Comparison of protein levels of endogenous and recombinant proteins is difficult, because endogenous SF1 exists in multiple isoforms (Figure 3A; 76) and their exact contribution to splicing is not established.', {'entities': [(181, 189, 'FUNCTION'), (101, 104, 'PHYSIO')]}),
    ('In vitro KDM assay\nKDM6B (JMJD3) activity was measured using the JMJD3 Chemiluminescent Assay Kit (Tebu-Bio, The Netherlands) according to the manufacturers’ instructions.', {'entities': []}),
    ('The 1st most strong cluster represented by lung AC mitotic/cell cycle up-regulated genes, 2-nd cluster is represented by normal lung epithelial cells at the strong suppression, 3-rd and 4-th clusters are represented by the genes involved in cell communication, motility and the immune system.\n', {'entities': [(121, 149, 'CELLTYPE'), (241, 259, 'FUNCTION'), (43, 58, 'CELLTYPE'), (278, 291, 'FUNCTION'), (59, 69, 'PHYSIO'), (261, 269, 'FUNCTION')]}),
    ('Several infectious pathogens and toxins are well-known to use GSLs as cellular entry receptor.', {'entities': [(70, 93, 'FUNCTION'), (8, 28, 'PHYSIO'), (33, 39, 'PHYSIO'), (62, 66, 'PHYSIO')]}),
    ('The first slice was collected at the beginning at the anterior aspect of the corpus callosum, one section was collected every 500 µm apart until a total of six sections had been collected for each animal.', {'entities': [(54, 92, 'REGION')]}),
    ('These studies have suggested that fNIRS is capable to detect the effect of nutrients and food components on PFC activation.\n', {'entities': [(89, 104, 'PHYSIO'), (112, 122, 'FUNCTION'), (75, 84, 'PHYSIO'), (108, 111, 'REGION')]}),
    ('Mechanistically, CTIF associates with both the eukaryotic translation elongation factor 1 alpha 1 (eEF1A1) and dynactin 1 (DCTN1) through its N-terminal region, forming a functional complex called CTIF-eEF1A1-DCTN1 (CED) complex.', {'entities': [(47, 97, 'PHYSIO'), (197, 214, 'PHYSIO'), (111, 121, 'PHYSIO'), (99, 105, 'PHYSIO'), (123, 128, 'PHYSIO'), (17, 21, 'PHYSIO'), (216, 219, 'PHYSIO')]}),
    ('The human protein is listed first, followed by its ortholog in A.aegypti which is also predicted to interact with the DENV protein.', {'entities': []}),
    ('Thirty minutes after the injection, the brains were harvested, and tracer distribution evaluated in coronal sections as described previously\xa0(Iliff et al., 2012).', {'entities': [(40, 46, 'REGION')]}),
    ('In particular, edges of the triangles in the expression image may cross and create ambiguous regions.', {'entities': []}),
    ('Error bars show standard error from three or four biological replicates.', {'entities': []}),
    ('Their abilities are bound to numerous downstream effectors which lead to diverse parallel downstream signaling pathways [28].', {'entities': []}),
    ('Downregulated genes, which are not targeted by SA-miRNAs are shown with colored rim based on their functional category.', {'entities': [(47, 56, 'PHYSIO')]}),
    ('In an analysis more closely related to the one undertaken here, French and Pavlidis (2011) also ranked genes by correlation of expression level with connectivity degree, but this was not studied in any detail.', {'entities': []}),
    ('Of the 325 genes identified in the present study with transcript levels altered at P\u2009<\u20090.005, only 144 of these transcripts have been reported to be altered in BDNF-null mice at the least stringent level of significance, P\u2009<\u20090.05 [18] (Figure\xa04c).', {'entities': [(160, 174, 'PHYSIO')]}),
    ('In particular, the techniques of concurrent brain manipulation, including TMS and tDCS, and EEG imaging, show greatly encouraging clinical potential.', {'entities': []}),
    ('Immediately after the capillary was removed, a small amount of Kwik-Cast Sealant (KWIK-CAST, World Precision Instruments) was applied to seal the site of injection.', {'entities': []}),
    ('D-PDMP treatment reduced the markers for cell proliferation and angiogenesis.', {'entities': [(41, 59, 'FUNCTION'), (64, 76, 'FUNCTION'), (0, 6, 'PHYSIO')]}),
    ('Further data analyses were conducted using an in-house R pipeline containing tools for identifying peaks overlapping in two samples, the analysis of genomic distribution of peaks and the integration of peak and gene expression datasets.', {'entities': []}),
    ('Thus, its repurposing as remyelinating drug may have several advantages compared to the development of entirely new compounds since its safety profile has been confirmed by exhaustive clinical applications.', {'entities': [(25, 43, 'FUNCTION')]}),
    ('On the other hand, overexpression of human alpha-synuclein in the AAV-injected (right) substantia nigra caused a slight decrease (−13%) in TH-positive cells in wild-type mice and a more pronounced reduction (−29%) in L444P/+ animals (Fig. 6B).', {'entities': [(139, 156, 'CELLTYPE'), (87, 103, 'REGION'), (43, 58, 'PHYSIO')]}),
    ('Gene Ontology enrichment analysis was performed using topGO [98, 99].', {'entities': []}),
    ('The residual homogenates were adjusted to 10.5% (w/v) sucrose in 5 mM Tris-HCl (pH 7.4) and overlaid onto 10 ml of 30% (w/v) sucrose in 5 mM Tris-HCl (pH 7.4).', {'entities': []}),
    ('P < 0.05; ns, non-significant.', {'entities': []}),
    ('This review discusses the most commonly used MRI measures and our current knowledge of brain development through longitudinal investigations (Section 2), the biological validity of interpretations derived from these investigations (Sections 3, 4), as well as the variety of methods to process, analyze and model longitudinal changes in brain structure (Sections 5, 6).', {'entities': []}),
    ('Both monomers are composed of GTP molecules.', {'entities': [(0, 13, 'PHYSIO'), (30, 43, 'PHYSIO')]}),
    ('Many of the longitudinal studies described in the previous sections have modeled brain development during childhood and adolescence against age, and it remains the most popular measure of biological development.\n', {'entities': []}),
    ('Here we present a novel block mixture model and novel algorithms for optimizing the model.', {'entities': []}),
    ('NMNAT2 is involved in nicotinate and nicotinamide metabolism, and is a novel regulator of cell proliferation and apoptosis in NSCLC by binding with SIRT3 [44].\n', {'entities': [(22, 60, 'FUNCTION'), (77, 108, 'FUNCTION'), (113, 122, 'FUNCTION'), (0, 6, 'PHYSIO'), (126, 131, 'REGION'), (148, 153, 'PHYSIO')]}),
    ('FA activation occurs primarily via acyl-CoA synthetase long-chain family member isoforms (ACSL) [31].', {'entities': [(35, 54, 'PHYSIO'), (0, 13, 'FUNCTION')]}),
    ('The B3gnt5 enzyme also initiates the formation of the SSEA-1 epitope, which is identical to the Lewis X antigen.', {'entities': [(96, 111, 'PHYSIO'), (4, 10, 'PHYSIO'), (54, 60, 'PHYSIO')]}),
    ('Next, we adjusted the cortical subregional measures for height (Table S4).', {'entities': [(22, 42, 'REGION')]}),
    ('Alternatively, although within the same production category (dairy, beef, dual-purpose), the breeds may have been selected for subtly different production characteristics or have been subjected to differential natural (environmental) selection.', {'entities': []}),
    ('These results demonstrated that cilengitide reduced bevacizumab-induced invasion.', {'entities': [(44, 80, 'FUNCTION'), (32, 43, 'PHYSIO')]}),
    ('Cycling was performed according to standard procedure.', {'entities': []}),
    ('The existence and general function of TREX seems conserved in plants [8,75,192,193], and it also appears to play a role in the transport of small-interfering RNA precursors for long-distance gene-silencing effects [8,194].', {'entities': [(127, 172, 'FUNCTION'), (177, 213, 'FUNCTION'), (38, 42, 'PHYSIO')]}),
    ('It is this degree of individual variability that makes longitudinal designs imperative for describing developmental trajectories.', {'entities': []}),
    ('In addition to detecting genes in the microarray platform associated with the glioblastoma survival, particular attention was given to genes known to be associated with glioblastoma and the association detected in this study.', {'entities': [(78, 90, 'CELLTYPE'), (169, 181, 'CELLTYPE')]}),
    ('Gene Set Enrichment Analysis\nFrom our association-based results and functional annotation, we observed that genes with the term “sphingolipid” and “myelin” were statistically over-represented in this brain region.', {'entities': []}),
    ('Zuberbier et al. studied the alterations of ganglioside expression during maturation of the human mast cell line HMC-1.', {'entities': [(44, 55, 'PHYSIO'), (98, 107, 'CELLTYPE'), (113, 118, 'CELLTYPE')]}),
    ('Table 4 illustrates the results of tests recovering block constant structure from 50 × 50 element matrices with 5 row and 5 column classes.', {'entities': []}),
    ('This was used as part of a secondary analysis, described below.', {'entities': []}),
    ('Moreover, deletion of AQP4 potentiated the increases in intracranial pressure in a murine model of hydrocephalus consistent with the notion that AQP4 supports and facilitates intraparenchymal fluid flow (Bloch et al., 2006).\n', {'entities': [(43, 77, 'FUNCTION'), (175, 202, 'FUNCTION'), (22, 26, 'PHYSIO'), (145, 149, 'PHYSIO')]}),
    ('A combination of AD-specific miRNA expression signatures with the rapidly developing and expanding amyloid load imaging techniques may be useful as non-invasive diagnostic tools in AD diagnosis in the future [20].ResultsInitial biomarker screening using next-generation sequencing\nTo detect potential AD biomarkers we examined blood from well-characterized patients and controls.', {'entities': [(99, 106, 'PHYSIO'), (29, 34, 'PHYSIO')]}),
    ('Another compound that exhibited a pro-differentiative effect on OPCs in presence of CSPG components is protamine, a polycationic peptide that is widely used clinically to stop the anticoagulant effects of heparin and that showed a high affinity for aggrecan-coated substrates.', {'entities': [(180, 201, 'FUNCTION'), (116, 136, 'PHYSIO'), (103, 112, 'PHYSIO'), (249, 257, 'PHYSIO'), (205, 212, 'PHYSIO'), (64, 68, 'CELLTYPE'), (84, 88, 'PHYSIO')]}),
    ('There were 1,388 shared nodes and 1,766 shared interactions between these two sub-networks.', {'entities': []}),
    ('119 transcripts showed significant changes in their steady-state level in Elavl3/4 KO mice, 91 of which were expressed in human brain.', {'entities': [(74, 90, 'PHYSIO'), (122, 133, 'REGION')]}),
    ('After 30 min, mice were euthanized and perfusion-fixed with carbodiimide/glutaraldehyde.\xa0', {'entities': [(73, 87, 'PHYSIO'), (60, 72, 'PHYSIO')]}),
    ('Click here for fileAdditional file 3\nTable S2.', {'entities': []}),
    ('In addition to DNAm, histone modifications have also been implicated in the etiology of MDD (reviewed in 203).', {'entities': [(21, 42, 'PHYSIO'), (76, 91, 'FUNCTION'), (15, 19, 'PHYSIO')]}),
    ('In order to detect the non-redundant sets of genes and associated biological themes, we performed a clustering analysis using enriched gene categories from the databases GO, Kyoto Encyclopedia of Genes and Genomes (KEGG), Reactome and CGAP tissue EST expression for the 1063 true LXR target genes.', {'entities': []}),
    ("Authors' contributions\nFB screened ES cells for homologous recombination characterized positive ES cell clones, was responsible for mouse breeding and phenotyping, and participated to manuscript preparation.", {'entities': []}),
    ('Tumor growth measurement was performed by direct tumor weight assessment at the end of the experiment.', {'entities': []}),
    ('The Illumina Sentrix Mouse-6 BeadChip V1.0 interrogated approximately 46,000 sequences from the mouse transcriptome.', {'entities': []}),
    ('On the other hand, although EEG is a useful electrophysiological technique, its very low spatial resolution makes it difficult to precisely identify the activated areas of the brain, limiting its application to specific research questions related to eating disorders (Jauregui-Lobera, 2012).', {'entities': [(250, 266, 'FUNCTION'), (268, 283, 'CITATION'), (176, 181, 'REGION')]}),
    ('Co-immunopurified proteins were analysed by western blotting.\n', {'entities': []}),
    ('We did not measure water turnover in our study animals before the removal of drinking water.', {'entities': []}),
    ('Additional SNPs of Interest\nWe identified 7 SNPs with suggestive evidence of association (p < 5 x 10−4) located in or within 20 kb of 7 genes with links to hearing loss (Table 1).', {'entities': []}),
    ('We did not treat periventricular and deep WMH separately, as has been done in some previous studies, because these have been shown to be highly correlated [e.g. DeCarli et al., 2005 found the correlation to be around r\u2009=\u20090.9] and their division may be arbitrary: for example, periventricular WMH are often contiguous with superior deep WMH.\n', {'entities': [(276, 295, 'REGION'), (322, 339, 'REGION'), (17, 32, 'REGION'), (37, 45, 'REGION')]}),
    ('The original report from the URMC group on the glymphatic system showed that deletion of astrocytic water channels suppressed both the influx of CSF tracers injected into the cisterna magna and the efflux of tracers infused directly into striatum (Iliff et al., 2012).', {'entities': [(47, 64, 'PHYSIO'), (100, 114, 'PHYSIO'), (175, 189, 'REGION'), (135, 148, 'FUNCTION'), (89, 99, 'CELLTYPE'), (238, 246, 'REGION')]}),
    ('(B)\nPrincipal component analysis shows distinct transcriptome segregation for\nthe purified populations along three principal components axes.', {'entities': []}),
    ('The expression of Lc3 synthase in splenic B cells is interesting in light of the high level of activity with gangliosides synthesized through GM3 and GM1 [33].', {'entities': [(34, 49, 'CELLTYPE'), (18, 30, 'PHYSIO'), (109, 121, 'PHYSIO'), (142, 145, 'PHYSIO'), (150, 153, 'PHYSIO')]}),
    ('At 8 years of age, he was diagnosed with transient peripheral facial nerve palsy.', {'entities': []}),
    ('Ceramide could also be hydrolyzed to generate sphingosine and its derivatives (Figure 2C–E).', {'entities': [(46, 57, 'PHYSIO'), (0, 8, 'PHYSIO')]}),
    ('Human peripheral B cells contain relatively large amounts of more complex globosides which are nearly absent in tonsillar B lymphocytes (32, 62).', {'entities': [(112, 135, 'CELLTYPE'), (6, 24, 'CELLTYPE'), (74, 84, 'PHYSIO')]}),
    ('It has been reported that BEX family members could regulate cell cycle and apoptotic signaling [10, 11].\n', {'entities': [(51, 70, 'FUNCTION'), (75, 94, 'FUNCTION'), (26, 44, 'PHYSIO')]}),
    ('This effect was particularly evident in the caudolateral region of the substantia nigra pars reticulata, where bilateral electrolytic lesions resulted in attenuation of the severity of ethanol withdrawal symptoms (Chen et al. 2011b).', {'entities': [(44, 103, 'REGION'), (185, 212, 'FUNCTION')]}),
    ('Grb2 recruits Sos, which activates the Ras/MAPK signalling pathway [34].', {'entities': [(25, 66, 'FUNCTION'), (5, 17, 'FUNCTION'), (0, 4, 'PHYSIO')]}),
    ('In brief, Aqp4 KO mice were generated on a CD1 background, following the construction of a targeting vector for homologous recombination of a 7 kb SacI AQP4 genomic fragment, in which part of the exon one coding sequence was deleted.', {'entities': [(147, 173, 'PHYSIO'), (10, 14, 'PHYSIO'), (43, 46, 'PHYSIO')]}),
    ('MVPA may be preferable if there is a distributed set of multiple brain networks that underlie a complex neuropsychological construct such as cue-induce food craving.', {'entities': [(141, 164, 'FUNCTION'), (0, 4, 'PHYSIO')]}),
    ('However, when a complete ECD signature was compared using the best differentially expressed gene signatures of alternative methods, the ECD provides significantly larger number of the genes separating AC and AT samples (Figure 6).', {'entities': []}),
    ('Values differing at least two standard deviations from the mean were considered indicative a significant difference in expression.', {'entities': []}),
    ('Accordingly, the DI of wt mice was in the normal range (DI: 0.67±0.08; *p<0.05), while N-Shc-/- mice showed a total lack of discrimination between novel and familiar objects, (DI: -0.07±0.22).Figure 1(A) ChAT fluorescent immunolabeling (Millipore, goat, 1:1000; anti-goat Alexa488 antibody) in the MS, DbB and CA1 of 10 months old male N-Shc -/- and age-matched male wt mice.', {'entities': [(204, 208, 'PHYSIO'), (302, 305, 'REGION'), (310, 313, 'REGION'), (298, 300, 'REGION')]}),
    ('To address this question, we silenced caspase-3 (Figure 6b) and then monitored Bid processing upon treatment with ABT-737 and TRAIL.', {'entities': [(79, 93, 'FUNCTION'), (38, 47, 'PHYSIO'), (126, 131, 'PHYSIO')]}),
    ('The Fgfr3-iCreER PAC transgenic line was obtained from William Richardson (UCL, UK)85.', {'entities': [(4, 16, 'PHYSIO')]}),
    ('However, this conflicting observation may be due to the type of cell line used (U87 cell-line), since the experiment was only carried out using a single cell line.', {'entities': [(80, 93, 'CELLTYPE')]}),
    ('The other eight sheep showed similar responses during the experimental protocol.', {'entities': []}),
    ('mRNA abundance of OSBP and related genes (OSBPL2, OSBPL10) in mammary was comparable with that of SREBF1 and 2, and their expression was up-regulated ~1.5-fold during lactation (Figure 5) suggesting a functional role, likely involving the regulation of SREBF1 and the coordination of sphingolipid and cholesterol synthesis.', {'entities': [(268, 322, 'FUNCTION'), (50, 57, 'PHYSIO'), (62, 69, 'REGION'), (42, 48, 'PHYSIO'), (98, 104, 'PHYSIO'), (253, 259, 'PHYSIO'), (0, 4, 'PHYSIO'), (18, 22, 'PHYSIO')]}),
    ('All animal experiments were performed in accordance with approved animal policies of the National Public Health Institute, Helsinki.', {'entities': []}),
    ('The column (Acquity BEH C4, 1 × 100 mm) was eluted with a gradient of 75% solvent A (ACN/water/5 mM NH4-formate) to 100 % solvent B (ACN/MeOH/5 mM NH4-formate) over 10 minutes.', {'entities': []}),
    ('The package also implements T-test, Wilcoxon Test, LIMMA, LIMMA-trend [11], and RankProd [13] for testing differences between both groups.', {'entities': []}),
    ('The possibility of obtaining a similar antiglioblastoma response with single-dose reduction by combining BCNU with RTV is thus more relevant clinically for BCNU, which could in principle be administered for longer times before reaching its cumulative limiting dose.', {'entities': []}),
    ('Raw data, too low to be trusted: .', {'entities': []}),
    ('The “doublecortin regulators” act on DCX to aid effective migration.', {'entities': [(30, 67, 'FUNCTION'), (5, 28, 'PHYSIO')]}),
    ('Interestingly, DCX may also be implicated in the development of cancer cells due to its significance in the migration of neuroblasts.', {'entities': [(64, 76, 'CELLTYPE'), (49, 60, 'FUNCTION'), (121, 132, 'CELLTYPE'), (108, 117, 'FUNCTION'), (15, 18, 'PHYSIO')]}),
    ('Genes2Networks (G2N) module of X2K connects TFs with PPI to yield transcriptional complexes related to these gene signatures.', {'entities': []}),
    ('Details of networks are available in Additional file 1 (Supplementary Materials and Discussion) and the legend of Figure 6.', {'entities': []}),
    ('Besides RO60, Y RNPs contain several other RBPs such as ZBP1, MOV10, and Y-box proteins, and have been found to be remodeled upon stress (Sim et al., 2012).', {'entities': [(115, 136, 'FUNCTION'), (73, 87, 'PHYSIO'), (14, 20, 'PHYSIO'), (62, 67, 'PHYSIO'), (8, 12, 'PHYSIO'), (43, 47, 'PHYSIO'), (56, 60, 'PHYSIO'), (150, 154, 'CITATION')]}),
    ('(D) Accumulation of S129 phosphorylated alpha-synuclein in the right (AAV-injected) ventral mesencephalon of L444P/+ and wild-type mice.', {'entities': [(84, 105, 'REGION'), (40, 55, 'PHYSIO')]}),
    ('Supporting InformationS1 TablePrimers for real-time PCR.\n', {'entities': []}),
    ('It has been noted by several researchers that the potential influences of sex are under-explored in neuroscientific research (Beery and Zucker 2011; Cahill 2006, 2017; Karp et al. 2017).', {'entities': [(126, 147, 'CITATION')]}),
    ('The length of a given locus was systematically extended, ranging between 5,000 to 20,000,000 base pairs and 2 to 100 genes.', {'entities': []}),
    ('Sixty patients could be included in the miRNA analyses, the first 38 for the derivation group and the further consecutive 22 for the validation one.', {'entities': [(40, 45, 'PHYSIO')]}),
    ('ELAVL proteins have been shown to regulate several aspects of RNA metabolism.', {'entities': [(62, 76, 'FUNCTION'), (0, 5, 'PHYSIO')]}),
    ('Intriguingly, these glutamatergic impairments strongly related to epigenetic dysregulation in long-term heroin users19.', {'entities': [(66, 90, 'FUNCTION'), (20, 33, 'NEUROTRANSMITTER')]}),
    ('Interestingly, however, a prospective study found that young adults who showed lower recruitment of striatal regions in response to milk shake receipt (Stice et al., 2008b, 2015) and palatable food images (Stice et al., 2010b) showed greater future weight gain if they had a genetic propensity for reduced DA signaling capacity.', {'entities': [(309, 327, 'FUNCTION'), (100, 116, 'REGION'), (152, 163, 'CITATION'), (206, 217, 'CITATION'), (306, 308, 'NEUROTRANSMITTER')]}),
    ('These intermediate size deletions and duplications, referred to as copy number variations (CNVs), are more common in the general population than ever imagined before and could account for more genomic differences among sindividuals than single nucleotide polymorphisms (SNPs) [1], [2].', {'entities': []}),
    ('CTNNB1 is considered the cancer drivers for hepatocellular carcinoma development with variable frequencies depending on the etiology.', {'entities': [(59, 80, 'FUNCTION'), (25, 39, 'FUNCTION'), (44, 58, 'CELLTYPE'), (0, 6, 'PHYSIO')]}),
    ('For example, retrograde endocannabinoid signaling, a pathway mainly consisting of neuromodulatory endocannabinoids and their receptors, and playing important role in mediating global modulation of synaptic strength, localized short-term associative plasticity and cerebellar long term depression, was identified as enriched pathway for schizophrenia.', {'entities': [(166, 214, 'FUNCTION'), (216, 259, 'FUNCTION'), (13, 49, 'PHYSIO'), (275, 295, 'FUNCTION'), (264, 274, 'REGION')]}),
    ('In addition, the common pathways enriched for two diseases including neurotransmitters receptor signaling transduction pathways and intracellular signaling transduction cascades were also included, i.e. dopamine synapse, glutamateric synapse, nicotine addiction and cAMP signaling pathways, etc.', {'entities': [(266, 289, 'FUNCTION'), (243, 261, 'FUNCTION'), (221, 233, 'NEUROTRANSMITTER'), (203, 211, 'NEUROTRANSMITTER'), (212, 219, 'PHYSIO'), (234, 241, 'PHYSIO')]}),
    ('Brain regions are colored as orange for endbrain, cyan for hindbrain, purple for interbrain, and gray for midbrain.', {'entities': [(81, 91, 'REGION'), (59, 68, 'REGION'), (40, 48, 'REGION'), (106, 114, 'REGION')]}),
    ('Similar to anesthesia type, this variable also functioned as a proxy for the null study since all other datasets reported an exact volumetric injection rate.', {'entities': []}),
    ('Relative gene expression was analyzed using the CT method87.', {'entities': []}),
    ('The most prominent change was the -6.4 fold downregulation of kinesin family member 5C (Kif5c), followed by DEAD (Asp-Glu-Ala-Asp) box polypeptide 6 (Ddx6) and Gprc5b (-6.0 and -5.7 respectively).', {'entities': [(62, 86, 'PHYSIO'), (160, 166, 'PHYSIO'), (108, 112, 'PHYSIO'), (150, 154, 'PHYSIO')]}),
    ('While the ECD classifier was derived using the cross-normalized dataset as input, the classifiers derived using PAM, EDGE, WT and t-test used the original MAS5-normalized data as input.', {'entities': []}),
    ('While “one-gene-at-a-time” studies can provide important information on the contributions of individual genes and evolutionarily conserved pathways to alcohol sensitivity, it is becoming increasingly clear that complex phenotypes are emergent features of dynamic networks of interacting genes (Ayroles et al. 2009; Morozova et al. 2012).', {'entities': [(315, 335, 'CITATION'), (294, 313, 'CITATION')]}),
    ('Furthermore, we acknowledge that a more comprehensive review also covering Bos indicus and African Bos taurus cattle would provide an enhanced overview of the impact of artificial and natural selection on the cattle genome.', {'entities': []}),
    ('Accordingly, using the same analysis method of French and Pavlidis (2011) to evaluate relationships between expression and connectivity patterns, the pattern NE and OE genes (pooled) were not significant.', {'entities': []}),
    ('Unlike ShcC, ShcB is present in retina, heart and vascular endothelial cells [20], while ShcC shows a unique expression in lymphocytes that is not shown by ShcB [21].\n', {'entities': [(50, 76, 'CELLTYPE'), (123, 134, 'CELLTYPE'), (32, 38, 'REGION'), (40, 45, 'REGION'), (7, 11, 'PHYSIO'), (13, 17, 'PHYSIO'), (89, 93, 'PHYSIO'), (156, 160, 'PHYSIO')]}),
    ('The color shade intensity of the node correlates with the expression level of the indicated genes.', {'entities': []}),
    ('Several synaptic neurotransmitter pathways have also been implicated in alcohol sensitivity, including signaling through dopamine (Bainton et al. 2000; Kong et al. 2010), the GABABR1 receptor (Dzitoyeva et al. 2003), neuropeptide F (Wen et al. 2005) and octopamine (Scholz et al. 2000; Rothenfluh and Heberlein 2002; Guarnieri and Heberlein 2003).', {'entities': [(8, 42, 'PHYSIO'), (286, 315, 'CITATION'), (317, 345, 'CITATION'), (193, 214, 'CITATION'), (72, 91, 'FUNCTION'), (131, 150, 'CITATION'), (266, 284, 'CITATION'), (152, 168, 'CITATION'), (175, 191, 'PHYSIO'), (233, 248, 'CITATION'), (217, 231, 'NEUROTRANSMITTER'), (254, 264, 'NEUROTRANSMITTER'), (121, 129, 'NEUROTRANSMITTER')]}),
    ('57 × 10−5).', {'entities': []}),
    ('Pathway analyses of DEGs were determined according to the Kyoto Encyclopedia of Genes and Genomes (KEGG) database.', {'entities': []}),
    ('These sugars are added post-translationally in the Golgi to serine residues onto core proteins moiety and can be further extensively modified in subsequent steps that lead to at least sulfation and epimerization.', {'entities': [(60, 75, 'PHYSIO'), (51, 56, 'PHYSIO')]}),
    ('Competition between tumor and cytotoxic T cells for limited glucose in the TME hampers immune response [5,15].', {'entities': [(79, 102, 'FUNCTION'), (30, 47, 'CELLTYPE'), (20, 25, 'CELLTYPE'), (75, 78, 'REGION')]}),
    ('6-35.', {'entities': []}),
    ('Patients usually develop symptoms between the second and fifth decade.', {'entities': []}),
    ('Epe1 also promotes histone turnover in heterochromatin and acts to prevent spreading of heterochromatin beyond its boundaries [37,40].', {'entities': [(67, 103, 'FUNCTION'), (10, 35, 'FUNCTION'), (39, 54, 'PHYSIO'), (0, 4, 'PHYSIO')]}),
    ('1 M Tris-HCl pH 7.', {'entities': []}),
    ('The mRNA expression levels of HPRT across groups were not statistically different (see Fig.', {'entities': [(4, 8, 'PHYSIO'), (30, 34, 'PHYSIO')]}),
    ('A chemical identity card of the receptor was made available to the scientific community, the first ever established for a neurotransmitter receptor.', {'entities': []}),
    ('To determine the basis for the altered BA profile, liver enzyme mRNAs responsible for BA synthesis including Cyp7a1, Cyp8b1, Cyp27a1, and Cyp7b1 were detected by qPCR.', {'entities': [(51, 69, 'PHYSIO'), (86, 98, 'FUNCTION'), (39, 49, 'FUNCTION'), (125, 132, 'PHYSIO'), (109, 115, 'PHYSIO'), (117, 123, 'PHYSIO'), (138, 144, 'PHYSIO')]}),
    ('81RR case (n= 84)37 (44)37 (44)10 (12)0.', {'entities': []}),
    ('Some of the most important studies investigating the role of this metal on miRNA in in vitro and in vivo models are summarized in Table 2.', {'entities': [(75, 80, 'PHYSIO')]}),
    ('Inbreeded from Cyfip1HET mice, fertilized Cyfip1 KO oocytes are detectable in blastocyst stage [223].', {'entities': [(15, 29, 'PHYSIO'), (78, 88, 'CELLTYPE'), (52, 59, 'CELLTYPE'), (42, 48, 'PHYSIO')]}),
    ('Thus, hyperactivation of TGF-β signaling is responsible for the renal fibrosis and can also be identified as the hallmark of CKD.', {'entities': [(25, 40, 'PHYSIO'), (64, 78, 'FUNCTION'), (125, 128, 'FUNCTION')]}),
    ('However, extracellular Pro did not affect expression of NF-κB in fibroblasts.', {'entities': [(9, 26, 'PHYSIO'), (65, 76, 'CELLTYPE'), (56, 61, 'PHYSIO')]}),
    ('1C, lower panel; Supplementary Fig.', {'entities': []}),
    ('The existence of a small population of VGAT+ beta cells containing GABA in insulin granules reconciles our observations with previous reports of quantal exocytotic GABA release events that coincide with insulin release31.', {'entities': [(75, 91, 'PHYSIO'), (153, 163, 'FUNCTION'), (67, 71, 'NEUROTRANSMITTER'), (164, 168, 'NEUROTRANSMITTER')]}),
    ('The cAMP/PKA pathway participates in adipogenesis process regulation.', {'entities': [(37, 68, 'FUNCTION'), (4, 20, 'PHYSIO')]}),
    ('The scores were calculated by the right-tailed Fisher’s exact test.', {'entities': []}),
    ('Recently, it was demonstrated that luteolin effectively suppresses IL-1β, TNF-α, IL-6 and IL-8 secretion from PBMC from healthy donors incubated with LPS [203], confirming reports showing that luteolin reduces IL-6 and TNF-α secretion in LPS-stimulated RAW 264.', {'entities': [(44, 66, 'FUNCTION'), (35, 43, 'PHYSIO'), (193, 201, 'PHYSIO'), (67, 72, 'PHYSIO'), (74, 79, 'PHYSIO'), (219, 224, 'PHYSIO'), (81, 85, 'PHYSIO'), (90, 94, 'PHYSIO'), (110, 114, 'REGION'), (210, 214, 'PHYSIO'), (150, 153, 'PHYSIO'), (238, 241, 'PHYSIO')]}),
    ('Cold exposure has been reported to trigger a metabolic program and enhance energy expenditure, and this process is partially mediated by CYP7B1 [46].', {'entities': [(35, 62, 'FUNCTION'), (67, 93, 'FUNCTION'), (137, 143, 'PHYSIO')]}),
    ('An ensuing question is how to find the subset of marks.', {'entities': []}),
    ('Plasmatic levels of miR-422a were negatively correlated with muscle strength, and this miR was highly expressed in muscle [41].', {'entities': [(61, 76, 'FUNCTION'), (20, 28, 'PHYSIO'), (115, 121, 'CELLTYPE')]}),
    ('These sectioned tissues were used for FISH staining as described.', {'entities': []}),
    ('Data are presented as the mean ± SD of three technical replicates (*p < 0.', {'entities': []}),
    ('proposed a metric, local network similarity (LNS) to quantify expression divergence of orthologous genes [67].', {'entities': []}),
    ('In the same study, cell surface GRP78 expression was inversely correlated with E-cadherin expression, while positively correlating with N-cadherin expression; these observations allowed the authors to suggest the implication of cell surface-bound GRP78 in EMT regulation [243].', {'entities': [(79, 100, 'FUNCTION'), (136, 157, 'FUNCTION'), (32, 37, 'PHYSIO'), (247, 252, 'PHYSIO')]}),
    ('One small nonrandomized but multicenter trial of 61 patients with remdesivir reported clinical improvement in 36 of the 53 patients for whom data could be analyzed; however, there was no control group and a high number of side effects with serious side effects were reported in 12 patients (44).', {'entities': []}),
    ('Coronaviruses usually cause respiratory infections, such as those detected in the common cold, in patients.', {'entities': [(22, 50, 'FUNCTION'), (0, 13, 'PHYSIO')]}),
    ('As expected, MAP1889c induced significant production of IL-10, IL-1β, IL-6, and IL-12p70 in a dose-dependent manner when compared with untreated cells (Figure 3B).', {'entities': [(22, 55, 'FUNCTION'), (135, 150, 'CELLTYPE'), (13, 21, 'PHYSIO'), (80, 88, 'PHYSIO'), (56, 61, 'PHYSIO'), (63, 68, 'PHYSIO'), (70, 74, 'PHYSIO')]}),
    ('To clarify this issue, we redid the “one mark removal” analysis using downloaded NarrowPeak data files for the same set of histone marks.', {'entities': []}),
    ('Treatment with a current pediatric B‐cell lymphoma regimen in these patients achieved CR with durable remission.\n\n', {'entities': [(35, 50, 'CELLTYPE')]}),
    ('DESCRIPTION: HCD is a first year course with mandatory attendance.', {'entities': []}),
    ('For patients with multiple ICU admissions, only the first stay was included.', {'entities': []}),
    ('In other cases, the material obtained for morphological examination.', {'entities': []}),
    ('1New York University, New York, NY; 2New York University, New York, NY; 3New York University, New York, NY.', {'entities': []}),
    ('Fourteen of the 36 patients referred to use TLC-PA completed a survey about the office referral encounter.', {'entities': []}),
    ('Future work will provide important additional information about the roles of LINCs not only in healthy physiology, but also pathophysiology, including determining whether manipulation of LINCs could provide therapeutic benefit, for example, in Alzheimer’s disease (Koliatsos et al., 2006) or temporal lobe epilepsy (Krook-Magnuson et al., 2013).\n\n\n', {'entities': [(292, 314, 'FUNCTION'), (207, 226, 'FUNCTION'), (77, 82, 'PHYSIO'), (187, 192, 'PHYSIO')]}),
    ('Results: Total 282 patients were included.', {'entities': []}),
    ('DISCUSSION: Obtaining a thorough social history of environmental and dietary exposure to pigs is essential in the diagnosis of Yersinia enterocolitica given the nature of this bacterium.', {'entities': []}),
    ('CASE: A 61-year-old male, with history of hypertension, was brought to the emergency department by his co-workers when he was found to be unresponsive at work.', {'entities': []}),
    ('Initial WBC was >100,000/mm3 in 35 (17.6%), 50,000‐100,000/mm3 in 14 (7%) and 47 (23.7%) had 10,000‐50,000/mm3.', {'entities': []}),
    ('RESULTS: We found a high level of inconsistency in the functionality of the CPOE systems evaluated, both within and across systems.', {'entities': []}),
    ("Patients' characteristics, treatment regimen, steroids cumulative dose and treatment modalities of AVN were analyzed.\n\n", {'entities': []}),
    ('RESULTS: 41 residents received the ACP curriculum.', {'entities': []}),
    ('The age at presentation, type of vascular tumors and malformations {International Society for the Study of Vascuar Anomalies (ISSVA) Classification), associated abnormalities, treatment options and outcome were reviewed.', {'entities': [(33, 48, 'CELLTYPE')]}),
    ('Nerve impingement, progressive pain and headaches are common symptoms.', {'entities': [(0, 17, 'FUNCTION'), (19, 35, 'FUNCTION'), (40, 49, 'FUNCTION')]}),
    ('Curricula such as ours may ultimately make this time safer and improve health outcomes.', {'entities': []}),
    ('METHODS: The intervention lasted 4\xa0months.', {'entities': []}),
    ('At lower doses (weekly doses of 7.5 to 25\xa0mg), it is commonly used for treatment of rheumatoid arthritis, psoriasis, systemic lupus erythematous, crohn’s, ectopic pregnancy, multiple sclerosis and many others.', {'entities': [(71, 104, 'FUNCTION'), (117, 144, 'FUNCTION'), (174, 192, 'FUNCTION'), (155, 172, 'FUNCTION'), (106, 115, 'FUNCTION'), (146, 153, 'FUNCTION')]}),
    ('Prior functional studies have indicated that the NAcMS received glutamatergic direct inputs from ILA, BLA, and SUB, while received direct GABAergic inputs from ZI (Castro and Bruchas, 2019), which is in accordance with our mapping results.', {'entities': [(164, 182, 'CITATION'), (64, 77, 'NEUROTRANSMITTER'), (138, 147, 'NEUROTRANSMITTER'), (49, 54, 'REGION'), (97, 100, 'REGION'), (102, 105, 'REGION'), (111, 114, 'REGION'), (160, 162, 'REGION')]}),
    ('This process appears to depend on the involvement of genes such as Per2, which typically is involved in maintaining the normal daily rhythm (i.e., the circadian clock) of an organism (Spanagel et al. 2005).', {'entities': [(104, 139, 'FUNCTION'), (184, 204, 'CITATION'), (151, 166, 'FUNCTION'), (67, 71, 'PHYSIO')]}),
    ('DISCUSSION: Most patients with intestinal ascariasis are asymptomatic, hence it can be undetected for years until they develop some symptoms (1,2).', {'entities': []}),
    ('Among patients with Rituximab as initial therapy 15 had LDH>1000U/L, 1 had LDH>500 U/L, 1 < 500U/L. Three patients experienced relapse and died.', {'entities': []}),
    ('Further benefits can include better patient satisfaction, improved patient outcomes and streamlined hospital throughput.', {'entities': []}),
    ('On postop day 52 (4\xa0days after completing steroid therapy), he again presented to the hospital with similar complaints of severe dyspnea with high oxygen requirements.', {'entities': []}),
    ('A very small proportion of deceased PBT patients have autopsies and efforts should be made to increase this number.\n\n', {'entities': []}),
    ('MEASURES OF SUCCESS (DISCUSS QUALITATIVE AND/OR QUANTITATIVE METRICS WHICH WILL BE USED TO EVALUATE PROGRAM/INTERVENTION): We measured the number of consults received, time spent for consults, and nature of referral questions.', {'entities': []}),
    ("These combined results confirmed histiocytes are non‐Langerhan's cells.", {'entities': [(49, 70, 'CELLTYPE'), (33, 44, 'CELLTYPE')]}),
    ('RESULTS: Of 171 surveys sent, data were collected from 149 respondents (87\xa0% response).', {'entities': []}),
    ('The overall survival was 68% at 5 years.', {'entities': []}),
    ("Results: From the 1960s to present a more focused, organized and proactive approach has been taken by medical and psycho social teams to provide 'cure of the whole child.'", {'entities': []}),
    ('The goals of this study were to develop a physician scorecard for diabetes management and evaluate the ability of this scorecard to identify physicians who are performing better or worse than expected after accounting for relevant patient characteristics.\n\n', {'entities': []}),
    ('Median duration of symptoms prior to treatment was 12 months (range 1‐96 months).', {'entities': []}),
    ('Leukapheresis was done in 4 patients, one of whom expired.', {'entities': []}),
    ('Table 5.29Regulation of RBP4 production in human adipocytes (Source: [976]; ↑ increase, ↓ decrease)The adipokine and plasmatic retinol carrier RBP4 tethers to plasmalemmal receptors in addition to retinoic acid receptors NR1b1 to NR1b3 and NR2b1 to NR2b3.', {'entities': [(117, 142, 'FUNCTION'), (197, 220, 'PHYSIO'), (159, 181, 'PHYSIO'), (49, 59, 'CELLTYPE'), (103, 112, 'PHYSIO'), (221, 226, 'PHYSIO'), (230, 235, 'PHYSIO'), (240, 245, 'PHYSIO'), (249, 254, 'PHYSIO'), (24, 28, 'PHYSIO'), (143, 147, 'PHYSIO')]}),
    ('These data suggest that, during alert rest, the collective activities (and thus, outputs) of arkypallidal and prototypic GPe neurons are profoundly different.', {'entities': [(121, 132, 'CELLTYPE')]}),
    ('α-conotoxin MII (α-CTx-MII) and MII [H9A; L15A] were synthesized30.Data Analysis and Statistics\nBaseline electrophysiological data were recorded for 5–10\u2009min, before drug superfusion and during the washout.', {'entities': [(0, 15, 'PHYSIO'), (17, 26, 'PHYSIO')]}),
    ('Regardless of the difference in reward responses of individual neurons, Pavlovian conditioning only induces inhibition to reward-predicting cues, supporting the hypothesis that LHb neurons encode negative motivational value.', {'entities': [(108, 144, 'FUNCTION'), (189, 223, 'FUNCTION'), (72, 94, 'FUNCTION'), (32, 48, 'FUNCTION'), (177, 188, 'CELLTYPE'), (63, 70, 'CELLTYPE')]}),
    ('Ghrelin may play a role in epilepsy, but some of the current data are conflicting.', {'entities': [(27, 35, 'FUNCTION'), (0, 7, 'PHYSIO')]}),
    ('This group also found that photo-stimulation of lateral habenula drives behavioral despair and anhedonia, which is blocked by inhibiting the NMDA bursting activity effects on monoaminergic reward centers (35).', {'entities': [(65, 104, 'FUNCTION'), (48, 64, 'REGION'), (189, 203, 'REGION'), (175, 188, 'NEUROTRANSMITTER'), (141, 145, 'PHYSIO')]}),
    ('Nicotine 0.1, 0.5, and 1 mg/kg groups revealed 7, 12 and 4 different T-patterns, respectively.', {'entities': [(0, 8, 'PHYSIO')]}),
    ('Thus, the sex differences in the relative number of DA neurons in these areas may have functional implications in terms of connectivity and integration between cortical and subcortical processing.', {'entities': [(160, 195, 'FUNCTION'), (52, 62, 'CELLTYPE')]}),
    ('Furthermore, in an experiment examining the co-registration of noxious-evoked ensemble unit activities in the S1 and ACC of behaving rats, a single dose of morphine intraperitoneally suppressed the long latency response in the S1 and significantly attenuated early and late responses in the ACC [26].', {'entities': [(183, 219, 'FUNCTION'), (248, 283, 'FUNCTION'), (156, 164, 'PHYSIO'), (117, 120, 'REGION'), (291, 294, 'REGION'), (110, 112, 'REGION'), (227, 229, 'REGION')]}),
    ('The combined action of hypothalamic Y1 and Y5 receptors in the PVN, DMH, and VMH mediates hyperphagia [1018].240In the hypothalamus, insulin and leptin decrease anabolic (pro-feeding) and increase catabolic neuropeptides, whereas ghrelin has opposite effects [1019].', {'entities': [(188, 220, 'FUNCTION'), (77, 101, 'FUNCTION'), (242, 258, 'FUNCTION'), (43, 55, 'PHYSIO'), (119, 131, 'REGION'), (133, 140, 'PHYSIO'), (230, 237, 'PHYSIO'), (145, 151, 'PHYSIO'), (63, 66, 'REGION'), (68, 71, 'REGION'), (36, 38, 'PHYSIO')]}),
    ('Furthermore, increased self-stimulation of mice expressing ChR2:YFP PV positive VP neurons was also associated with increased activity in VTA neurons (Faget et al., 2018).', {'entities': [(68, 90, 'CELLTYPE'), (116, 134, 'FUNCTION'), (138, 149, 'CELLTYPE')]}),
    ('Other studies in humans, however, report no sex differences in basal DA concentrations, which is also consistent with the preclinical data (i.e., sex differences only during certain phases of the reproductive cycle).\n', {'entities': [(69, 71, 'NEUROTRANSMITTER')]}),
    ('For example, we identified that tdTom mRNA in the LHb, the BLP, the PMH, and the RMN colocalized with Vglut2 mRNA, while in the MePD and the lateral septum, tdTom mRNA showed substantial overlap with Gad1 mRNA.', {'entities': [(141, 155, 'REGION'), (102, 113, 'PHYSIO'), (32, 42, 'PHYSIO'), (157, 167, 'PHYSIO'), (200, 209, 'PHYSIO'), (128, 132, 'REGION'), (50, 53, 'REGION'), (59, 62, 'REGION'), (68, 71, 'REGION'), (81, 84, 'REGION')]}),
    ('administration of SB334867 did not exert such effects, thus confirming the results of a previous study (128) that found that intra-PVT SB334867 administration did not impact cue-induced COC-seeking behavior, thus suggesting a key role for OrxR2 signaling in the PVT in COC-seeking behavior.\n', {'entities': [(174, 206, 'FUNCTION'), (269, 289, 'FUNCTION'), (18, 26, 'PHYSIO'), (135, 143, 'PHYSIO'), (239, 244, 'PHYSIO'), (131, 134, 'REGION'), (262, 265, 'REGION')]}),
    ('Taken together, these findings are consistent with our behavioral data in which the reinforcing effects of nicotine, likely involving VTA activation, are substantially conserved in the knockout mice.', {'entities': [(84, 115, 'FUNCTION'), (134, 137, 'REGION')]}),
    ('In addition to the personal suffering of patients, the economic burden caused by anxiety disorders is heavy (Gustavsson et al., 2011).\n', {'entities': []}),
    ('Cancer worry has been shown to be an important barrier/facilitator in transition to long‐term followup care and also impacts psychosocial adjustment in survivors.', {'entities': []}),
    ('We surveyed primary care physicians (PCPs) in the Department of General Internal Medicine at our academic medical center 1\xa0year after inpatient EMR implementation to assess satisfaction with discharge communication and the desired content of communication at discharge.\n\n', {'entities': []}),
    ('One of the insightful studies demonstrated the effects of morphine (1 mg/ml, total volume of 60 nl) by a direct delivery into the VTA [71].', {'entities': [(58, 66, 'PHYSIO'), (130, 133, 'REGION')]}),
    ('C,D: SOM-labeled neurons in layers 1–3 of the PL/AC showed comparable increases in Fos-ir among the HFD feeding and exploring groups, but no differences between groups were apparent in the other parts of the mPFC, where about half of all SOM-labeled cells were Fos-positive.', {'entities': [(5, 24, 'CELLTYPE'), (238, 255, 'CELLTYPE'), (261, 273, 'PHYSIO'), (100, 111, 'PHYSIO'), (28, 38, 'REGION'), (83, 89, 'PHYSIO'), (208, 212, 'REGION'), (46, 48, 'REGION'), (49, 51, 'REGION')]}),
    ('The majority of students (75–99\xa0%) showed knowledge deficits in the remaining concepts tested.', {'entities': []}),
    ('The mice were housed under standard climate-controlled conditions on a 12 h light–dark cycle (lights on at 9:00 AM) with standard rodent chow (Harlan Teklad 7012, 3.10 kcal/g) and water available ad libitum.', {'entities': []}),
    ('Current pain was rated as 3.7/10 (SD = 2.1) and worst pain was rated as 5.5/10 (SD = 2.4).', {'entities': []}),
    ('Results: Case 1: The patient was diagnosed with posterior fossa ATRT at the age of three months.', {'entities': []}),
    ('With decreases in length of inpatient stays, patients are being discharged with more complex follow-up needs, highlighting the need for effective communication with outpatient providers.', {'entities': []}),
    ('Eventually her fever and headache resolved and her mental status improved markedly.', {'entities': []}),
    ('There were total of 19 (33.9%) transplant related mortalities of which 6 (31.5%) were attributable to infections.\n\n', {'entities': []}),
    ('Faculty expressed significant tension over the evaluation process.', {'entities': []}),
    ('1Brigham and Women, Boston, MA; 2Harvard Medical School, Boston, MA.', {'entities': []}),
    ('Their contents increase when mussels are extracted 24 h post-mortem, but remain unaffected by boiling the tissue prior to extraction.\n\n\n', {'entities': []}),
    ('U50,488H, a κ receptors agonist, suppresses staphylococcal enterotoxin B induced proliferation of T lymphocytes and IL-2 production in vitro.', {'entities': [(33, 94, 'FUNCTION'), (12, 31, 'PHYSIO'), (116, 131, 'FUNCTION'), (98, 111, 'CELLTYPE'), (4, 8, 'PHYSIO'), (0, 3, 'PHYSIO')]}),
    ('This may explain the greater sensitivity of the Orx system to OrxR antagonism for drug-seeking behavior vs. natural reward-seeking behavior (66) and could explain why transient inactivation of the PVT prevented COC conditioned reinstatement and not behavior that was motivated by stimuli that were paired with a highly palatable food (123, 126).', {'entities': [(201, 240, 'FUNCTION'), (108, 139, 'FUNCTION'), (82, 103, 'FUNCTION'), (62, 66, 'PHYSIO'), (48, 51, 'PHYSIO'), (197, 200, 'REGION')]}),
    ('The enkephalin-producing neurons are distributed widely throughout the brain, with the highest concentrations found in the nucleus accumbens (NAc) and the hypothalamus.', {'entities': [(4, 32, 'CELLTYPE'), (123, 140, 'REGION'), (155, 167, 'REGION'), (71, 76, 'REGION'), (142, 145, 'REGION')]}),
    ('In the InfS, SP may either influence the KP and NKB secretory output via autocrine/paracrine mechanisms or regulate GnRH neurosecretion directly.', {'entities': [(27, 68, 'FUNCTION'), (107, 144, 'FUNCTION'), (7, 11, 'REGION'), (13, 15, 'PHYSIO')]}),
    ('Recently, it has been demonstrated that MHb firing rate alters the neurotransmitter system used by the vMHb; tonic firing appears to engage glutamatergic transmission, while high‐rate phasic firing drives acetylcholine release (Ren et al. 2011).', {'entities': [(228, 243, 'CITATION'), (140, 153, 'NEUROTRANSMITTER'), (205, 218, 'NEUROTRANSMITTER'), (103, 107, 'REGION'), (40, 43, 'REGION')]}),
    ('Thus, it is evident that the LHb occupies a key position among pathways involved in the transmission of information concerning emotional processes (limbic input) and motor behavior decision-making processes (basal ganglia input).', {'entities': [(88, 146, 'FUNCTION'), (166, 206, 'FUNCTION'), (208, 221, 'REGION'), (148, 154, 'REGION'), (29, 32, 'REGION')]}),
    ('The brain was dissected, post-fixed for 4 hr at 4°C, and cryoprotected overnight in 30% sucrose in PBS.', {'entities': [(4, 9, 'REGION')]}),
    ('Reduced GABA release in the VP occurs during reinstated cocaine seeking, and this process likely disinhibits VP neurons (Tang et al., 2005).', {'entities': [(45, 71, 'FUNCTION'), (97, 108, 'FUNCTION'), (109, 119, 'CELLTYPE'), (8, 12, 'NEUROTRANSMITTER'), (28, 30, 'REGION')]}),
    ('However, evidence for phenotypically patent (i.e., VGAT-positive) GABAergic neurons in this region has been incomplete38.\n', {'entities': [(66, 83, 'CELLTYPE'), (51, 64, 'CELLTYPE')]}),
    ('In addition, we want to suggest that anteromedial division of the bed nucleus of the stria terminalis contains the human limbic equivalent of the lamprey habenula-projecting globus pallidus (GPh).', {'entities': [(37, 101, 'REGION'), (174, 189, 'REGION'), (154, 162, 'REGION'), (191, 194, 'REGION')]}),
    ('However, there still remain uncharacterized hypothalamic regions.', {'entities': [(44, 64, 'REGION')]}),
    ('The opioid peptides also serve as neuromodulators and the opioid regulation of dopaminergic pathways (Christensson-Nylander et al., 1986; Spanagel et al., 1992; Steiner and Gerfen, 1998) is of special interest with respect to drug reward, reinforcement, and addiction.', {'entities': [(161, 179, 'CITATION'), (58, 75, 'FUNCTION'), (4, 19, 'PHYSIO'), (34, 49, 'FUNCTION'), (239, 252, 'FUNCTION'), (79, 91, 'NEUROTRANSMITTER'), (226, 237, 'FUNCTION'), (258, 267, 'FUNCTION')]}),
    ('ENK neurons are found among the entorhinal, piriform, and medial prefrontal cortex (mPFC, infralimbic and prelimbic).', {'entities': [(58, 82, 'REGION'), (0, 11, 'CELLTYPE'), (90, 101, 'REGION'), (32, 42, 'REGION'), (106, 115, 'REGION'), (44, 52, 'REGION'), (84, 88, 'REGION')]}),
    ('However, more recent experiments have shown that the role of dopamine in reward is more complex than simple stimulus-response.', {'entities': [(61, 69, 'NEUROTRANSMITTER'), (73, 79, 'FUNCTION')]}),
    ('Similarly, internalization of μ receptors was previously considered as a neural mechanism underlying morphine tolerance.', {'entities': [(30, 41, 'PHYSIO'), (110, 119, 'FUNCTION'), (101, 109, 'PHYSIO')]}),
    ('Increased βCaMKII expression was also detected in glutamatergic LHb neurons (Seo et al., 2018).\n', {'entities': [(50, 75, 'CELLTYPE'), (10, 17, 'PHYSIO')]}),
    ('After twelve months of treatment with intrathecal morphine in patient group, there was an increase in μ opioid receptor (MOR) mRNA levels in T lymphocytes (also in B lymphocytes).', {'entities': [(102, 119, 'PHYSIO'), (141, 154, 'CELLTYPE'), (164, 177, 'CELLTYPE'), (50, 58, 'PHYSIO'), (121, 124, 'PHYSIO')]}),
    ('To determine whether the opioid-sensitive population of thalamic neurons in mouse project to both the ACC and DMS, two approaches were used.', {'entities': [(56, 72, 'CELLTYPE'), (25, 31, 'PHYSIO'), (102, 105, 'REGION'), (110, 113, 'REGION')]}),
    ('First, we examined whether engagement of Gq‐coupled signaling increases firing of MHb ChAT expressing neurons.', {'entities': [(82, 109, 'CELLTYPE'), (41, 61, 'PHYSIO'), (62, 78, 'FUNCTION')]}),
    ('Whereas antagonism of nAChR (mecamyline) reduces cue-induced cocaine craving in dependent subjects [417].Sex differences\nThe preceding descriptions of cholinergic function in the striatum have largely been derived from research in males.', {'entities': [(41, 76, 'FUNCTION'), (151, 162, 'NEUROTRANSMITTER'), (29, 39, 'PHYSIO'), (179, 187, 'REGION'), (22, 27, 'PHYSIO')]}),
    ('This was to be expected, as the proper routing of hippocampal information and functional segregation of neuronal ensembles (Buzsaki and Chrobak, 1995) require strong coordination of the inhibition.', {'entities': [(89, 122, 'FUNCTION'), (124, 143, 'CITATION'), (50, 61, 'REGION')]}),
    ('The present study used optogenetic tools to target and reversibly silence LHb pyramidal neurons with high temporal specificity (Gradinaru et al., 2010), which enabled real-time manipulation of LHb activity only during the tailshock itself while performing simultaneous microdialysis in the BLA, a downstream circuit element that is critical for the expression of IS-induced anxiety-like behavior (Christianson et al., 2010).', {'entities': [(349, 395, 'FUNCTION'), (74, 95, 'CELLTYPE'), (193, 196, 'REGION'), (290, 293, 'REGION')]}),
    ('We examined the two major cell types in a context- and cue-induced cocaine-seeking paradigm, VPGABA neurons (73% of all neurons) and VPGlu neurons (23%), as well as a subpopulation of VPGABA neurons co-expressing proenkephalin (16%).', {'entities': [(42, 82, 'FUNCTION'), (93, 107, 'CELLTYPE'), (184, 198, 'CELLTYPE'), (133, 146, 'CELLTYPE'), (213, 226, 'PHYSIO')]}),
    ('For example, the nucleus reuniens receives input from the prefrontal cortex and relays it to the hippocampus (Ito et al. 2015; Hallock et al. 2016).', {'entities': [(127, 146, 'CITATION'), (58, 75, 'REGION'), (17, 33, 'REGION'), (110, 125, 'CITATION'), (97, 108, 'REGION')]}),
    ('Despite this evidence, the function, subterritorial expression and behavioral relevance of discrete 5-HT receptors within the LHb remain vague.', {'entities': [(100, 114, 'PHYSIO'), (126, 129, 'REGION')]}),
    ('NPS treatment also rescues deficient extinction learning in hyperanxious rats (Slattery et al., in press), exhibiting aberrant cortico-AMY activation (Muigg et al., 2008).', {'entities': [(19, 56, 'FUNCTION'), (127, 138, 'REGION'), (0, 3, 'PHYSIO')]}),
    ('Examining loss-of-function in the LHb shows that inhibiting LHb function with habenular lesions in rats impairs their ability to recognize or learn newly introduced escape routes in a forced swim test (Thornton et al., 1985), and also impairs their ability to learn to avoid a foot shock during an active avoidance task (Thornton and Bradbury, 1989).', {'entities': [(104, 147, 'FUNCTION'), (298, 319, 'FUNCTION'), (321, 342, 'CITATION'), (184, 200, 'FUNCTION'), (34, 37, 'REGION'), (60, 63, 'REGION')]}),
    ('Previous preclinical studies in nearly all animal studies, including species from zebra fish up to higher primates, have already linked the MHb–interpeduncular nucleus (IPN) cholinergic pathway to anxiety, fear, and nicotine addiction36–38.', {'entities': [(144, 167, 'REGION'), (174, 185, 'NEUROTRANSMITTER'), (197, 204, 'FUNCTION'), (206, 210, 'FUNCTION'), (140, 143, 'REGION'), (169, 172, 'REGION')]}),
    ('Based on these findings we focused our further analysis on the subpopulation of information-predictive neurons, with the goal of testing whether they continued to encode IPEs throughout the behavioral task (for the remaining neurons, see Supplementary Figs. 6,7).Coding of unpredicted denial of reward information\nAccording to our hypothesis, lateral habenula neurons should encode negative IPEs when reward information is unexpectedly denied.', {'entities': [(80, 110, 'CELLTYPE'), (343, 367, 'CELLTYPE'), (375, 395, 'FUNCTION'), (163, 174, 'FUNCTION')]}),
    ('Fasting and HFD decreases and increases AdCyAP1 synthesis in VMH, respectively.\n', {'entities': [(30, 57, 'FUNCTION'), (0, 7, 'PHYSIO'), (12, 15, 'PHYSIO'), (61, 64, 'REGION')]}),
    ('Understanding this could suggest that meditation coupled with enhance spiritual belief may indeed induce DA release at the VTA and cingulate gyrus that could translate to better clinical outcomes and reduced relapse [80, 81].\n', {'entities': [(131, 146, 'REGION'), (123, 126, 'REGION'), (105, 107, 'NEUROTRANSMITTER')]}),
    ('As required by the idea that DRN 5-HT activation is critical in mediating the consequences of IS, exactly equal amounts of ES do not produce DRN activation or behavioral changes typically associated with DRN activation (Maswood et al., 1998).', {'entities': [(64, 96, 'FUNCTION'), (33, 37, 'NEUROTRANSMITTER'), (29, 32, 'REGION'), (141, 144, 'REGION'), (204, 207, 'REGION')]}),
    ('Because these regions are devoid of GnRH-immunoreactive (IR) somata, type-III GnRH neurons are unlikely to fully process the prohormone to the mature GnRH decapeptide and their role, if any, in reproduction is questionable.', {'entities': [(113, 135, 'FUNCTION'), (69, 90, 'CELLTYPE'), (150, 166, 'PHYSIO'), (36, 40, 'PHYSIO')]}),
    ('The effect of T4 on Trhde depends on the local conversion of T4 to T3 by deiodinase 2 (Dio2) also expressed in tanycytes (Marsili et al., 2011).', {'entities': [(73, 85, 'PHYSIO'), (111, 120, 'CELLTYPE'), (20, 25, 'PHYSIO'), (87, 91, 'PHYSIO'), (14, 16, 'PHYSIO'), (61, 63, 'PHYSIO'), (67, 69, 'PHYSIO')]}),
    ('Future experiments using similar temporally specific activation or inhibition strategies in VP subpopulations during operant drug-seeking responses could further elucidate a more precise role for these cells and their projections during drug seeking.\n', {'entities': [(117, 147, 'FUNCTION'), (237, 249, 'FUNCTION'), (92, 94, 'REGION')]}),
    ('Secretin stimulates the dorsal division of the parvocellular neurons of the PVN, which are involved in the control of central autonomic outflow.246 In addition, central and peripheral secretin upregulates synthesis of the melanocortin receptor MC4 in the PVN, which supports secretin action.', {'entities': [(107, 143, 'FUNCTION'), (222, 247, 'PHYSIO'), (266, 290, 'FUNCTION'), (47, 68, 'CELLTYPE'), (193, 214, 'FUNCTION'), (184, 192, 'PHYSIO'), (76, 79, 'REGION'), (255, 258, 'REGION')]}),
    ('Some VMN neurons project axons to the MCG, and neural projections from the VMN to MCG are an important part of the neural circuitry underlying lordosis (Daniels et al., 1999).', {'entities': [(115, 151, 'FUNCTION'), (5, 8, 'REGION'), (38, 41, 'REGION'), (75, 78, 'REGION'), (82, 85, 'REGION')]}),
    ('Thus, their upregulation in the neuropathic pain model used in our experiments cannot be attributed to the decreased dopaminergic tone.\n', {'entities': [(32, 48, 'FUNCTION'), (117, 129, 'NEUROTRANSMITTER')]}),
    ('Indeed, a combination of paired recordings and post-hoc anatomical reconstruction in acute hippocampal slices showed that, in addition to being connected with each other, BCs form synapses onto trilaminar cells (Ali et al., 1999).', {'entities': [(194, 210, 'CELLTYPE'), (91, 102, 'REGION'), (171, 174, 'CELLTYPE')]}),
    ('It is conceivable that at mixed GABA-Glu synapses, the ratio of Glu over GABA co-released from these cells depends on the strengths and frequency of varied input stimulations [44, 141, 189].', {'entities': [(32, 36, 'NEUROTRANSMITTER'), (73, 77, 'NEUROTRANSMITTER'), (37, 40, 'NEUROTRANSMITTER'), (64, 67, 'NEUROTRANSMITTER')]}),
    ('Indeed, as neurons in both habenulae respond to odors (Dreosti et al., 2014; Jetti et al., 2014; Okamoto, 2014) there must be routes, other than via direct mitral cell innervation, for such sensory input to reach the habenulae.', {'entities': [(37, 53, 'FUNCTION'), (156, 167, 'CELLTYPE'), (27, 36, 'REGION'), (217, 226, 'REGION'), (11, 18, 'CELLTYPE'), (97, 104, 'CITATION')]}),
    ('Augmented NR3c2 activation in obesity can result from: (1) adipocyte production of aldosterone and aldosterone secretagogues, (2) increased NR3c2 synthesis, and (3) altered activity of NR3c2-interacting proteins [825].\n', {'entities': [(185, 211, 'PHYSIO'), (69, 94, 'FUNCTION'), (59, 68, 'CELLTYPE'), (10, 15, 'PHYSIO'), (140, 145, 'PHYSIO')]}),
    ('Twenty four hours after photoconversion, most red Kaede cells maintain their positions within the diencephalon and do not expand into the telencephalon (F).', {'entities': [(138, 151, 'REGION'), (98, 110, 'REGION'), (50, 61, 'CELLTYPE')]}),
    ('The two nonapeptides are not only secreted from the neurohypophysis into the general circulation, but - probably upon some specific stimuli, and largely independently of their peripheral release - are also released intracerebrally (e.g. into septum).', {'entities': [(52, 67, 'REGION'), (8, 20, 'PHYSIO'), (242, 248, 'REGION')]}),
    ('AcbSh injection of CART decreases both regular and AcbSh muscimol-elicited food intake, and CART mRNA levels are decreased within the medial pfLH during fasting (Yang et al., 2005), suggesting that the pfLH may secrete CART to the AcbSh to suppress feeding.', {'entities': [(57, 86, 'FUNCTION'), (240, 256, 'FUNCTION'), (134, 145, 'REGION'), (92, 101, 'PHYSIO'), (0, 5, 'REGION'), (51, 56, 'REGION'), (231, 236, 'REGION'), (19, 23, 'PHYSIO'), (219, 223, 'PHYSIO')]}),
    ('LHA-LHb and Feeding\nAn interesting area of reward-related connection to the LHb is the LHA, which is implicated in feeding and reinforcement processes (Jennings et al., 2013).', {'entities': [(115, 150, 'FUNCTION'), (43, 68, 'FUNCTION'), (0, 3, 'REGION'), (4, 7, 'REGION'), (76, 79, 'REGION'), (87, 90, 'REGION')]}),
    ('In addition, somatostatin decreases ghrelin O-acyl transferase expression, an enzyme that catalyzes the acylation of ghrelin [55].', {'entities': [(26, 73, 'FUNCTION'), (90, 124, 'FUNCTION'), (13, 25, 'PHYSIO')]}),
    ('However, we also find that LH→LHb neurons directly synapse onto 5HT and DA neurons.', {'entities': [(42, 67, 'FUNCTION'), (27, 41, 'CELLTYPE'), (72, 82, 'CELLTYPE')]}),
    ('Both resistin and melanocortin agonists may influence AT 11β HSD1, which converts inactive into active glucocorticoids, thereby favoring obesity and insulin resistance.', {'entities': [(73, 118, 'FUNCTION'), (137, 167, 'FUNCTION'), (18, 39, 'PHYSIO'), (44, 65, 'FUNCTION'), (5, 13, 'PHYSIO')]}),
    ('Oscillatory activity was induced in CA1 minislices by adding the cholinergic receptor agonist carbachol (5 μM) to the aCSF (Pietersen et al., 2014).', {'entities': [(77, 93, 'PHYSIO'), (65, 76, 'NEUROTRANSMITTER'), (94, 103, 'PHYSIO'), (36, 39, 'REGION')]}),
    ('The medial habenula also has a very high level of opioid receptors (Gardon et al., 2014) and has been implicated in aversion, withdrawal, and negative affect (Salas et al., 2009; Baldwin et al., 2011; Frahm et al., 2011; Koppensteiner et al., 2017; Molas et al., 2017).', {'entities': [(50, 66, 'PHYSIO'), (4, 19, 'REGION'), (142, 157, 'FUNCTION'), (126, 136, 'FUNCTION'), (116, 124, 'FUNCTION')]}),
    ('Consequently, dorsally, GFP expression is likely located within derivatives of the prethalamus and prethalamic eminence (Figure 5C; the prethalamic eminence has also been named as thalamic eminence or eminentia thalami; see Wullimann and Mueller, 2004; Puelles, 2007; Mueller and Guo, 2009).', {'entities': [(224, 245, 'CITATION'), (99, 119, 'REGION'), (136, 156, 'REGION'), (180, 197, 'REGION'), (201, 218, 'REGION'), (268, 283, 'CITATION'), (83, 94, 'REGION'), (253, 260, 'CITATION'), (24, 27, 'PHYSIO')]}),
    ('One of them (single arrows in A,C) is retrogradely labeled after hippocampal fluorogold injection (FG).', {'entities': [(65, 76, 'REGION'), (77, 87, 'PHYSIO'), (99, 101, 'PHYSIO')]}),
    ('Cytotoxic CD8+ T lymphocytes secrete TNFSF1, IL2, Ifnγ, and CCL5; CD4+ TH1 cells TNFSF1, IL12, and INFγ, these cytokines affecting adipocyte function and favoring the M1 macrophage phenotype.', {'entities': [(154, 190, 'FUNCTION'), (121, 149, 'FUNCTION'), (37, 43, 'PHYSIO'), (81, 87, 'PHYSIO'), (50, 54, 'PHYSIO'), (60, 64, 'PHYSIO'), (89, 93, 'PHYSIO'), (99, 103, 'PHYSIO'), (45, 48, 'PHYSIO')]}),
    ('The 6- to 8-week study duration involved a total of nine visits, each on different days (one orientation, two neurocognitive, and six neuroimaging visits; Fig. 1A) (15, 22, 62, 64, 85).', {'entities': []}),
    ('A strong glutamatergic projection from the lateral habenula (LHb) to DRN has been noted in many studies (Aghajanian and Wang, 1977; Kalén et al., 1985; Araki et al., 1988; Sego et al., 2014).', {'entities': [(43, 59, 'REGION'), (9, 22, 'NEUROTRANSMITTER'), (61, 64, 'REGION'), (69, 72, 'REGION')]}),
    ('Future studies could involve directly evaluating and manipulating miRNAs to determine the relative importance of miRNAs in producing a maternal brain.10.1371/journal.pone.0038602.g002\nFigure 2Schematic representation of the brain regions (boxed areas) dissected for gene array analysis.\n', {'entities': [(123, 149, 'FUNCTION'), (66, 72, 'PHYSIO'), (113, 119, 'PHYSIO')]}),
    ('Second, it is known that the Hb can be further divided into the medial and lateral nuclei that have different inputs/outputs and different functions [Lecca et al., 2014; Viswanath et al., 2014].', {'entities': [(64, 89, 'REGION'), (29, 31, 'REGION')]}),
    ('The authors suggested that such reduced density of brain 5-HTT may reflect a deficit of neuronal 5-HT, or a compensatory process in the 5-HT system attempting to increase the availability of synaptic 5-HT.', {'entities': [(88, 96, 'CELLTYPE'), (51, 56, 'REGION'), (57, 62, 'PHYSIO'), (97, 101, 'NEUROTRANSMITTER'), (136, 140, 'NEUROTRANSMITTER'), (200, 204, 'NEUROTRANSMITTER')]}),
    ('Light stimulation of voltage-clamped eNpHR-eYFP-positive neurons in MHb slices from eNpHR-eYFP-infected ChAT-cre mice elicited outward currents at a holding potential of −70 mV under voltage clamp and hyperpolarization under current clamp, dramatically silencing action potential firing (Supplementary Fig. 7b), confirming that eNpHR-eYFP was expressed and functional in MHb cholinergic neurons.\n', {'entities': [(253, 286, 'FUNCTION'), (37, 64, 'CELLTYPE'), (118, 143, 'FUNCTION'), (371, 394, 'CELLTYPE'), (104, 112, 'PHYSIO'), (68, 71, 'REGION')]}),
    ('In contrast, a certain neuronal population of PeFAH responded to these psychological stressors and showed an increase in c-Fos expression.', {'entities': [(23, 42, 'CELLTYPE'), (46, 51, 'REGION'), (121, 126, 'PHYSIO')]}),
    ('Furthermore, systemic administration of DA and glucocorticoid receptor antagonists was sufficient to block stress induced reductions in GABAB-GIRK currents (Lecca et al., 2017).', {'entities': [(101, 155, 'FUNCTION'), (47, 82, 'PHYSIO'), (40, 42, 'NEUROTRANSMITTER')]}),
    ('White adipocytes store energy, whereas brown adipocytes dissipate energy, converting chemical energy into heat for thermoregulation.', {'entities': [(0, 16, 'CELLTYPE'), (39, 55, 'CELLTYPE'), (56, 72, 'FUNCTION'), (17, 29, 'FUNCTION')]}),
    ('Interestingly, analysis indicated that the volume changes of MHb decreased remarkably in the caudal region for the LPS-injected mice compared to rostral and middle regions (Fig. 5E).', {'entities': [(145, 171, 'REGION'), (93, 106, 'REGION'), (61, 64, 'REGION')]}),
    ('In the presence of ACh, [3H]-glutamate accumulation increased to 51 ± 15 pmol of glutamate/mg of protein (Figure 10E).', {'entities': [(29, 38, 'NEUROTRANSMITTER'), (81, 90, 'NEUROTRANSMITTER'), (19, 22, 'NEUROTRANSMITTER')]}),
    ('Ultimately, each route by which LH subregions alter activity of the AcbSh and change food intake is subsequently re-directed back through the LH, as ablation or inhibition of the LH halts AcbSh-mediated feeding (Stratford and Wirtshafter, 2012b; Urstadt et al., 2013a).Indirect LH to Acb pathways\nConsidering the food-directed motivational and hedonic effects of GABA, glutamate, and peptide neurotransmission within the AcbSh, it is of much interest to determine the extra-accumbal sources of such input.', {'entities': [(182, 210, 'FUNCTION'), (313, 339, 'FUNCTION'), (212, 237, 'CITATION'), (78, 96, 'FUNCTION'), (468, 482, 'REGION'), (369, 378, 'NEUROTRANSMITTER'), (384, 391, 'NEUROTRANSMITTER'), (68, 73, 'REGION'), (421, 426, 'REGION'), (363, 367, 'NEUROTRANSMITTER'), (284, 287, 'REGION'), (32, 34, 'REGION'), (142, 144, 'REGION'), (179, 181, 'REGION'), (278, 280, 'REGION')]}),
    ('Moreover, Group II and III mGluRs can be located on adjacent neurons releasing the neurotransmitter GABA and help regulate the actions of those neurons (Schoepp 2001).', {'entities': [(114, 151, 'FUNCTION'), (10, 33, 'PHYSIO'), (153, 165, 'CITATION'), (61, 68, 'CELLTYPE'), (100, 104, 'NEUROTRANSMITTER')]}),
    ("They also exert opposing effects in the VTA (181, 182), such as opposing actions on VTA neuronal firing rate, in which they counteract each other's effects upon co-release (181).", {'entities': [(124, 171, 'FUNCTION'), (84, 108, 'FUNCTION'), (10, 32, 'FUNCTION'), (40, 43, 'REGION')]}),

]
