---
sidebar_position: 28
title: 🚧 SurveillanceStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# SurveillanceStation
:::warning
 
This API is not documented yet.
 
:::
## Overview

## Methods
### `surveillance_station_info`
Get infos about surveillance station and the server  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
Informations about surveillance station and the server  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "CMSMinVersion": "9.2.2-11575",
        "DSModelName": "DS723+",
        "SvsClientMinVersion": "2.1.3-2474",
        "VS360HDLoginMinVersion": "5.0.1-6253",
        "VS960HDMinVersion": "3.0.1-3254",
        "cameraNumber": 1,
        "customizedPortHttp": 9900,
        "defaultWallpaperCount": 2,
        "enableVideoRelay": false,
        "hostname": "SYNO-FLORENTB",
        "inaAdvancedPriv": 0,
        "isBeta": false,
        "isLicenseEnough": 1,
        "is_beta": false,
        "liscenseNumber": 2,
        "maxCameraSupport": 40,
        "maxlanport": "3",
        "path": "/webman/3rdparty/SurveillanceStation/",
        "pluginHelperVersion": "",
        "productName": "Synology NAS",
        "remindQuickconnectTunnel": true,
        "reportURL": "deprecated",
        "serial": "2260TPR7X30E6",
        "serviceVolSize": 192,
        "strInaAdvancedPriv": "000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "timezone": "Amsterdam",
        "timezoneTZDB": "Europe/Amsterdam",
        "uid": 1027,
        "unique": "synology_r1000_723+",
        "userPriv": 1,
        "version": {
            "build": "11575",
            "major": "9",
            "minor": "2",
            "small": "2"
        },
        "webPluginVersion": ""
    },
    "success": true
}
```
</details>



---


### `camera_save`
_summary_  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_params_**  [`SaveCameraParamType`](/apis/structures.md#savecameraparamtype)   
Check details of the parameters structures by clicking on the type  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
_description_  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "template": "data"
    },
    "success": true
}
```
</details>



---


### `camera_list`
Get camera list with a lot of options  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_idList_** `str`  
The list of CAMERA_ID to be queried concatenated by ",". Defaults to `""`  
  
**_blFromCamList_** `bool`  
Indicating if the caller is from cam list. Defaults to `False`  
  
**_offset_** `int`  
The offset to be shifted in the total result. Defaults to `0`  
  
**_limit_** `int`  
Number of cameras to be returned.. Defaults to `0`  
  
**_blIncludeDeletedCam_** `bool`  
Indicating if deleted cameras should be listed or not. Defaults to `True`  
  
**_privCamType_** `int`  
Weighted sum indicated the types of the camera. Defaults to `3`
    0x00: NONE
    0x01: LIVEVIEW
    0x02: PLAYBACK
    0x04: LENS
    0x08: AUDIO  
  
**_basic_** `bool`  
Indicating to show basic settings or not. Defaults to `True`  
  
**_streamInfo_** `bool`  
Indicating to show streaming information or not. Defaults to `True`  
  
**_blPrivilege_** `bool`  
Indicating if the user privilege should be checked or not. Defaults to `True`  
  
**_camStm_** `int`  
Stream number of the camera live view. Defaults to `2`
    0: Live stream
    1: Recording stream
    2: Mobile stream (default value)  
  
**_blGetMulticastInfo_** `bool`  
Indicating to show multicast infos or not. Defaults to `True`  
  
**_videoCapInfo_** `bool`  
Indicating to show video capabilities or not. Defaults to `False`  
  
**_eventDetection_** `bool`  
Indicating to show event detection or not. Defaults to `True`  
  
**_ptz_** `bool`  
Indicating to show ptz info or not. Defaults to `True`  
  
**_fisheye_** `bool`  
Indicating to show fisheye info or not. Defaults to `True`  
  
**_deviceOutCap_** `bool`  
Indicating to show deviceOutCap info or not. Defaults to `True`  
  
**_liveviewAnalytics_** `bool`  
Indicating to show liveviewAnalytics info or not. Defaults to `True`  
  
**_ioList_** `bool`  
Indicating to show ioList info or not. Defaults to `True`  
  
**_optimize_** `bool`  
Optimize. Defaults to `True`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
A lot of informations about each camera  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "cameras": [
            {
                "ADCap": 0,
                "ADDetSrc": -1,
                "AppList": [],
                "DINum": 0,
                "DONum": 0,
                "MDCap": 0,
                "MDDetSrc": -1,
                "MDModeList": [
                    0,
                    1
                ],
                "PDCap": 0,
                "PDDepend": 0,
                "PDDetSrc": -1,
                "QRCodeCap": 0,
                "TDCap": 0,
                "TDDetSrc": -1,
                "advLiveMinDuration": 10,
                "advLiveProfile": 0,
                "advLiveTrigAuto": true,
                "advLiveTrigEvt": "000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                "advLiveTrigSingle": false,
                "alertEvents": "000000000000000000000000000000000000000000000000000000000000000000000000000000001",
                "analyticsDirection": 1,
                "analyticsDwellTime": 5,
                "analyticsFrame": true,
                "analyticsLine": false,
                "analyticsObjSize": 0,
                "analyticsRegion": "",
                "analyticsSens": 1,
                "analyticsType": 0,
                "analyticsVirtualFence": false,
                "appDetType": -1,
                "application": false,
                "audioCap": true,
                "audioDenoiseLevel": 0,
                "audioOut": false,
                "audioType": 6,
                "autoFocus": false,
                "autoPan": 0,
                "autoPanInitPos": -2,
                "autoPanPreSleepTime": 10,
                "autoUpgradeCriticalOnly": false,
                "autoUpgradeDays": "",
                "autoUpgradeEnabled": false,
                "autoUpgradeHour": 0,
                "autoUpgradeMinute": 0,
                "auto_restart_interval": 0,
                "blAudioDenoiseEnabled": false,
                "blAudioDisableRec": false,
                "blAudioPriv": true,
                "blDayLightSavingEnabled": false,
                "blDisableRec": false,
                "blEnableExtDI": false,
                "blEnableLiveBuffering": false,
                "blG726LE": false,
                "blHDREnabled": false,
                "blLEDIndicatorEnabled": false,
                "blLiveviewPriv": true,
                "blPresetSpeed": false,
                "blPtzShowIcon": false,
                "blReceivePocZero": false,
                "blThirdStream": true,
                "brightness": 0,
                "c2_plan_id": "",
                "c2_stream_no": 0,
                "calling_notify_ado_src_id": 0,
                "calling_notify_duration": 0,
                "camCurrentFirmware": "",
                "camDualRecStorageStatus": 0,
                "camFov": "",
                "camIdOnRecServer": 0,
                "camLiveMode": 0,
                "camMobileLiveMode": 0,
                "camMountType": 0,
                "camRecShare": "surveillance",
                "camRecShareMountType": 0,
                "camRecSharePath": "/volume1/surveillance",
                "camRecStorageStatus": 0,
                "camRecVolume": "/volume1",
                "camRotOption": 0,
                "camSourceType": 1,
                "camStatus": 16,
                "camVideoType": "H.264",
                "channel_id": "1",
                "checkedAlertDIs": 0,
                "connectionOverSSL": false,
                "contrast": 0,
                "dayToNightThreshold": 0,
                "daybegin": 8,
                "daybeginMinute": 0,
                "dayend": 18,
                "dayendMinute": 0,
                "defLiveProfile": 0,
                "defog": 0,
                "deleted": false,
                "denoiseLevel": 0,
                "deviceType": 1,
                "doorbellNum": 0,
                "dsIp": "",
                "dsPort": 5000,
                "dualRec": {
                    "camPostRecTime": 5,
                    "camPreRecTime": 5,
                    "drCustom1DIDetect": 0,
                    "drCustom1Detect": 1,
                    "drCustom2DIDetect": 0,
                    "drCustom2Detect": 1,
                    "drFolder": "Generic_ONVIF-001_dual",
                    "drIsRotByDate": true,
                    "drIsRotBySpace": false,
                    "drIsSetEvtPrefix": false,
                    "drIsSetRecFolder": true,
                    "drPrefix": "Generic_ONVIF-001",
                    "drRecShareName": "surveillance",
                    "drRecSharePath": "/volume1/surveillance",
                    "drRecordTime": 30,
                    "drRotByDate": 30,
                    "drRotBySpace": 10,
                    "drSchedule": [
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                    ],
                    "drStmProfile": 0,
                    "drVolume": "/volume1"
                },
                "dualRecStatus": 0,
                "dual_rec_mode": 0,
                "dual_volume_space": "0",
                "enableAdvLive": false,
                "enableAutoLiveProfile": true,
                "enableMulticast": false,
                "enableMulticastMobile": false,
                "enablePrivacyMask": false,
                "enablePtzControl": true,
                "enableSRTP": false,
                "enable_calling_notify": false,
                "enabled": true,
                "exposure_control": 6,
                "exposure_mode": 4,
                "extDIDev": 0,
                "extDIPorts": -1,
                "feRegionList": [],
                "firmware": "",
                "fisheyeDispMode": "",
                "fisheyeParam": {},
                "folder": "/volume1/surveillance/Generic_ONVIF-001",
                "forceEnableMulticast": false,
                "forceMjpeg": false,
                "fps": 30,
                "hasCamParam": true,
                "hasEdgeStg": false,
                "host": "192.168.1.15",
                "id": 1,
                "intercomCap": 0,
                "io_list": [],
                "irLEDIntensity": 90,
                "isStatusUnrecognized": false,
                "is_rotated_by_date": true,
                "is_rotated_by_space": true,
                "last_edit_time": "",
                "last_restart_time": "",
                "last_sync_time": "",
                "ledCap": false,
                "liveBufferingSec": 1,
                "mac": "3E:5F:9C:A6:D7:1F",
                "mixAudioOutEnabled": false,
                "model": "Generic_ONVIF",
                "multiDI": false,
                "multicastAudioPort": 0,
                "multicastAudioPortMobile": 0,
                "multicastGrpAddr": "",
                "multicastGrpAddrMobile": "",
                "multicastVideoPort": 0,
                "multicastVideoPortMobile": 0,
                "mute": false,
                "name": "Generic_ONVIF-001",
                "nightToDayThreshold": 0,
                "objTrack": false,
                "osdColor": 0,
                "osdDateFormat": 0,
                "osdText": "",
                "osdTimeFormat": 0,
                "osd_format": 0,
                "osd_position": 6,
                "osd_status": true,
                "ownerDsId": 0,
                "pairedSpeakerEnabled": false,
                "pairedSpeakerId": 0,
                "pairedSpeakerType": 0,
                "param_chklist": 1,
                "period_sync_time_hour": 0,
                "port": 8080,
                "presetNum": 0,
                "privacyMaskEnabled": false,
                "privacyMaskSrc": 0,
                "privacyRegion": "",
                "privilege": 31,
                "profileSettingList": "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
                "ptSpeed": 3,
                "ptzCap": 0,
                "ptzContinuous": 0,
                "ptzCtrlConfig": {},
                "ptzDirection": 0,
                "ptzHomeType": 0,
                "ptzSpeedConfig": -1,
                "ptzSpeedKeepOrigin": true,
                "quality": "5",
                "recBitrateCtrl": 1,
                "recCbrBitrate": 1024,
                "recStatus": 0,
                "relayPortList": [],
                "resolution": "1920x1080",
                "restart_day": 0,
                "rotation_by_date": 30,
                "rotation_by_space": "10",
                "rotation_option": 0,
                "rtspPathTimeout": 0,
                "saturation": 0,
                "serialNumber": "",
                "setDICap": false,
                "setDOCap": false,
                "sharpness": 0,
                "shutterGainMax": 0,
                "shutterGainMin": 0,
                "shutterMax": 0,
                "shutterMin": 0,
                "singleStream": true,
                "snapshotInterval": 0,
                "snapshot_path": "/webapi/entry.cgi?api=SYNO.SurveillanceStation.Camera&method=GetSnapshot&version=1&cameraId=1&timestamp=1739488148&preview=true&camStm=1",
                "speedDryCap": false,
                "status": 3,
                "status_flags": 0,
                "stmFisheyeType": 0,
                "stm_info": [
                    {
                        "camPath": "cnRzcDovL2FkbWluOmFkbWluQDE5Mi4xNjguMS4xNTo4MDgwL2gyNjRfbm9hdWRpby5zZHA=",
                        "fisheyeType": 0,
                        "fps": 30,
                        "quality": "5",
                        "resolution": "1920x1080",
                        "stmNo": 1,
                        "type": 0
                    },
                    {
                        "camPath": "cnRzcDovL2FkbWluOmFkbWluQDE5Mi4xNjguMS4xNTo4MDgwL2gyNjRfdWxhdy5zZHA=",
                        "fisheyeType": 0,
                        "fps": 30,
                        "quality": "5",
                        "resolution": "1920x1080",
                        "stmNo": 1,
                        "type": 1
                    },
                    {
                        "camPath": "cnRzcDovL2FkbWluOmFkbWluQDE5Mi4xNjguMS4xNTo4MDgwL2gyNjRfdWxhdy5zZHA=",
                        "fisheyeType": 0,
                        "fps": 30,
                        "quality": "5",
                        "resolution": "1920x1080",
                        "stmNo": 1,
                        "type": 2
                    }
                ],
                "stm_info_ptzCaps": [
                    {
                        "autoFocus": false,
                        "autoPan": 0,
                        "autoPanInitPos": -2,
                        "autoPanPreSleepTime": 10,
                        "blPresetSpeed": false,
                        "blPtzShowIcon": false,
                        "objTrack": false,
                        "presetNum": 0,
                        "ptSpeed": 3,
                        "ptzCap": 0,
                        "ptzContinuous": 0,
                        "ptzCtrlConfig": {},
                        "ptzDirection": 0,
                        "ptzHomeType": 0,
                        "ptzSpeedConfig": -1,
                        "ptzSpeedKeepOrigin": true,
                        "zoomSpeed": 3
                    },
                    {
                        "autoFocus": false,
                        "autoPan": 0,
                        "autoPanInitPos": -2,
                        "autoPanPreSleepTime": 10,
                        "blPresetSpeed": false,
                        "blPtzShowIcon": false,
                        "objTrack": false,
                        "presetNum": 0,
                        "ptSpeed": 3,
                        "ptzCap": 0,
                        "ptzContinuous": 0,
                        "ptzCtrlConfig": {},
                        "ptzDirection": 0,
                        "ptzHomeType": 0,
                        "ptzSpeedConfig": -1,
                        "ptzSpeedKeepOrigin": true,
                        "zoomSpeed": 3
                    },
                    {
                        "autoFocus": false,
                        "autoPan": 0,
                        "autoPanInitPos": -2,
                        "autoPanPreSleepTime": 10,
                        "blPresetSpeed": false,
                        "blPtzShowIcon": false,
                        "objTrack": false,
                        "presetNum": 0,
                        "ptSpeed": 3,
                        "ptzCap": 0,
                        "ptzContinuous": 0,
                        "ptzCtrlConfig": {},
                        "ptzDirection": 0,
                        "ptzHomeType": 0,
                        "ptzSpeedConfig": -1,
                        "ptzSpeedKeepOrigin": true,
                        "zoomSpeed": 3
                    }
                ],
                "strTimeZone": "",
                "streamAudioVolume": 0,
                "time_server": "disable",
                "tvStandard": 0,
                "type": 3,
                "uiStmNoList": "1,1,1",
                "update_time": 13,
                "vendor": "ONVIF",
                "videoMode": "",
                "video_flip": true,
                "video_mirror": true,
                "video_rotation": 0,
                "volume": 50,
                "volume_space": "0",
                "whiteBalanceBlue": 0,
                "whiteBalanceMode": 0,
                "whiteBalanceRed": 0,
                "wifiSSID": "",
                "wiperCap": false,
                "zoomSpeed": 3
            }
        ],
        "delcam": [],
        "existCamMntTypeMap": null,
        "keyTotalCnt": 2,
        "keyUsedCnt": 1,
        "timestamp": "1739488148",
        "total": 1
    },
    "success": true
}
```
</details>



---


### `get_camera_info`
This function return information about a camera.  
cameraIds : This parameter is named cameraIds in the API documentation but it refer to 1 camera ID  
privCamType: int = 1
    SYNO.SS.CamPriv.LIVEVIEW = 1;
    SYNO.SS.CamPriv.PLAYBACK = 2;
    SYNO.SS.CamPriv.LENS = 4;
    SYNO.SS.CamPriv.AUDIO = 8;
    SYNO.SS.CamPriv.DIGIOUT = 16;  
All other parameters must be let to default value  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  



---


### `camera_list_group`



---


### `get_snapshot`
By default, the profileType is 1, which is the default profile.  
Binary data is returned, so the response is not a json object.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera` 
</div>
  



---


### `enable_camera`



---


### `disable_camera`



---


### `get_capability_by_cam_id`



---


### `count_occupied_size`



---


### `is_shortcut_valid`



---


### `get_live_path`



---


### `audio_event_enum`



---


### `alarm_event_enum`



---


### `md_parameter_save`



---


### `motion_event_enum`



---


### `motion_parameter_save`



---


### `di_parameter_save`



---


### `alarm_sts_polling`



---


### `td_parameter_save`



---


### `enumerate_camera_group`



---


### `save_specific_group`



---


### `delete_specific_groups`



---


### `enumerate_group_information`



---


### `enumerate_camera_from_archive`



---


### `enumerate_archive_from_folder`



---


### `check_available_size_of_sdcard`



---


### `check_licence_quota`



---


### `format_specific_sd_card`



---


### `quick_create_single_camera`



---


### `move_camera_lens`



---


### `camera_lens_zoom`



---


### `list_preset_ptz_camera`



---


### `move_camera_lens_to_preset_position`



---


### `list_patrol_cameras`



---


### `force_cam_to_execute_patrol`



---


### `focus_camera`



---


### `control_camera_iris_in_out`



---


### `auto_focus`



---


### `move_cam_lens_to_absolute_position`



---


### `move_cam_to_home_position`



---


### `auto_pan_camera`



---


### `start_stop_object_tracking`



---


### `start_stop_external_recording`



---


### `query_event_list_by_filter`



---


### `delete_recordings`



---


### `delete_events_by_filter`



---


### `delete_all_recordings`



---


### `apply_settings_advance_tab`



---


### `count_by_number_of_event`



---


### `keep_event_play_alive`



---


### `stop_recording_event`



---


### `load_settings_in_advanced_tab`



---


### `lock_selected_event`



---


### `unlock_selected_event`



---


### `unlock_selected_filter_event`



---


### `lock_selected_recordings`



---


### `download_recordings`



---


### `check_if_recording_playable`



---


### `play_specific_recording`



---


### `download_merged_recording_files`
Download the merged files of UTC time range recordings of target camera.  
If there are different resolution or codec within UTC time range, the recordings will merge as much as possible
and downlod file will be a zip file.  
This method will start a task which have keep-alive mechanism.
Use GetRangeExportProgress method to get newest progress and keep-alive.
After receiving progress 100, use OnRangeExportDone method to download exported recording within 1
minutes.
If you want to cancel range export task, just do not send GetRangeExportProgress method or
OnRangeExportDone method. System will cleanup processed files itself.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  



---


### `get_newest_progress_keep_alive`



---


### `download_recording_from_target`
Response  
MP4 or zip file data.
The response type can be found in fileExt of GetRangeExportProgress method response when progress 100.  
Note
GetRangeExportProgress method must be sent within 1 minute after corresponding RangeExport method task
is completed, otherwise the exported recordings will be cleared.  
2.3.11.20 API Error Code
Code Description
400 Execution failed.
401 Parameter invalid.
405 CMS server connection failed.
414 Some events not exist.
439 Too many items selected.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Recording` 
</div>
  



---


### `handle_load_event_export`



---


### `check_name_export_event`



---


### `get_camera_information_list`



---


### `check_destination_folder_availability`



---


### `handle_save_event_export`



---


### `get_event_export_info_from_recording_server`



---


### `load_event_mount`



---


### `redirect_webapi_to_target_ds`
webAPI Array of `webAPI_info`  
Example:
`webAPI={"api": "SYNO.SurveillanceStation.AddOns", "version": 1, "method":
"List"}`  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS` 
</div>
  



---


### `modify_share_privilege`



---


### `apply_option_settings`



---


### `get_cms_info`



---


### `get_log_recording_data_from_target_ds`



---


### `get_samba_service`



---


### `check_if_samba_on_and_rec_enabled`



---


### `get_encoded_single_image_of_camera`



---


### `get_cms_status`



---


### `enable_smb_service`



---


### `notify_slave_ds_to_disconnect`



---


### `lock_recording_server_prevent_setting_change`



---


### `enable_ds_into_recording_server`



---


### `unpair_recording_servers`



---


### `get_free_memory_size`



---


### `handle_slave_ds`



---


### `get_target_ds_info`



---


### `logout_slave_ds`



---


### `pair_slave_ds`



---


### `login_slave_ds`
2.3.15.9 API Error Code  
Code Description
400 Execution failed.
401 Invalid parameter.
415 message connect failed.  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.CMS.GetDsStatus` 
</div>
  



---


### `save_slave_ds`



---


### `load_slave_ds_list`



---


### `count_number_of_logs`



---


### `clear_selected_logs`



---


### `get_information_log`



---


### `get_advanced_settings_logs`



---


### `set_advanced_setting_logs`



---


### `load_license_data`



---


### `get_http_video_stream`



---


### `save_action_rule`



---


### `download_action_rule`



---


### `send_data_2_player`



---


### `delete_all_histories_of_action_rule`



---


### `list_action_rules`



---


### `disable_action_rules`



---


### `enable_action_rules`



---


### `list_history_action_rules`



---


### `delete_action_rule`



---


### `get_list_of_emaps`



---


### `get_specific_emaps_setting`



---


### `get_emap_image`



---


### `get_autorized_ds_token`



---


### `set_message_event`



---


### `get_message_event`



---


### `set_notification_sender_name`



---


### `get_notification_sender_name`



---


### `set_advanced_notification_setting`



---


### `get_advanced_notification_setting`



---


### `send_test_mesg_to_primary_secondary_phone`



---


### `get_setting_notification_sms`



---


### `set_sms_service_setting`



---


### `send_test_sms`



---


### `send_test_mail`



---


### `list_mobile_paired_devices`



---


### `unpair_device`



---


### `get_controller_access_schedule`



---


### `get_camera_alarm_schedule`



---


### `get_sys_dependent_schedule`



---


### `set_batch_schedule`



---


### `get_access_ctrl_door_schedule`



---


### `get_camera_schedule`



---


### `set_sys_dependent_schedule`



---


### `set_controller_access_schedule`



---


### `set_camera_schedule`



---


### `get_notification_email_string`



---


### `set_adv_tab_info_filter`



---


### `create_sms_service_provider`



---


### `list_sms_provider`



---


### `delete_sms_service_provider`



---


### `get_addson_to_update`



---


### `enable_specific_addon`



---


### `get_specific_addon_update_info`



---


### `get_specific_addon_info`



---


### `get_total_addon_info`



---


### `update_addon_package`



---


### `check_addon_status`



---


### `disable_addon`



---


### `set_addon_autoupdate`



---


### `delete_specific_camera_recording_server`



---


### `get_camera_event_analytic`



---


### `delete_selected_events`



---


### `delete_specific_camera_events`



---


### `get_analytic_history`



---


### `get_analytic_history_by_filter`



---


### `unklock_selected_events`



---


### `set_camera_analytic_trigger`



---


### `flush_event_header`



---


### `lock_selected_events`



---


### `get_analytic_event_from_rec_server`



---


### `save_analytic_settings`



---


### `check_if_snapshot_exist`



---


### `save_snapshot_modification`



---


### `count_snapshot_by_category`



---


### `check_any_locked_snapshot`



---


### `unlock_snapshot_by_filter`



---


### `list_snapshot_information`



---


### `unlock_snapshot`



---


### `take_snapshot`



---


### `get_snapshot_setting_function`



---


### `delete_snapshot_by_filter`



---


### `get_snapshot_image`



---


### `lock_snapshot_image`



---


### `downld_single_snapshot`



---


### `save_new_snapshot_setting`



---


### `save_snapshot`



---


### `check_snapshot_status`



---


### `enable_visualstation`



---


### `update_vs_network_config`



---


### `lock_visualstation_by_id`



---


### `enumerate_vs_owner_info`



---


### `unlock_visualstation_by_id`



---


### `disable_visualstation_by_id`



---


### `delete_specific_visualstation`



---


### `enumerate_layout_visualstation`



---


### `save_layout_information`



---


### `delete_layout_visualstation`



---


### `clear_visualstation_search_result`



---


### `get_visualstation_ip_info`



---


### `stop_previous_visualstation_search`



---


### `get_visualstation_list`



---


### `get_number_of_controller`



---


### `get_cardholder_count`



---


### `enum_all_controllers_logger`



---


### `get_cardholder_photo`



---


### `get_log_count`



---


### `get_cardholder_info`



---


### `retrieve_last_access_credential`



---


### `enable_disable_controller`



---


### `acknowledge_all_alarm_level_log`



---


### `modify_controller_logger_config`



---


### `save_controller_settings`



---


### `download_filtered_logs`



---


### `get_door_name_from_controller`



---


### `test_connection_and_authentication`



---


### `enumerate_controller_list_info`



---


### `save_cardholder_setting`



---


### `enumerate_door_info`



---


### `clear_logs_surveillance_station`



---


### `list_all_user_privilege`



---


### `manual_lock_operation`



---


### `save_user_door_priv_setting`



---


### `list_all_logs`



---


### `delete_selected_controller`



---


### `retrieve_data_from_controller`



---


### `block_cardholder`



---


### `get_controller_count`



---


### `start_controller_search`



---


### `get_controller_search_result`



---


### `enumerate_digital_output`



---


### `save_digital_output_parameters`



---


### `long_polling_digital_output_status`



---


### `trigger_external_event`



---


### `get_list_io_modules`



---


### `get_io_port_list`



---


### `get_supported_list_io_modules`



---


### `save_setting_io_module`



---


### `enable_io_modules`



---


### `disable_io_modules`



---


### `delete_io_modules`



---


### `test_connection_to_io_module`



---


### `get_capability_io_module`



---


### `configure_io_port_setting`



---


### `poll_trigger_state_io_module`



---


### `poll_do_trigger_module`



---


### `get_number_of_devices`



---


### `get_category_count_io_module`



---


### `start_search_io_module`



---


### `get_search_io_module_info`



---


### `get_current_camera_status`



---


### `enum_preset_camera_list`



---


### `get_preset_camera_capability`



---


### `record_current_camera_position`



---


### `delete_list_preset_camera`



---


### `go_specific_preset_by_given_speed`



---


### `set_current_camera_position`



---


### `enum_patrol_list`



---


### `enum_patrol_name_list`



---


### `load_patrol_detail`



---


### `add_or_modify_patrol`



---


### `delete_specific_patrol`



---


### `run_patrol`



---


### `stop_patrol`



---


### `toggle_home_mode`



---


### `get_home_mode_settings`



---


### `get_transaction_list`



---


### `get_all_transaction_list`



---


### `lock_history_records`



---


### `unlock_history_records`



---


### `delete_history_records`



---


### `start_session_with_specified_session_id`



---


### `complete_session_with_specified_id`



---


### `cancel_session_with_specified_session_id`



---


### `carry_data_into_session_id`



---


### `add_edit_active_vault_task`



---


### `login_source_server_get_info`



---


### `delete_archive_vault_task`



---


### `list_exist_archive_vault`



---


### `enable_archive_vault_task`



---


### `disable_archive_vault_task`



---


### `disable_archive_vault_batchedit_task`



---


### `get_batch_edit_progress`



---


### `get_batchedit_proress_info`



---


### `clean_batchedit_progress_data`



---


### `get_youtube_live_broadcast_setting`



---


### `set_youtube_live_broadcast_info`



---


### `close_youtube_live_broadcast`



---


### `get_deep_video_analytic`



---


### `create_edit_DVA_task`



---


### `delete_dva_task`



---


### `enable_dva_task`



---


### `disable_dva_task`



---


### `reset_counter_people_counting_task`



---


### `get_people_enter_leave_count`



---


### `get_people_count_of_day`



---


### `list_people_counting_task`



---


### `delete_recording_file_of_detection`



---


### `get_info_of_task_and_frame`



---


### `lock_recording_file_of_detection`



---


### `unlock_recording_file_of_detection`



---


### `get_info_people_counting_task`



---


### `create_people_counting_task`



---


### `modify_setting_of_people_counting_task`



---


### `delete_task_group`



---


### `start_count_people_task_in_groups`



---


### `stop_count_people_task_in_groups`



---


### `get_number_counting_task_group`



---


### `lock_recording_file_result`



---


### `get_face_list_task`



---


### `create_or_edit_task`



---


### `delete_face_task`



---


### `enable_task_to_start_detection_recording`



---


### `disable_task_to_stop_detection_recording`



---


### `list_task_with_privilege_to_watch`



---


### `create_face_group`



---


### `disable_face_grooup`



---


### `edit_face_group`



---


### `get_face_group_list`



---


### `count_face_groups`



---


### `detect_faces_image`



---


### `create_registered_face`



---


### `delete_registered_face`



---


### `edit_registered_face`



---


### `list_registered_face`



---


### `count_registered_face`



---


### `search_registered_face`



---


### `get_face_result_list`



---


### `delete_face_result`



---


### `lock_face_result`



---


### `unlock_face_result`



---


### `get_recording_file_of_face_info`



---


### `get_recognition_face_information`



---


### `correct_face_result`



---


### `mark_face_result_as_stranger`



---


### `add_new_bookmark`



---


### `delete_bookmark`



---


### `list_bookmark_detail`



---


### `list_camera_model`
Get list of camera model available  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Preload` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of camera model in cameraModel, list of camera capabilities in camCap and a tempCamInfo  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "camCap": [{...}],
        "cameraModel": [{...}*8000],
        "tempCamInfo": {...}
    },
    "success": true
}
```
</details>



---


### `list_audio_pattern`
Get list of audio patterns  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.AudioPattern` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of audio patterns  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "audioPattern": [
            {
                "desc": "system default pattern 1",
                "fmt": ".mp3",
                "id": 1,
                "isDefault": true,
                "length": 8,
                "name": "Alarm Sound"
            },
            {
                "desc": "system default pattern 2",
                "fmt": ".mp3",
                "id": 2,
                "isDefault": true,
                "length": 40,
                "name": "Alarm beeping"
            },
            {
                "desc": "system default pattern 3",
                "fmt": ".mp3",
                "id": 3,
                "isDefault": true,
                "length": 28,
                "name": "Digital alarm clock beeping"
            },
            {
                "desc": "system default pattern 4",
                "fmt": ".mp3",
                "id": 4,
                "isDefault": true,
                "length": 5,
                "name": "Bell"
            },
            {
                "desc": "system default pattern 5",
                "fmt": ".mp3",
                "id": 5,
                "isDefault": true,
                "length": 20,
                "name": "Dog bark"
            },
            {
                "desc": "system default pattern 6",
                "fmt": ".mp3",
                "id": 6,
                "isDefault": true,
                "length": 31,
                "name": "Emergency SFX"
            },
            {
                "desc": "system default pattern 7",
                "fmt": ".mp3",
                "id": 7,
                "isDefault": true,
                "length": 10,
                "name": "Mans voice saying Hello"
            },
            {
                "desc": "system default pattern 8",
                "fmt": ".mp3",
                "id": 8,
                "isDefault": true,
                "length": 6,
                "name": "Mans voice saying Stop"
            },
            {
                "desc": "system default pattern 9",
                "fmt": ".mp3",
                "id": 9,
                "isDefault": true,
                "length": 9,
                "name": "Siren"
            },
            {
                "desc": "system default pattern 10",
                "fmt": ".mp3",
                "id": 10,
                "isDefault": true,
                "length": 18,
                "name": "Warning Signal Danger"
            }
        ],
        "total": 10
    },
    "success": true
}
```
</details>



---


### `list_share`
List share for recordings  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Share` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of shared folder for recordings  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "sharelist": [
            {
                "blAutoMount": false,
                "blHidden": true,
                "blMigrating": false,
                "camCnt": 1,
                "description": "",
                "displayName": "surveillance / volume1",
                "enableRecLimit": false,
                "encType": 0,
                "mountSource": "",
                "mountStatus": 0,
                "mountType": 0,
                "quota": 192,
                "recLimitGB": 100,
                "shareDsId": 0,
                "shareId": 1,
                "shareIdOnRec": 0,
                "shareName": "surveillance",
                "sharePath": "/volume1/surveillance",
                "shareVolume": "volume1",
                "volumeFormat": 3
            }
        ],
        "total": 1
    },
    "success": true
}
```
</details>



---


### `check_license_quota`
Check license quota if cameras in camList in added  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.License` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_camList_** `List[dict]`  
List of camera(s), here is example of a list of dict of the camera:
```json
[{"ip": "10.13.22.141", "model": "DCS-3110", "vendor": "DLink", "port": 80}]
```  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Infos about licenses and server  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "ServersList": [
            {
                "afterAdding": 2, 
                "beforeAdding": 1,
                "dsId": 0,        
                "platformMax": 40 
            }
        ],
        "licenseAvailable": 1,    
        "licenseNeeded": 1
    },
    "success": true
}
```
</details>



---


### `start_camera_search_process`
Start the camera search process, return a PID  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Search` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
pid that is used in the `get_camera_search_info` as parameter  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "pid": 12773
    },
    "success": true
}
```
</details>



---


### `get_camera_search_info`
Get result of the search, this need to be call cyclic until result `searchStatus` is `False` (around 1min)  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
pid that is given in response of the `start_camera_search_process`  
  
**_offset_** `int`  
Offset in the camera found. Defaults to `0`  
  
**_blIncludeOverSSLCap_** `bool`  
Include camera that support SSL. Defaults to `True`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
List of cameras with infos found between last call of the request  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "camCount": 1,
        "camList": [
            {
                "WiFiSSID": "",
                "blActivated": false,
                "blHasOverSSLCap": false,
                "blNativeIntegrated": false,
                "blOverSSL": false,
                "ip": "192.168.1.15",
                "mac": "3E:5F:9C:A6:D7:1F",
                "model": "BUILD_687",
                "operationMode": "",
                "port": 8080,
                "serialNumber": "",
                "vendor": "ONVIF"
            }
        ],
        "searchStatus": true
    },
    "success": true
}
```
</details>



---


### `start_camera_search_iprange_process`
Start the camera search process with IP / port range and model list, return a PID  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_ip_** `str`  
Start IP address for the search  
  
**_end_ip_** `str`  
End IP address for the search  
  
**_start_port_** `int`  
Start port for the search.  
  
**_end_port_** `int`  
Start port for the search.  
  
**_model_list_** `List[dict]`  
List of dict that define models to search.
Here is an example:
```json
[{"vendor":"ONVIF","model":"Generic_ONVIF","usr":"YOUR_CAMERA_USERNAME","pass":"YOUR_CAMERA_PASSWORD","isOverHTTPS":false}]
```  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
pid that is used in the `get_camera_search_iprange_info` as parameter  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "pid": 20228
    },
    "success": true
}
```
</details>



---


### `get_camera_search_iprange_info`
Get result of the search from IP range, this need to be call cyclic until result `searchStatus` is `False` (around 200s in my test)  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SurveillanceStation.Camera.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pid_** `int`  
pid that is given in response of the `start_camera_search_iprange_process`  
  
**_offset_** `int`  
Offset in the camera found. Defaults to `0`  
  
**_blIncludeOverSSLCap_** `bool`  
Include camera that support SSL. Defaults to `True`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
List of cameras with infos found between last call of the request  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "camCount": 1,
        "camList": [
            {
                "WiFiSSID": "",
                "blActivated": false,
                "blHasOverSSLCap": false,
                "blNativeIntegrated": false,
                "blOverSSL": false,
                "ip": "192.168.1.15",
                "mac": "3E:5F:9C:A6:D7:1F",
                "model": "BUILD_687",
                "operationMode": "",
                "port": 8080,
                "serialNumber": "",
                "vendor": "ONVIF"
            }
        ],
        "searchStatus": true
    },
    "success": true
}
```
</details>



---


