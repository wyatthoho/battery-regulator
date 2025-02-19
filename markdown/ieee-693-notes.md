# Notes of IEEE 693

## Objective

The objective is to secure substation equipment that will have no 
***significant damage*** and maintain electrical functionality at
normal operating conditions during and after a seismic event.
Some damage is tolerated, provided that it is not significant
structural damage.

Significant damage is defined as follows:

- ***Failure to maintain fuctionality***: The equipment ceases to 
  perform its primary electrical function.
- ***Excess yielding or fracture***: The equipment has a possibility 
  of imminent collapse at nominal electric operating conditions.

It is important to realize that ***yielding is permitted*** provided
that it does not impair electrical functionality or pose a risk of
imminent collapse. ***Fracture*** of a component is considered 
significant damage.

## Levels

This recommended practice recognizes three seismic qualification 
levels: ***high***, ***moderate*** and ***low***. For the high 
qualification level, the horizontal zero period acceleration (ZPA) 
associated with the seismic qualification objective is ***1.0 g***.

The selection of seismic level for seismic qualification involves
risk management. The acceptance or aversion of risk can only
be judged by the user, thus the selection of seismic level should
only be done by users.

## Approaches

Two qualification approaches are defined herein:

- ***Performance level qualification approach***
- ***Design level qualification approach***

To help ensure uniformity of qualification procedurees for any specify
type of equipment, the seismic qualification approach is establiished
in each particular ***equipment annex***.

The seismic qualification objective permits ***yielding*** of 
components when subjected to performance level loading. However, 
all of the design level analytical qualification techniques assumes
a ***linear*** response.

As the ***performance level*** of equipment is often projected from tests
conducted at the ***design level*** or analyses, there is uncertainty as to 
the true performance level. To reduce the risks of unfavorable 
performance associated with this uncertainty, the user may wish
to assign the ***high qualificationn level*** to sites with a PGA
less than, but approaching, ***0.5 g***.

Ideally, all equipment would be qualified utilizing performance level testing; 
however, this may not always be possible for the reasons such as safety concerns,
serviceability concerns, financial concerns or test facility limitations.
Design level testing may be used unless performance level testing is required 
by this recommended practice.

## Response Spectra

The ***required response spectra (RRS)*** used in a performance level 
qualification corresponds to the "High Performance Level 
Response Spectrum" depicted in ***Figure A.1***.

![](../images/ieee-693-notes/required-response-spectrum-high.png)

The accelerations of the response spectra used for the design level
approach at the moderate and high seismic qualification levels are 
half of the performance level spectra at any given frequency and level 
of damping.

![](../images/ieee-693-notes/required-response-spectrum-moderate.png)

Irrespective of seismic qualification level or seismic qualification 
method, the spectrum shape is consistent. The spectra contained in 
this recommended practice are expected to be suitable for most 
substation site conditions; however, they may be inadequate when any of 
the following exceptional situations exists:

- Near field conditions
- Very soft soil sites
- Equipment in the upper floors of buildings
- Hill sites
- Subduction zone earthquakes
- ...

## Damping

A damping ratio of ***2%*** (damping) may be assumed for all design
level ***analysis***, while a value of ***5%*** is used to ***match*** 
the required response spectra (RRS). 

The damping for matching is used generically with establishing 
the sufficiency of time-history data used in conjuction with time 
history analysis and testing. It has been shown to be more 
conservative in comparison to matchinig at 2% damping.

Damping can either be assumed by any of the following methods:

- Measuring the decay rate
- Measuring the half-power bandwidth
- Curve fitting to frequency response methods
- Time domain curve fitting

## Qualification Procedures

The equipment should be ***tested*** or ***analyzed*** in its 
equivalent in-service configuration, including support structures.

The ***support structure*** must be designed for the seismic demand 
loads and dynamic characteristics of the combined equipment/support
structure. For equipment that is mounted on a support structure, 
the combined system may be qualified by one of the following:

- analyze and/or test the combined system
- using an analytically-derived, modified input motion that allows for 
  the effects of the support structure
- using a modified input motion (2.5 x RRS)

***Normal operating loads*** are to be considered to act simultaneously 
with ***seismic*** and ***dead loads***.

Terminal attachments representing the in-service configuration of 
the equipment ***terminal masses*** should be included:

- 500 kV and greater: 11 kg
- Greater than 145 kV to less than 500 kV: 7 kg

***Conductor loading*** shall be considered in the qualification of 
equipment by using either the moment amplification factor (MAF) or 
equivalent terminal force (ETF) methods. Depending on the situation, one 
of these methods might be more stringent than the other; the manufacturer 
may choose the one providing the lower increase in demand.

Analysis and time history testing shall be ***triaxial*** with 
simulation of ***translational ground accelerations*** in three directions. 
A test response spectrum that envelops the RRS shall be applied in the
two perpendicular horizontal axes together with a response spectrum 
in the vertical axis that shall have an acceleration of ***80%*** 
of that in the horizontal axes.

Using the design level ***seismic loads*** corresponding to 50% of the
performance level loading defined by the response spectra of Figure
A.1 for the high performance levels.

## Annex of Station Batteries and Battery Racks

The seismic withstand capability of battery racks shall demonstrated
as follows:

- Non-rigid racks of three or more stacks: By performance level 
  ***time history shake-table testing***
- Non-rigid racks of two stacks: By ***dynamic analysis***
- Rigid racks and all racks of one stack: By ***static analysis***

## Time History Shake-Table Test

Terminal masses shall be attached to conductor connection points
in accordance with A.1.2.3. Following time history test, perform
static pull test on the insulator element in accordance with
A.3.

The ***resonant frequency search test*** is for determing the 
resonant frequencies and low response level damping of equipment.
A ***sine sweep*** or ***random noise*** excitation test shall be 
used. A frequency search above ***33 Hz*** is not required. It is
suggested that amplitude of ***0.1 g*** be used.

***Theoretical motions*** refer to input motions developed by a 
variety of software packages and used as input to the shake table.
***Table output motions*** refer to motions that are measured from
instruments mounted on the shake-table platform.

The theoretical response spectrum developed for testing shall
envelop the RRS. When the high seismic level is specified, the
performance level spectra with 5% damping as shown in Figure A.1
shall be used. The theoretical response spectrum for testing shall 
be computed at 5% damping and shall include the lower corner
point frequency of the RRS (1.1 Hz).

The ***strong part ratio*** of a given record is defined as the 
ratio of the time required to accumulate from 25% to 75% of the 
total cumulative energy of the record, to the time required to 
accumulate from 5% to 95% of the total cumulative energy of the 
record.

## Static Analysis

The forces on each component of the equipment shall be obtained
by multiplying the values of the ***mass*** of the components
by the ***acceleration*** specified in the principal directions.

The vertical seismic forces shall act simultaneously with both
horizontal seismic forces. The three forces shall be using one of
the ***combination techniques*** in A.1.4.4.

When the ***high*** seismic level is specified, the static analysis 
shall use a ***design*** level load consisting of ***0.5 g*** in the
two horizontal directions and ***0.4 g*** in the vertical direction.

When the ***moderate*** seismic level is specified, the static analysis 
shall use a ***design*** level load consisting of ***0.25 g*** in the 
two horizontal directions and ***0.2 g*** in the vertical direction.


## Dynamic Response Spectrum Analysis

The finite element model shall be dynamically analyzed using a modal 
spectrum analysis. 

The total response of all modes in any direction shall be determined 
by combining all modal response components acting in that direction 
using the ***SRSS*** technique, except if the mode frequencies differ 
by less than 10% of the lower mode, then these closely spaced modes 
are added directly and these added modes and the remaining modes are 
added using the SRSS method. 

In lieu of the SRSS combination of three orthogonal earthquake 
components, a ***100/40/40*** combination rule may be used.

Alternatively, the total response in any direction may be determined 
by applying the ***CQC*** technique to all modal response components 
acting in that direction.

The acceptance criteria for establishing sufficiency in a particular 
direction shall be that the cumulative participating mass of the modes 
considered shall be at least ***90%*** of the sum of effective masses 
of all modes.

Should the finite element model have several resonant frequencies above 
33 Hz such that the attainment of the acceptance criteria in an orthogonal 
excitation direction is impractical (as is often the case with vertically 
stiff equipment), then the effects of the orthogonal inputs can be 
simulated as follows:

1. Determine the remaining effective mass in a given direction.
2. For each component, apply a static force equal to the mass of the 
   component times the percentage of mass missing times the design 
   level ZPA.
3. Calculate stresses, reactions, and other design parameters using 
   these forces.
4. For each direction, combine stresses, reactions, and other design 
   parameters from the dynamic analysis with those from the analysis 
   above using the SRSS.

When the high seismic level is specified, the design level spectrum equaling 
***50%*** of the performance level spectrum given in Figure A.1 shall be used. 

When the moderate seismic level is specified, the design level spectrum 
equaling ***50%*** of the performance level spectrum given in Figure A.2 shall 
be used.

A damping value of ***2%*** or less shall be used for dynamic analysis, unless 
a higher damping value is justified by one of the tests specified in A.1.1.6.

## Acceptance Criteria

### **Design Level Load Combinations**

Where appropriate this recommended practice recognizes both ***ASD***
and ***LRFD*** design methodologies. The load combinations to be used
for ASD and LRFD methods shall be as follows:

- \\(ASD = 1.0D + 1.0E_{DL} + 1.0OP\\)
- \\(ASD = 0.6D + 1.0E_{DL} + 1.0OP\\)
- \\(LRFD = 1.2D + 1.4E_{DL} + 1.0OP\\)
- \\(LRFD = 0.9D + 1.4E_{DL} + 1.0OP\\)

Use the more critical of the two equations, where:

- \\(D\\) is the dead load
- \\(E_{DL}\\) is the earthquake load demand from the design level spectra
- \\(OP\\) is the normal operating load

### **Design Level Allowable Strength/Stress**

The total load/stresses found shall not exceed the allowable 
load/stresses. Allowable load/stress shall be as follows,

- ***Steel***. Latest edition of the AISC Manual of Steel Construction
- ***Aluminum***. Latest edition of the Aluminum Association's Aluminum Design Manual.
  - ***ASD***: Substation structures shall be designed with the safety factors specified for bridge-type structures.
  - ***LRFD***: The LRFD capacities given in the Aluminum Design Manual have resistance factors calibrated for building-type structures only. Consequently, the specifics of the design methodology are inconsistent with the objectives of this recoommended practice and should therefore not be used.
- ...

