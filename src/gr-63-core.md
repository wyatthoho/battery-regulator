# Notes of GR-63-CORE

## Packaged Equipment Drop Tests

Category B (> 100 kg) containers are subjected to free-fall, corner, 
and edge drops. The criteria below apply to Category B containers.

![](../img/gr-63-core/drop-height-packaged-b.png)

The packaged equipment is dropped once on each of the following locations:

- Surface: S1, S2, S3
- Edge: E1, E2, E3
- Corner: C1, C2, C3, C4

![](../img/gr-63-core/drop-surfaces.png)

### Free-Fall Drop

For Equipment Under Test (EUT) designed with handling hardware (e.g., 
eye bolts, etc.), the unit should be supported from it and allowed to 
assume the resultant position.

Because the rest face may not be horizontal, the prescribed drop height
 should be measured from the lowest point on the equipment to the floor.

![](../img/gr-63-core/free-fall-drop.png)

### Edge Drop

The support shall be the same height as the drop height. Raise the test 
edge to the drop height and release the EUT. After the EUT has impacted 
the test surface, *it shall be retained from toppling over*.

![](../img/gr-63-core/edge-drop.png)

### Corner Drop

The corner drop is performed as described in two different methods. 
The selection of the test method is based on engineering judgment of 
the more severe for the given EUT.

In Method 1, the support shall be the same height as the drop height. 
The EUT ts located on the support to maximize the impact on the corner
under test. Raise the test corner to drop height and release the EUT.
After the EUT has impacted the test surface, it shall be restrained 
from toppling over.

In Method 2, raise the test corner to drop height and release the EUT. 
After the EUT has impacted the test surface, it shall be restrained from 
toppling over.

![](../img/gr-63-core/corner-drop.png)

---

## Unpackaged Equipment Drop Tests

The unpackaged equipment shall not sustain any physical damage or 
deteriorate in functional performance when subjected to the applicable 
shock levels listed in the table below.

![](../img/gr-63-core/drop-height-unpackaged.png)

The EUT is subject to the following drops:

![](../img/gr-63-core/drop-surfaces.png)

- Rest Surface: S1
- Corner: C1, C2
- Edge: E1, E3

Drop the equipment once on each corner and edge adjacent to the rest 
surface.

![](../img/gr-63-core/equipment-handling.png)

---

## Earthquake Environment and Criteria

Zone 4 corresponds to the highest risk areas, Zone 3 the next highest, 
and so on.

A **frame-level** test configuration is used for network equipment 
supplied with a framework. A **shelf-level** configuration is used for 
equipment supplied as a single shelf to be installed in framework by 
the purchaser.

The equipment tested is expected to meet **physical** and **functional** 
performance requirements.

### Physical Performance Criteria

Typical examples of permanent structural damage are bent or buckled 
uprights, deformed bases, cracks, and failed anchors or fastening 
hardware.

During **frame-level** testing, the physical performance of the 
equipment shelves, framework, and fastening hardware are considered. 
Permanent structural or mechanical damage of any of these elements 
constitutes a test failure. During **shelf-level** testing, only the 
equipment shelf's physical performance is considered.

**Frame-level** equipment shall be constructed so that during the
waveform testing of Section 5.4.1, the maximum single-amplitude
deflection at the top of the framework, relative to the base, does not
exceed **75 mm**.

**Frame-level** equipment shall have a natural mechanical frequency
greater than **2.0 Hz** (necessary) and **6.0 Hz** (desirable) as 
determined by the swept sine survey.

### Earthquake Test Methods

Telecommunications equipment is earthquake tested using a prescribed 
waveform. The acceleration-time history waveform, **WERTEQII**, has been 
synthesized from several typical earthquakes and for different building 
and soil site conditions.

Waveforms are available from Bellcore on computer diskette in ASCII code. 
There are three waveforms: one for Zones 1 and 2 testing, one for Zone 3 
testing, and one for Zone 4 testing. For information and copies of the 
waveforms, contact Richard Kluge at (201)829-4669 or rgpk@notes.cc.bellcore.com.

![](../img/gr-63-core/verteqii-zone4.png)

When reproducing the Bellcore waveform, the shaker table's analyzed 
acceleration, known as the Test Response Spectrum (**TRS**), must meet or 
exceed the Required Response Spectrum (**RRS**) for the applicable 
Earthquake Risk Zone in the range from **1.0 to 50 Hz**. The TRS is 
determined using a damping level of **2%**.

![](../img/gr-63-core/required-response-spectrum.png)

---

## Framework and Anchor Criteria

For framework used in earthquake risk zones, the **static pull testing**
procedures of Section 5.4.1.4 should be followed, meeting these
objectives:

- The maximum single amplitude deflection at the top of the framework 
  should not exceed **75 mm**.
- The top of the framework should return to its original position, 
  within **6 mm** when the load is removed.
- The framework should sustain no permanent structural damage during
  static framework testing.

---

## Office Vibration

### Office Vibration Environment

Telecommunications equipment may be subjected to low-level vibration in 
service that is typically caused by nearby rotating equipment, outside 
rail or truck traffic, or construction work in adjacent buildings.

### Transportation Environment

Equipment will generally experience maximum vibration in the 
non-operating, packaged condition, during commercial transportation.
There are low-level vibrations of randomly distributed frequencies 
reaching **1 to 500 Hz** with occasional transient peaks.

![](../img/gr-63-core/transportation-environment.png)
