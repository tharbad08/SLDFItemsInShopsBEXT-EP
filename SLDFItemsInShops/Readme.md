## Required Mods:
- BTX_ExpansionPack v1.1-beta2
- BT_Extended_Timeline v2.0.0.3
- BT_Extended_CE v2.0.0.4
- BTX_PlayableVehicles v1.0

## What the mod does (Campaign)
- lvl-0: Mechs tagged worse.
- lvl-1: Light Mechs, Vees, Stock weapons (Long laser, Med laser, Small laser, SRM2,4, LRM5,10, AC2,5,10).
- lvl-2: Med Mechs, Vees, +1 weapons lvl1, Stock weapons (PPC, AC/20, LRM15,20, SRM6).
- lvl-3: Heavy Mechs, Vees, +2 lvl1 weapons, +1 lvl2 weapons.
- lvl-4: Assault Mechs, Vees, +3 lvl1 weapons, +2 lvl2 weapons. SLDF Stock weapons.
- lvl-5: SLDF common Mechs, +3 lvl2 weapons, lvl4 +1 weapons.
- lvl-6: SLDF rare Mechs, lvl4 +2 weapons. 
- lvl-7: lvl4 +3 weapons.

Upgrades were assigned to each level sometimes by rarity and sometimes by my logic.

## Planets revelation stages (I used the flipped file):
0. All unaligned planets.
1. Weldry, Fjaldr, Ichlangis: milestone_305_sim_argo_start
2. Panzyr, Bringdam, RyansFate, Mechdur: milestone_324_sim_argo
3. Smithon, Umgard, Enkra, Zangul: milestone_344_sim_argo
4. Itrom, Mangzhangdian (Post Nautilus castle): milestone_532_sim_argo
5. Tyrlon, Guldra, Heliat, Gangtok: milestone_623_sim_argo
6. Coromodir, Aea, Qalzi, RegisRoost, Katinka, Artru: milestone_700_notify_complete
7. Chance to see in Research Progression, SLDF Progression and Battlefield Progression planets.

## Number of items:
- Number of items: 50% of max.

## What the mod does (Career)
- Doubles the amounts of items offered in markets (Done by appending all item lists to themselves)
- Allows to buy SLDF items: Number of items same as in itemCollection_SLDF_lvl-# lists
-   ElectronicsProgression: itemCollection_SLDF_Equipment_lvl-4,5,6
-   ChemicalsProgression: itemCollection_SLDF_Weapons_lvl-4,5,6,7
-   MiningProgression: itemCollection_SLDF_Equipment_lvl-4, itemCollection_SLDF_Ammo_lvl-4
-   MunitionsProgression: itemCollection_SLDF_Ammo_lvl-4,5, itemCollection_SLDF_Weapons_lvl-4
-   ResearchProgression: itemCollection_SLDF_Weapons_lvl-4,5, itemCollection_SLDF_Mech_lvl-4,5, itemCollection_SLDF_MechPart_lvl-4,5, itemCollection_SLDF_Vee_lvl-4
-   StarleagueProgression: itemCollection_SLDF_Weapons_lvl-6,7, itemCollection_SLDF_Equipment_lvl-6, itemCollection_SLDF_Mech_lvl-6, itemCollection_SLDF_MechPart_lvl-6
-   BattlefieldProgression: Entire lvl6 except ammo, itemCollection_SLDF_Vee_lvl-4.
-   Battlefield: Entire lvl5 except ammo, itemCollection_SLDF_Equipment_lvl-3, itemCollection_SLDF_Vee_lvl-3.
-   Starleague: itemCollection_SLDF_Mech_lvl-4,5, itemCollection_SLDF_MechPart_lvl-4,5, itemCollection_SLDF_Weapons_lvl-4,5, itemCollection_SLDF_Equipment_lvl-4,5
-   Research: itemCollection_SLDF_Ammo_lvl-4, itemCollection_SLDF_Equipment_lvl-3, itemCollection_SLDF_Vee_lvl-3, itemCollection_SLDF_Weapons_lvl-3, itemCollection_SLDF_MechPart_lvl-3
-   Electronics: itemCollection_SLDF_Equipment_lvl-2,3
-   Chemicals: itemCollection_SLDF_Weapons_lvl-2,3
-   All minor planets: itemCollection_SLDF_Ammo_rare_use

### What if I don't have Vees enabled?
- You won't see them

## This mod make my game too easy!
- I know. That's the point. 
- If you only want SLDF items in the shop, empty itemCollection_SLDF_lvl-1,2,3 files
- You can delete some files from the "starsystem" dir to remove the mod extra items from those stores. I suggest deleting everything but: Weldry, Panzyr, Smithon, Itrom, Tyrlon and Coromodir.
- OR: enter items folder and open itemCollection_SLDF_lvl-# files. Lower the the number in the 3rd field. Say: itemCollection_SLDF_Ammo_lvl-1,Reference,**14**,1 to itemCollection_SLDF_Ammo_lvl-1,Reference,**7**,1 will lower the number of items drown from that list from 14 to 7.

## License
This software is licensed with GPL 3.0. If you repacked it, please let me know. If you have problems, open an issue.
