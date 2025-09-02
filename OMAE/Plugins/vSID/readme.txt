- correlation mode "easy" required due to ES limitations! It's under investigation if we could change it so "S/C-Mode")
- cleared to land flag added within the tag + ARR list (left click on AFL)
- vSID SID added within the tag
- appSI in just a random order for testing
- A SIDs highlighted
- Radar SIDs for testing only manual without transition (this kind of SID does need some extra attention within the config later on)

Time dependant SIDs: (deactivated by default)
- ".vsid time othh" => A SIDs will be used during the published times

Area: (active by default)
- ".vsid area othh west" => (de-)activates "west area", all departures parking on the western part of the airport via TULUB and LUBET will get RWY 34L/16R. Area is active by default for most of the time low traffic situations.

Custom Rules: (deactivated by default)
- ".vsid rule othh tulubwest" => all TULUB departures will get RWY 34L/16R
- ".vsid rule othh lubetwest" => all LUBET departures will get RWY 34L/16R

vSID Wiki: https://github.com/Gameagle/vSID/wiki
VatGer vSID Controller Manual: https://knowledgebase.vatsim-germany.org/books/vsid-plugin/page/vsid-controller-manual