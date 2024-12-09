# [U.A.E FIR] AIRAC 2412 - Revision 1
@U.A.E FIR Operations The Operations Department has been updating the **U.A.E FIR [OMAE]** sector file. Controllers must either perform a clean installation of the sector file or download the update package and overwrite their current files.  

## Sector File Changelog:
### Ground Radar Plugin
Significant reports of plugin crashes and tag issues have been received. The following changes have been implemented as a temporary measure until a fix is available:  

- **[OUTBOUND LISTS]** Outbound lists are now disabled by default to prevent crashes when controllers attempt to close them. Aerodrome controllers can restore their timer by navigating to **WINDOW → DEP TIMER → SELECT RUNWAY**.  
- **[TAGS]** The "Standby" label has been disabled as it was causing issues where controllers could not see aircraft, even if their transponder was in the correct mode and ON FREQUENCY.  
- **[SMGCS]** Sheikh Zayed Stand zoom level adjusted.

### Changes
- **[SETTINGS-PROFILES]** Fixed an issue where the A-CDM link was cut off due to a ":" placed in the profiles.txt file causing everything after that to be whipped off.

### Additions
- NIL
- 
### Removals
- NIL

[U.A.E FIR AeroNav Download](https://files.aero-nav.com/OMAE)

## Notice Confirmation
Controllers are required to acknowledge this operations update by clicking the :greentick: to confirm receipt. Please ensure that your sector file is updated accordingly. We have implemented several checks that allow us to easily identify if your sector file is not up to date!

## Interested in Contributing? Contribute now on GitHub!
In an effort to encourage contributions from everyone, the Sector File configuration files are now available on the **Arabian vACC GitHub Organization.**

Anyone can contribute or report issues by opening an issue to highlight a problem or suggest improvements. Members interested in contributing should fork the repository to their own account and submit a pull request for review and inclusion in the next AIRAC cycle.

[U.A.E FIR GitHub Repository](https://github.com/Arabian-vACC/OMAE-U.A.E-FIR-Controller-Pack)