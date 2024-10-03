# Notes of IEEE 693

## What clauses or annexes should be used? (Based on Figure 1)

- Clause 5.7, 5.8, 5.10, 5.12
- Annex A.1.4, A.1.6, A.2, A.4
- Annex J
- Annex S

---

## 5.2 Seismic qualification objective

### **General**

The objective is to secure substation equipment that will have no 
***significant damage*** and maintain electrical functionality at
normal operating conditions during and after a seismiic event.
Some damage is tolerated, provided that it is not significant
structural damage.


### **Significant damage**

- ***Failure to maintain fuctionality***: The equipment ceases to perform its primary electrical function.
- ***Excess yielding or fracture***: The equipment has a possibility of imminent collapse at nominal electric operating conditions.

It is important to realize that ***yielding is permitted*** provided
that it does not impair electrical functionality or pose a risk of
imminent collapse. ***Fracture*** of a component is considered 
significant damage.

---

## 5.3 Seismic qualification approaches

### **General**

- ***Performance level qualification approach***
  - Performance level testing
  - Performance level analysis
- ***Design level qualification approach***
  - Design level testing
  - Design level analysis

To help ensure uniformity of qualification procedurees for any specify
type of equipment, the seismic qualification approach is establiished
in each particular ***equipment annex***.

The accelerations of the response spectra used for the design level
approach at the moderate and high seismic qualification levels are 
half of the performance level spectra at any given frequency and level 
of damping.

---

## 5.5 Seismic qualification methods with respect to analytical qualifications

The seismic qualification objective permits ***yielding*** of 
components when subjected to performance level loading. However, 
all of the design level analytical qualification techniques assumes
a ***linear*** response.

---

## 5.6 Damping with respect to seismic qualification methods

A damping ratio of ***2%*** (damping) may be assumed for all design
level ***analysis***,while a value of ***5%*** is used to ***match*** 
the required response spectra (RRS). 

The damping for matching is used generically with establishing 
the sufficiency of time-history data used in conjuction with time 
history analysis and testing. It has been shown to be more 
conservative in comparison to matchinig at 2% damping.

---

## 5.7 Seismic qualification levels

This recommended practice recognezes three seismic qualification 
levels: high, moderate, and low. For the ***high*** qualification 
level, the horizontal zero period acceleration (ZPA) associated with 
the seismic qualification objective is ***1.0 g***.

The required response spectra (RRS) used in a performance level 
qualification corresponds to the "High Performance Level 
Response Spectrum" depicted in ***Figure A.1***.

---

## 5.8 Response spectra

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

---

## 5.10 Influence of support structures

The support structure must be designed for the seismic demand loads 
and dynamic characteristics of the combined equipment/support
structure. For equipment that is mounted on a support structure, 
the combined system may be qualified by one of the following:

- analyze and/or test the combined system
- using an analytically-derived, modified input motion that allows for the effects of the support structure
- using a modified input motion (2.5 x RRS)

---

## 5.12 Selecting the seismic level

The selection of seismic level for seismic qualification involves
risk management. The acceptance or aversion of risk can only
be judged by the user, thus the selection of seismic level should
only be done by users.

As the performance level of equipment is often projected from tests
conducted at the design level or analyses, there is uncertainty as to 
the true performance level. To reeduce the risks of unfavorable 
performance associated with this uncertainty, the user may wish
to assign the ***high qualificationn level*** to sites with a PGA
less than, but approaching, ***0.5 g***.

---

## Annex A

### **Qualification configuration**

The equipment should be ***tested*** or ***analyzed*** in its 
equivalent in-service configuration, including support structures.

### **Normal operating loads**

Normal operating loads are to be considered to act simultaneously 
with seismic and dead loads.

### **Triaxial analysis and testing**

Analysis and time history testing shall be triaxial with simulation
of ***translational ground accelerations*** in three directions. A 
test response spectrum that envelops the RRS shall be applied in the
two perpendicular horizontal axes together with a response spectrum 
in the vertical axis that shall have an acceleration of ***80%*** 
of that in the horizontal axes.

### **Damping**

Damping can either be assumedat a conservative level (5.6) or 
determined by any of the following methods:

- Measuring the decay rate
- Measuring the half-power bandwidth
- Curve fitting to frequency response methods
- Time domain curve fitting

### **High seismic qualification level**

Qualifications to the ***high*** seismic qualification level shall
meet the relevant requirements given in Annex A in conjunction with 
the spectrum depicted in ***Figure A.1***.

![](../img/ieee-693-notes/required-response-spectrum.png)

### **Time history shake-table test qualification**

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

### **Analytical qualification**

Using the design level seismic loads corresponding to 50% of the
performance level loading defined by the response spectra of Figure
A.1 for the high performance levels.

Terminal attachments representing the in-service configuration of 
the equipment ***terminal masses*** should be included:

- 500 kV and greater: 11 kg
- Greater than 145 kV to less than 500 kV: 7 kg

The incremental increase in demand on the equipment insulator due
to application of the moment amplification factor (MAF) or equivalent 
terminal force (ETF) shall be applied for equipment qualified by 
analysis in accordance with A.1.6.

The ***SRSS*** method, as used in this recommended practice, combines local seismic forces acting on a particular element of a structure
system. In lieu of the SRSS combination of three orthogonal earthquake 
components, a ***100/40/40*** combination rule may be used.

#### ***Static Analysis***

The forces on each component of the equipment shall be obtained
by multiplying the values of the ***mass*** of the components
by the ***acceleration*** specified in the principal directions.

The vertical seismic forces shall act simultaneously with both
horizontal seismic forces. The three forces shall be using one of
the ***combination techniques*** in A.1.4.4.

When the ***high*** seismic level is specified, the static analysis 
shall use a ***design*** level load consisting of ***0.5 g*** in the
two horizontal directions and ***0.4 g*** in the vertical direction.

---

## Annex J Station batteries and battery racks

### **Battery racks**

The seismic withstand capability of battery racks shall demonstrated
as follows:

- Non-rigid racks of three or more stacks: By performance level time history shake-table testing
- Non-rigid racks of two stacks: By dynamic analysis
- Rigid racks and all racks of one stack: By ***static analysis***

### **Static analysis**

Battery racks shall be qualified according to the requirements of
**A.1** and **A.1.4.5**.

### **Acceptance criteria**

The general criteria of ***A.2*** or as applicable to the 
qualification method shall be met.
