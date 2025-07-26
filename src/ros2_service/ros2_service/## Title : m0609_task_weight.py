## Title : m0609_task_weight
## Time : 2025-05-28 18:24:50
Global_11 = 0
Global_1 = posx(497.10,48.55,27.37,128.99,179.94,128.63)
set_singular_handling(DR_AVOID)
set_velj(60.0)
set_accj(100.0)
set_velx(250.0, 80.625, DR_OFF)
set_accx(1000.0, 322.5)
gLoop182450978 = 0
while gLoop182450978 < 1:
    # MoveLNode
    movel(posx(494.44, 150.37, 35.20, 91.38, 179.96, 91.03), radius=0.00, ref=0, mod=DR_MV_MOD_ABS, ra=DR_MV_RA_DUPLICATE, app_type=DR_MV_APP_NONE)
    # SetNode
    set_digital_output(2,OFF)
    # WaitNode
    wait(1.00)
    # MoveLNode
    movel(posx(494.45, 150.37, 75.20, 91.15, 179.96, 90.80), radius=0.00, ref=0, mod=DR_MV_MOD_ABS, ra=DR_MV_RA_DUPLICATE, app_type=DR_MV_APP_NONE)
    # WaitNode
    wait(1.00)
    # WeightMeasureNode
    Global_11 = get_workpiece_weight()
    # CustomCodeNode
    tp_popup("{}".format(Global_11))
    gLoop182450978 = gLoop182450978 + 1