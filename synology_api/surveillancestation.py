from __future__ import annotations
from typing import Optional, Any, List
from . import base_api
import json
from enum import Enum


class SurveillanceStation(base_api.BaseApi):

    def surveillance_station_info(self) -> dict:
        """Get infos about surveillance station and the server
        
            Returns
            -------
            dict
                Informations about surveillance station and the server
        
            Example return
            ----------
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
        """
        
        
        api_name = 'SYNO.SurveillanceStation.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'GetInfo'
        }

        return self.request_data(api_name, api_path, req_param)

    def camera_save(self, id: str = None,
                    name: str = None,
                    dsld: int = None,
                    newName: str = None,
                    ip: str = None,
                    port: int = None,
                    vendor: str = None,
                    model: str = None,
                    userName: str = None,
                    password: str = None,
                    videoCodec: int = None,
                    audioCodec: int = None,
                    tvStandard: int = None,
                    channel: str = None,
                    userDefinePath: str = None,
                    fov: str = None,
                    streamXX: Any = None,
                    recordTime: int = None,
                    preRecordTime: int = None,
                    postRecordTime: int = None,
                    enableRecordingKeepDays: bool = None,
                    recordingKeepDays: int = None,
                    enableRecordingKeepSize: bool = None,
                    recordingKeepSize: int = None,
                    enableLowProfile: bool = None,
                    recordSchedule: list[int] = None,
                    rtspPathTimeout: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def camera_list(self, idList: str = "", blFromCamList: bool = False, offset: int = 0, limit: int = 0, blIncludeDeletedCam: bool = True,
                privCamType: int = 3, basic: bool = True, streamInfo: bool = True, blPrivilege: bool = True, camStm: int = 2,
                blGetMulticastInfo: bool = True, videoCapInfo: bool = False, eventDetection: bool = True, ptz: bool = True,
                fisheye: bool = True, deviceOutCap: bool = True, liveviewAnalytics: bool = True, ioList: bool = True, optimize: bool = True
            ) -> dict:
        """Get camera list with a lot of options
        
            Parameters
            ----------
            idList : str, optional
                The list of <CAMERA_ID> to be queried concatenated by ",". Defaults to `""`
            blFromCamList : bool, optional
                Indicating if the caller is from cam list. Defaults to `False`
            offset : int, optional
                The offset to be shifted in the total result. Defaults to `0`
            limit : int, optional
                Number of cameras to be returned.. Defaults to `0`
            blIncludeDeletedCam : bool, optional
                Indicating if deleted cameras should be listed or not. Defaults to `True`
            privCamType : int, optional
                Weighted sum indicated the types of the camera. Defaults to `3`
                    0x00: NONE
                    0x01: LIVEVIEW
                    0x02: PLAYBACK
                    0x04: LENS
                    0x08: AUDIO.
            basic : bool, optional
                Indicating to show basic settings or not. Defaults to `True`
            streamInfo : bool, optional
                Indicating to show streaming information or not. Defaults to `True`
            blPrivilege : bool, optional
                Indicating if the user privilege should be checked or not. Defaults to `True`
            camStm : int, optional
                Stream number of the camera live view
                    • 0: Live stream
                    • 1: Recording stream
                    • 2: Mobile stream (default value)
                Defaults to `2`
            blGetMulticastInfo : bool, optional
                Indicating to show multicast infos or not. Defaults to `True`
            videoCapInfo : bool, optional
                Indicating to show video capabilities or not. Defaults to `False`
            eventDetection : bool, optional
                Indicating to show event detection or not. Defaults to `True`
            ptz : bool, optional
                Indicating to show ptz info or not. Defaults to `True`
            fisheye : bool, optional
                Indicating to show fisheye info or not. Defaults to `True`
            deviceOutCap : bool, optional
                Indicating to show deviceOutCap info or not. Defaults to `True`
            liveviewAnalytics : bool, optional
                Indicating to show liveviewAnalytics info or not. Defaults to `True`
            ioList : bool, optional
                Indicating to show ioList info or not. Defaults to `True`
            optimize : bool, optional
                Optimize. Defaults to `True`
        
            Returns
            -------
            dict
                A lot of informations about each camera
        
            Example return
            ----------
            
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
        """

        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'List',
            "blIncludeDeletedCam": blIncludeDeletedCam,
            "blGetMulticastInfo": blGetMulticastInfo,
            "basic": basic,
            "streamInfo": streamInfo,
            "videoCapInfo": videoCapInfo,
            "eventDetection": eventDetection,
            "blPrivilege": blPrivilege,
            "ptz": ptz,
            "fisheye": fisheye,
            "deviceOutCap": deviceOutCap,
            "liveviewAnalytics": liveviewAnalytics,
            "ioList": ioList,
            "optimize": optimize,
            "privCamType": privCamType,
            "blFromCamList": blFromCamList,
            "idList": idList,
            "limit": limit,
            "offset": offset,
            "camStm": camStm,
        }

        return self.request_data(api_name, api_path, req_param)

    def get_camera_info(self, cameraIds: int = None, privCamType: int = 1,  blIncludeDeletedCam: bool = True,
                basic: bool = True, streamInfo: bool = True, optimize: bool = True, ptz: bool = True,
                eventDetection: bool = True, deviceOutCap: bool = True, fisheye: bool = True, camAppInfo: bool = True
            ) -> dict[str, object] | str:
        '''
        This function return information about a camera.
        
        cameraIds : This parameter is named cameraIds in the API documentation but it refer to 1 camera ID
        
        privCamType: int = 1
            SYNO.SS.CamPriv.LIVEVIEW = 1;
            SYNO.SS.CamPriv.PLAYBACK = 2;
            SYNO.SS.CamPriv.LENS = 4;
            SYNO.SS.CamPriv.AUDIO = 8;
            SYNO.SS.CamPriv.DIGIOUT = 16;
        
        All other parameters must be let to default value
        '''

        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def camera_list_group(self,
                          offset: int = None,
                          limit: int = None) -> dict[str, object] | str:

        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_snapshot(self,
                          id: Any = None,
                          name: str = None,
                          dsld: int = None,
                          profileType: int = 1) -> str:
        ''' By default, the profileType is 1, which is the default profile.
        Binary data is returned, so the response is not a json object.
        '''
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val
        ## Make sure to disable json response, as the response is a binary file
        ## Return only the content of the response where binary data is stored
        return self.request_data(api_name, api_path, req_param, response_json=False).content

    def enable_camera(self, 
                      idList: str = None,
                      blIncludeDeletedCam: bool = False) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}
        
        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_camera(self, 
                       idList: str = None,
                       blIncludeDeletedCam: bool = False) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}
        
        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_capability_by_cam_id(self, cameraId: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCapabilityByCamId', 'cameraId': cameraId}

        return self.request_data(api_name, api_path, req_param)

    def count_occupied_size(self, camId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetOccupiedSize', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    def is_shortcut_valid(self, cameraId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckCamValid', 'cameraId': cameraId}

        return self.request_data(api_name, api_path, req_param)

    def get_live_path(self, idList: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetLiveViewPath', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def audio_event_enum(self, camId: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AudioEnum', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    def alarm_event_enum(self, camId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AlarmEnum', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    def md_parameter_save(self, camId: int = None,
                         source: int = None,
                         mode: int = None,
                         sensitivity: int = None,
                         threshold: int = None,
                         objectSize: int = None,
                         percentage: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'MDParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def motion_event_enum(self, camId: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'MotionEnum', 'camId': camId}

        return self.request_data(api_name, api_path, req_param)

    def motion_parameter_save(self,
                              camId: int = None,
                              source: int = None,
                              mode: int = None,
                              keep: bool = None,
                              level: int = None) -> dict[str, object] | str:

        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ADParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def di_parameter_save(self,
                          camId: int = None,
                          idx: int = None,
                          keep: bool = None,
                          normal: int = None) -> dict[str, object] | str:

        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DIParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def alarm_sts_polling(self,
                          camId: int = None,
                          timeOut: int = None,
                          keep: Any = None) -> dict[str, object] | str:  # TODO not working

        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AlarmStsPolling'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def td_parameter_save(self,
                          camId: int = None,
                          source: int = None,
                          keep: Any = None,
                          duration: int = None) -> dict[str, object] | str:

        api_name = 'SYNO.SurveillanceStation.Camera.Event'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TDParamSave'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_camera_group(self, privCamType: int = None) -> dict[str, object] | str:

        api_name = 'SYNO.SurveillanceStation.Camera.Group'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum', 'privCamType': privCamType}

        return self.request_data(api_name, api_path, req_param)

    def save_specific_group(self, groupList: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Camera.Group'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save', 'groupList': groupList}

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_groups(self, Id: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera.Group'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete', 'id': Id}

        return self.request_data(api_name, api_path, req_param)

    def enumerate_group_information(self, camServerId: int = None,
                                    shareName: str = None,
                                    archiveName: str = None,
                                    camlist: Any = None,
                                    actFromHost: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera.Import'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_camera_from_archive(self,
                                    shareName: str = None,
                                    archiveName: str = None,
                                    serverId: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Camera.Import'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ArchiveCamEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_archive_from_folder(self,
                                          shareName: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera.Import'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ArchiveEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_available_size_of_sdcard(self,
                                       camId: Any = None,
                                       host: str = None,
                                       port: str = None,
                                       user: str = None,
                                       passw: str = None,
                                       vendor: str = None,
                                       model: str = None,
                                       ch: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ArchiveEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key is passw:
                        req_param[str('pass')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_licence_quota(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckQuota'}

        return self.request_data(api_name, api_path, req_param)

    def format_specific_sd_card(self,
                                camId: Any = None,
                                host: str = None,
                                port: str = None,
                                user: str = None,
                                passw: str = None,
                                vendor: str = None,
                                model: str = None,
                                ch: str = None,
                                timeout: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'FormatSDCard'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key is passw:
                        req_param[str('pass')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def quick_create_single_camera(self,
                                   camServerId: Any = None,
                                   actFromHost: bool = None,
                                   camStreamingType: str = None,
                                   camName: str = None,
                                   camIP: str = None,
                                   camPort: str = None,
                                   camVendor: str = None,
                                   camModel: str = None,
                                   camMountType: int = None,
                                   camChannel: str = None,
                                   camVideoType: str = None,
                                   camAudioType: str = None,
                                   camSourcePath: str = None,
                                   camUserName: str = None,
                                   camPassWord: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Camera.Wizard'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'QuickCreate'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_camera_lens(self,
                         cameraId: Any = None,
                         direction: str = None,
                         speed: int = None,
                         moveType: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Move'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def camera_lens_zoom(self,
                         cameraId: Any = None,
                         control: Any = None,
                         moveType: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Zoom'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_preset_ptz_camera(self,
                               cameraId: Any = None,
                               offset: int = None,
                               limit: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_camera_lens_to_preset_position(self,
                                            cameraId: Any = None,
                                            presetId: Any = None,
                                            position: Any = None,
                                            speed: Any = None,
                                            type: Any = None,
                                            isPatrol: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GoPreset'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_patrol_cameras(self,
                            cameraId: Any = None,
                            offset: int = None,
                            limit: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListPatrol'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def force_cam_to_execute_patrol(self,
                                    cameraId: Any = None,
                                    patrolId: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RunPatrol'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def focus_camera(self,
                     cameraId: Any = None,
                     control: Any = None,
                     moveType: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Focus'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def control_camera_iris_in_out(self,
                                   cameraId: Any = None,
                                   control: Any = None,
                                   moveType: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Iris'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def auto_focus(self, cameraId: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AutoFocus'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_cam_lens_to_absolute_position(self,
                                           posX: int = None,
                                           posY: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AbsPtz'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def move_cam_to_home_position(self,
                                  cameraId: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Home'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def auto_pan_camera(self,
                        cameraId: Any = None,
                        moveType: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AutoPan'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_stop_object_tracking(self,
                                   cameraId: Any = None,
                                   moveType: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ObjTracking'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_stop_external_recording(self,
                                      cameraId: Any = None,
                                      action: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ExternalRecording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Record'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def query_event_list_by_filter(self,
                                   offset: int = None,
                                   limit: int = None,
                                   cameraIds: str = None,
                                   fromTime: int = None,
                                   toTime: int = None,
                                   dsld: int = None,
                                   mountId: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_recordings(self,
                          idList: int = None,
                          dsld: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_events_by_filter(self,
                                reason: str = None,
                                cameraIds: str = None,
                                fromTime: Any = None,
                                toTime: Any = None,
                                locked: int = None,
                                evtSrcType: int = None,
                                evtSrcId: int = None,
                                blIncludeSnapshot: bool = None,
                                includeAllCam: bool = None,
                                from_end: int = None,
                                from_start: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteFilter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_all_recordings(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteAll'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def apply_settings_advance_tab(self,
                                rotateUnrecogCam: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ApplyAdvanced'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_by_number_of_event(self,
                                 offset: bool = None,
                                 limit: int = None,
                                 reason: str = None,
                                 cameraIds: str = None,
                                 fromTime: int = None,
                                 toTime: int = None,
                                 locked: int = None,
                                 evtSrcType: int = None,
                                 evtSrcId: int = None,
                                 blIncludeSnapshot: bool = None,
                                 includeAllCam: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def keep_event_play_alive(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Keepalive'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def stop_recording_event(self,
                                 idList: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Trunc'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def load_settings_in_advanced_tab(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LoadAdvanced'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_selected_event(self,
                                 reason: str = None,
                                 cameraIds: str = None,
                                 fromTime: int = None,
                                 toTime: int = None,
                                 locked: int = None,
                                 evtSrcType: int = None,
                                 evtSrcId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LockFilter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_selected_event(self,
                                 idList: str = None,
                                 dsld: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_selected_filter_event(self,
                                     reason: str = None,
                                     cameraIds: str = None,
                                     fromTime: int = None,
                                     toTime: int = None,
                                     locked: int = None,
                                     evtSrcType: int = None,
                                     evtSrcId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'UnlockFilter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_selected_recordings(self,
                                 idList: str = None,
                                 dsld: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_recordings(self,
                            id: int = None,
                            mountId: int = None,
                            offsetTimeMs: int = None,
                            playTimeMs: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Download'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param, response_json=False)

    def check_if_recording_playable(self,
                            eventId: int = None,
                            chkDetail: bool = None,
                            mountId: int = None,
                            dsld: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckEventValid'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def play_specific_recording(self,
                                recordingId: int = None,
                                alertRecording: bool = None,
                                mountId: int = None,
                                dsld: int = None,
                                videoCodec: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Stream'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_merged_recording_files(self,
                            camId: int = None,
                            fromTime: int = None,
                            toTime: int = None,
                            fileName: str = None) -> dict[str, object] | str:  # TODO not working

        """Download the merged files of UTC time range recordings of target camera.
           If there are different resolution or codec within UTC time range, the recordings will merge as much as possible
           and downlod file will be a zip file.

           This method will start a task which have keep-alive mechanism.
           Use GetRangeExportProgress method to get newest progress and keep-alive.
           After receiving progress 100, use OnRangeExportDone method to download exported recording within 1
           minutes.
           If you want to cancel range export task, just do not send GetRangeExportProgress method or
           OnRangeExportDone method. System will cleanup processed files itself."""

        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RangeExport'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_newest_progress_keep_alive(self, dlid: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetRangeExportProgress'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_recording_from_target(self,
                                       dlid: int = None,
                                       fileName: str = None) -> dict[str, object] | str:  # TODO not working

        """Response
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
           439 Too many items selected."""

        api_name = 'SYNO.SurveillanceStation.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'OnRangeExportDone'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def handle_load_event_export(self,
                                 start: int = None,
                                 limit: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_name_export_event(self,
                                dsId: int = None,
                                name: int = None,
                                share: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckName'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_information_list(self,
                                dslld: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CamEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_destination_folder_availability(self,
                                              freeSize: int = None,
                                              startTime: int = None,
                                              stopTime: int = None,
                                              camIdList: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckAvailableExport'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def handle_save_event_export(self,
                                 name: str = None,
                                 srcDsId: int = None,
                                 dstDsId: int = None,
                                 dstdir: str = None,
                                 freesize: int = None,
                                 start_time: int = None,
                                 stop_time: int = None,
                                 isoverwrite: int = None,
                                 camlistid: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_event_export_info_from_recording_server(self,
                                                    start_time: int = None,
                                                    stop_time: int = None,
                                                    camlistid: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording.Export'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetEvtExpInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def load_event_mount(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Recording.Mount'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def redirect_webapi_to_target_ds(self,
                                     dsId: int = None,
                                     webAPI: Any = None) -> dict[str, object] | str:  # TODO not working

        """webAPI Array of `webAPI_info`

           Example:
           `webAPI={"api": "SYNO.SurveillanceStation.AddOns", "version": 1, "method":
           "List"}` """

        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Redirect'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def modify_share_privilege(self,
                               privSet: int = None,
                               shareName: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def apply_option_settings(self,
                              central_auto_video_relay: bool = None,
                              central_enable: bool = None,
                              central_mode: str = None,
                              central_rec_mask_mode: bool = None,
                              central_rec_sync_time: bool = None,
                              nvr_enable: bool = None,
                              nvr_lang: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ApplyOption'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_cms_info(self,
                     isPolling: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_log_recording_data_from_target_ds(self,
                                              syncType: int = None,
                                              syncTargetId: int = None,
                                              limit: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DoSyncData'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_samba_service(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckSambaEnabled'}

        return self.request_data(api_name, api_path, req_param)

    def check_if_samba_on_and_rec_enabled(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'BatCheckSambaService'}

        return self.request_data(api_name, api_path, req_param)

    def get_encoded_single_image_of_camera(self,
                                           camId: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetMDSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_cms_status(self,
                       camId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCMSStatus'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_smb_service(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableSamba'}

        return self.request_data(api_name, api_path, req_param)

    def notify_slave_ds_to_disconnect(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'NotifyCMSBreak'}

        return self.request_data(api_name, api_path, req_param)

    def lock_recording_server_prevent_setting_change(self,
                                                     locked: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LockSelf'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_ds_into_recording_server(self,
                                        adminUsername: str = None,
                                        adminPasswd: str = None,
                                        central_rec_mask_mode: str = None,
                                        central_rec_sync_time: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableCMS'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unpair_recording_servers(self,
                                 adminUsername: str = None,
                                 key: str = None,
                                 mac: str = None,
                                 cmsMode: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'UnPair'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_free_memory_size(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetFreeSpace'}

        return self.request_data(api_name, api_path, req_param)

    def handle_slave_ds(self,
                        lock: bool = None,
                        adminUsername: str = None,
                        key: str = None,
                        mac: str = None,
                        masterAuthKey: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_target_ds_info(self,
                           slaveDslp: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Test'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def logout_slave_ds(self,
                        adminUsername: str = None,
                        key: str = None,
                        mac: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Logout'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def pair_slave_ds(self,
                      dsname: str = None,
                      slaveDslp: str = None,
                      port: int = None,
                      masterAuthKey: str = None,
                      model: str = None,
                      mac: str = None,
                      cms_locked: bool = None,
                      cms_masked: bool = None,
                      cms_sync_time: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Pair'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def login_slave_ds(self,
                        adminUsername: str = None,
                        key: str = None,
                        mac: str = None,
                       masterAuthKey: str = None,
                       hostName: str = None,
                       hostPort: int = None,
                       ignoreAuthError: str = None,
                       hostDisconnect: bool = None,
                       blUpdateVolSpace: bool = None,
                       enable_rec: bool = None,
                       cms_locked: bool = None,
                       cms_masked: bool = None,
                       cms_sync_time: bool = None) -> dict[str, object] | str:  # TODO not working

        """2.3.15.9 API Error Code
            Code Description
            400 Execution failed.
            401 Invalid parameter.
            415 message connect failed. """

        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Login'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_slave_ds(self,
                      slavedsName: str = None,
                      slavedsModel: str = None,
                      slavedsPort: int = None,
                      slavedsVersion: str = None,
                      slavedsMaxCamNum: int = None,
                      slavedsId: str = None,
                      slavedsIP: str = None,
                      slavedsEnable: int = None,
                      slavedsCamCnt: bool = None,
                      adminUsername: str = None,
                      adminPasswd: str = None,
                      cms_locked: bool = None,
                      cms_masked: bool = None,
                      cms_sync_time: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.CMS.GetDsStatus'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def load_slave_ds_list(self,
                      blNeedStatus: bool = None,
                      blGetSortInfo: bool = None,
                      blRuntimeInfo: bool = None,
                      dslds: str = None,
                      sortInfo: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.CMS.SlavedsList'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_number_of_logs(self,
                             slavedsName: str = None,
                             start: int = None,
                             limit: int = None,
                             level: str = None,
                             filterCamera: str = None,
                             cameraIds: str = None,
                             dsfrom: int = None,
                             to: int = None,
                             keyword: str = None,
                             keywordDsId: str = None,
                             time2String: str = None,
                             dsId: str = None,
                             srcType: int = None,
                             timezoneOffset: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_selected_logs(self,
                            blClearAll: bool = None,
                            level: int = None,
                            dsId: int = None,
                            filterCamera: str = None,
                            cameraIds: str = None,
                            dsfrom: int = None,
                            to: int = None,
                            keyword: str = None,
                            keywordDsId: str = None,
                            srcType: int = None,
                            timezoneOffset: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Clear'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_information_log(self,
                            start: int = None,
                            limit: int = None,
                            level: str = None,
                            filterCamera: str = None,
                            cameraIds: str = None,
                            dsfrom: int = None,
                            to: int = None,
                            keyword: str = None,
                            keywordDsId: str = None,
                            time2String: str = None,
                            dsId: int = None,
                            srcType: int = None,
                            all: bool = None,
                            blIncludeRecCnt: str = None,
                            blIncludeAuInfo: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_advanced_settings_logs(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def set_advanced_setting_logs(self,
                            data: Any = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetSetting', 'data': data }

        """data example:
        
           data=[{"SSLogType":321912835,"enable":1},{"SSLogType":321912836,"enable":0}]"""

        return self.request_data(api_name, api_path, req_param)

    def load_license_data(self,
                            num_only: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.License'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load', 'num_only': num_only}

        return self.request_data(api_name, api_path, req_param)


    def get_http_video_stream(self,
                              writeHeader: bool = None,
                              analyevent: bool = None,
                              mountId: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Stream'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EventStream'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_action_rule(self,
                         id: int = None,
                         name: str = None,
                         ruleType: int = None,
                         actType: int = None,
                         evtSrc: int = None,
                         evtDsId: int = None,
                         evtDevId: int = None,
                         evtId: int = None,
                         evtItem: int = None,
                         evtMinIntvl: int = None,
                         Actions: Any = None,
                         actSchedule: str = None,
                         Id: int = None,
                         actSrc: int = None,
                         actDsId: int = None,
                         actDevId: int = None,
                         actId: int = None,
                         actTimes: int = None,
                         actTimeUnit: int = None,
                         actTimeDur: int = None,
                         actItemId: int = None,
                         actRetPos: int = None,
                         extUrl: str = None,
                         userName: str = None,
                         password: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_action_rule(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DownloadHistory'}

        return self.request_data(api_name, api_path, req_param)

    def send_data_2_player(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SendData2Player'}

        return self.request_data(api_name, api_path, req_param)

    def delete_all_histories_of_action_rule(self, idList: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteHistory', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def list_action_rules(self, start: str = None, limit: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List', 'Start': start, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def disable_action_rules(self, idList: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def enable_action_rules(self, idList: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def list_history_action_rules(self, start: int = None, limit: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListHistory', 'start': start, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def delete_action_rule(self, idList: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.ActionRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete', 'idList': idList}

        return self.request_data(api_name, api_path, req_param)

    def get_list_of_emaps(self,
                          start: int = None,
                          limit: str = None,
                          emapIds: int = None,
                          includeItems: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Emap'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_specific_emaps_setting(self,
                                   emapIds: int = None,
                                   includeImage: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Emap'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_emap_image(self,
                       filename: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Emap.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_autorized_ds_token(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetRegisterToken'}

        return self.request_data(api_name, api_path, req_param)

    def set_message_event(self,
                          eventTypes: str = None,
                          subject: str = None,
                          content: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetCustomizedMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_message_event(self,
                          eventTypes: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetCustomizedMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_notification_sender_name(self,
                                     ss_pkg_name: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetVariables'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_notification_sender_name(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetVariables'}

        return self.request_data(api_name, api_path, req_param)

    def set_advanced_notification_setting(self,
                                          blSyncDSMNotify: bool = None,
                                          blCompactMsg: bool = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetAdvSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_advanced_notification_setting(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Notification'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetAdvSetting'}

        return self.request_data(api_name, api_path, req_param)

    def send_test_mesg_to_primary_secondary_phone(self,
                                                  smsEnable: bool = None,
                                                  smsMethod: int = None,
                                                  smsProvider: str = None,
                                                  userName: str = None,
                                                  password: str = None,
                                                  confirmPassword: str = None,
                                                  primaryPhoneCode: str = None,
                                                  primaryPhonePrefix: str = None,
                                                  secondaryPhoneCode: str = None,
                                                  secondaryPhonePrefix: str = None,
                                                  secondaryPhoneNumber: str = None,
                                                  setMinMessageInterval: bool = None,
                                                  minMessageInterval: int = None,
                                                  hasSysSms: bool = None,
                                                  apiId: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SendTestMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_setting_notification_sms(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def set_sms_service_setting(self,
                                smsEnable: bool = None,
                                smsMethod: int = None,
                                smsProvider: str = None,
                                userName: str = None,
                                password: str = None,
                                confirmPassword: str = None,
                                primaryPhoneCode: str = None,
                                primaryPhonePrefix: str = None,
                                secondaryPhoneCode: str = None,
                                secondaryPhonePrefix: str = None,
                                secondaryPhoneNumber: str = None,
                                setMinMessageInterval: bool = None,
                                minMessageInterval: int = None,
                                hasSysSms: bool = None,
                                apiId: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def send_test_sms(self,
                      attachSnapshot: bool = None,
                      enableInterval: bool = None,
                      mobileEnable: bool = None,
                      msgInterval: str = None,
                      primaryEmail: str = None,
                      secondaryEmail: str = None,
                      synoMailEnable: bool = None,
                      mail_recipient: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SendTestMessage'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def send_test_mail(self,
                       attachSnapshot: bool = None,
                       enableInterval: bool = None,
                       mobileEnable: bool = None,
                       msgInterval: str = None,
                       primaryEmail: str = None,
                       secondaryEmail: str = None,
                       synoMailEnable: bool = None,
                       mail_recipient: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.PushService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SendVerificationMail'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_mobile_paired_devices(self,
                                   attachSnapshot: bool = None,
                                   enableInterval: bool = None,
                                   mobileEnable: bool = None,
                                   msgInterval: str = None,
                                   primaryEmail: str = None,
                                   secondaryEmail: str = None,
                                   synoMailEnable: bool = None,
                                   mail_recipient: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Notification.PushService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListMobileDevice'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unpair_device(self,
                      targetIds: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Notification.PushService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_controller_access_schedule(self,
                      targetIds: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetAccessControlControllerSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_alarm_schedule(self,
                                  cameraId: int = None,
                                  alarmdx: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCameraAlarmSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_sys_dependent_schedule(self,
                                  eventGroupTypes: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSystemDependentSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_batch_schedule(self,
                           eventTypes: str = None,
                           schedule: Any = None,
                           cameraIds: str = None,
                           cameraGroupIds: str = None,
                           filter: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetBatchSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_access_ctrl_door_schedule(self,
                                      doorId: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetAccessControlDoorSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_schedule(self,
                            cameraId: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCameraSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_sys_dependent_schedule(self,
                                   eventType: int = None,
                                   schedule: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetSystemDependentSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_controller_access_schedule(self,
                                       eventType: int = None,
                                       schedule: Any = None,
                                       doorId: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetAccessControlSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_camera_schedule(self,
                            eventType: int = None,
                            schedule: Any = None,
                            cameraId: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Schedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetCameraSchedule'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_notification_email_string(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Notification.Email'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def set_adv_tab_info_filter(self,
                                X: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.Email'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Set'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_sms_service_provider(self,
                                    providerName: str = None,
                                    providerPort: int = None,
                                    providerUrl: str = None,
                                    providerTemplate: str = None,
                                    providerSepChar: str = None,
                                    providerNeedSSL: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Notification.SMS.ServiceProvider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Create'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_sms_provider(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Notification.SMS.ServiceProvider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        return self.request_data(api_name, api_path, req_param)

    def delete_sms_service_provider(self,
                                    providerName: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Notification.SMS.ServiceProvider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_addson_to_update(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetUpdateInfo'}

        return self.request_data(api_name, api_path, req_param)

    def enable_specific_addon(self,
                              service: int = None,
                              servicename: str = None) -> dict[str, object] | str: # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_specific_addon_update_info(self,
                       service: int = None) -> dict[str, object] | str: # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckUpdateInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_specific_addon_info(self,
                       service: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_total_addon_info(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        return self.request_data(api_name, api_path, req_param)

    def update_addon_package(self,
                             service: int = None,
                             filePath: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Update'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_addon_status(self,
                             service: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CheckEnableDone'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_addon(self,
                      service: int = None,
                      serviceName: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_addon_autoupdate(self,
                      service: int = None,
                      BlEnabled: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AddOns'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetAutoUpdate'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_camera_recording_server(self,
                                                camIdList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RecServClear'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_camera_event_analytic(self,
                                  camIdList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EventCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_selected_events(self,
                               dsIdList: str = None,
                               idList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ClearSelected'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_camera_events(self,
                               camIdList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EventCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_analytic_history(self,
                             camIdList: str = None,
                             typeListstring: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_analytic_history_by_filter(self,
                                       camIdList: str = None,
                                       dsId: int = None,
                                       lock: int = None,
                                       typeList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RecServerEnum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unklock_selected_events(self,
                                dsId: int = None,
                                idList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_camera_analytic_trigger(self,
                                       trigCamIdList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Trigger'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def flush_event_header(self,
                           eventId: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EventFlushHeader'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_selected_events(self,
                             dsId: int = None,
                             idList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_analytic_event_from_rec_server(self,
                                           camIdList: str = None,
                                           idList: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RecServerEventCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_analytic_settings(self,
                               camId: int = None,
                               type: int = None,
                               showFrame: bool = None,
                               showLine: bool = None,
                               showVirtualFence: bool = None,
                               beep: bool = None,
                               sens: int = None,
                               dwellTime: int = None,
                               direction: int = None,
                               objSize: int = None,
                               region: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Alert.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_if_snapshot_exist(self,
                               id: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ChkFileExist'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_snapshot_modification(self,
                                   id: int = None,
                                   createCopy: bool = None,
                                   width: int = None,
                                   height: int = None,
                                   byteSize: int = None,
                                   imageData: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Edit'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_snapshot_by_category(self,
                                   keyword: str = None,
                                   dsfrom: int = None,
                                   to: int = None,
                                   timezoneOffset: int = None,
                                   byteSize: int = None,
                                   imageData: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_any_locked_snapshot(self,
                                   id: str = None,
                                   dsfrom: int = None,
                                   to: int = None,
                                   keyword: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ChkContainLocked'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_snapshot_by_filter(self,
                                   dsfrom: int = None,
                                   to: int = None,
                                   keyword: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'UnlockFiltered'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_snapshot_information(self,
                                  idList: str = None,
                                  start: int = None,
                                  limit: int = None,
                                  dsfrom: int = None,
                                  to: int = None,
                                  keyword: str = None,
                                  imgSize: int = None,
                                  blIncludeAuInfo: bool = None,
                                  blIncludeRecCnt: bool = None,
                                  camId: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_snapshot(self,
                        objList: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def take_snapshot(self,
                      dsId: int = None,
                      camId: int = None,
                      blSave: bool = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TakeSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_snapshot_setting_function(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetSetting'}

        return self.request_data(api_name, api_path, req_param)

    def delete_snapshot_by_filter(self,
                                  deleteAllCommand: bool = None,
                                  dsfrom: int = None,
                                  to: int = None,
                                  keyword: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteFiltered'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    if key == 'dsfrom':
                        req_param[str('from')] = val
                    else:
                        req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_snapshot_image(self,
                           id: int = None,
                           imgSize: int = None) -> dict[str, object] | str:  # TODO to modify for download?
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LoadSnapshot'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_snapshot_image(self,
                            objList: Any = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def downld_single_snapshot(self,
                               id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Download'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_new_snapshot_setting(self,
                                  dispSnapshot: bool = None,
                                  dispDuration: int = None,
                                  limitTotalSize: bool = None,
                                  limitSizeInGb: int = None,
                                  addTimestamp: bool = None,
                                  timestampPosition: int = None)-> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_snapshot(self,
                      camName: str = None,
                      createdTm: int = None,
                      width: int = None,
                      height: int = None,
                      byteSize: int = None,
                      imageData: str = None)-> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def check_snapshot_status(self,
                              dispSnapshot: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.SnapShot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ChkSnapshotValid'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_visualstation(self,
                             vslist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def update_vs_network_config(self,
                                 vsMAc: str = None,
                                 ip: str = None,
                                 mask: str = None,
                                 gateway: str = None,
                                 blDhcp: bool = None,
                                 name: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ReqNetConfig'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_visualstation_by_id(self,
                                 vslist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_vs_owner_info(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        return self.request_data(api_name, api_path, req_param)

    def unlock_visualstation_by_id(self,
                                   vslist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_visualstation_by_id(self,
                                    vslist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_visualstation(self,
                                      vslist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_layout_visualstation(self,
                                       vsId: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_layout_information(self,
                                id: int = None,
                                vsId: int = None,
                                name: str = None,
                                canGrpId: int = None,
                                isDefault: int = None,
                                isFixAspectRatio: int = None,
                                layoutType: int = None,
                                channelList: Any = None,
                                customPosList: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_layout_visualstation(self,
                                    id: int = None,
                                    vsId: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_visualstation_search_result(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Start'}

        return self.request_data(api_name, api_path, req_param)

    def get_visualstation_ip_info(self,
                                  ip: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SearchIP'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def stop_previous_visualstation_search(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Stop'}

        return self.request_data(api_name, api_path, req_param)

    def get_visualstation_list(self,
                               offset: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.VisualStation.Layout'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'InfoGet'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_number_of_controller(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetUpdateInfo'}

        return self.request_data(api_name, api_path, req_param)

    def get_cardholder_count(self, filterKeyword: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountByCategoryCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_all_controllers_logger(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumLogConfig'}

        return self.request_data(api_name, api_path, req_param)

    def get_cardholder_photo(self,
                             photo_name: str = None,
                             isRedirectCgi: bool = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCardholderPhoto'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_log_count(self,
                      start: int = None,
                      limit: int = None,
                      filterType: int = None,
                      filterEventSource: Any = None,
                      filterSource: int = None,
                      filterEventSourceItem: int = None,
                      filterTimeFrom: int = None,
                      filterTimeTo: int = None,
                      filterKeyword: str = None,
                      timezoneOffset: int = None,
                      doorIds: str = None,
                      eventTypes: str = None,
                      update: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountByCategoryLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_cardholder_info(self,
                            start: int = None,
                            limit: int = None,
                            filterKeyword: str = None,
                            filterStatus: int = None,
                            filterCtrlerId: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def retrieve_last_access_credential(self,
                            ctrlerId: int = None,
                            idPtId: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'RetrieveLastCard'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_disable_controller(self,
                                  blEnable: bool = None,
                                  arrayJson: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableCtrler'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def acknowledge_all_alarm_level_log(self,
                                        start: int = None,
                                        limit: int = None,
                                        filterEventSource: Any = None,
                                        filterSource: int = None,
                                        filterEventSourceItem: str = None,
                                        filterTimeFrom: int = None,
                                        filterKeyword: str = None,
                                        doorIds: str = None,
                                        eventTypes: str = None,
                                        update: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AckAlarm'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def modify_controller_logger_config(self,
                                        data: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveLogConfig'}

        """data example:
        
        data={"log_evt":"11111111111111111111111111111111111111", 
              "id": 97, "log_alarm":"00111111111111111111111111111111111111"}"""

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_controller_settings(self,
                                 arrayJson: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        """arrayJson example:
        
           arrayJson="[{\"enable\":true,\"id\":97,\"name\":\"ctrler1\",\"host\":\"10.13.12.173\",\"port\":80,
                        \"model\":\"A1001\",\"username\":\"root\",\"password\":\"Q__Q-__-\",\"time_server\":
                        \"SurveillanceStation\",\"time_zone\":\"Fiji\",\"door\":[{\"id\":231,\"name\":\"FrontDoor\",
                        \"enable_cam\":true,\"cam_ds_id\":0,\"cam_id\":13}]}]\" """

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def download_filtered_logs(self,
                               start: int = None,
                               limit: int = None,
                               filterType: int = None,
                               filterEventSource: int = None,
                               filterSource: int = None,
                               filterEventSourceItem: str = None,
                               filterTimeFrom: int = None,
                               filterTimeTo: int = None,
                               filterKeyword: str = None,
                               doorIds: str = None,
                               eventTypes: str = None,
                               update: int = None) -> dict[str, object] | str:  # TODO to modify for download?
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DownloadLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_door_name_from_controller(self,
                                      ctrlerId: int = None,
                                      ip: str = None,
                                      port: int = None,
                                      userName: str = None,
                                      password: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetDoorNames'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def test_connection_and_authentication(self,
                                           ctrlerId: int = None,
                                           ip: str = None,
                                           port: int = None,
                                           userName: str = None,
                                           password: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TestConnect'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_controller_list_info(self,
                                       start: int = None,
                                       limit: int = None,
                                       update: int = None,
                                       blIncludeRecCnt: bool = None,
                                       blIncludeAuInfo: bool = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_cardholder_setting(self,
                                arrayJson: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_door_info(self,
                           DoorIds: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListDoor'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_logs_surveillance_station(self,
                                        filterType: int = None,
                                        filterEventSource: Any = None,
                                        filterSource: int = None,
                                        filterEventSourceItem: str = None,
                                        filterTimeFrom: int = None,
                                        filterTimeTo: int = None,
                                        filterKeyword: str = None,
                                        doorIds: str = None,
                                        eventTypes: str = None,
                                        update: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ClearLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_all_user_privilege(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListPrivilege'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def manual_lock_operation(self,
                              doorId: int = None,
                              operation: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DoorControl'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_user_door_priv_setting(self,
                                    arrayJson: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SavePrivilege'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_all_logs(self,
                      start: int = None,
                      limit: int = None,
                      filterType: int = None,
                      filterEventSource: Any = None,
                      filterSource: int = None,
                      filterEventSourceItem: str = None,
                      filterTimeFrom: int = None,
                      filterTimeTo: int = None,
                      filterKeyword: str = None,
                      timezoneOffset: int = None,
                      doorIds: str = None,
                      eventTypes: str = None,
                      update: int = None,
                      blIncludeRecCnt: bool = None,
                      blIncludeAuInfo: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListLog'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_selected_controller(self, ids: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def retrieve_data_from_controller(self, ctrlerId: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Retrieve'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def block_cardholder(self, arrayJson: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'BlockCardHolder'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_controller_count(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountByCategory'}

        return self.request_data(api_name, api_path, req_param)

    def start_controller_search(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Start'}

        return self.request_data(api_name, api_path, req_param)

    def get_controller_search_result(self,
                                     pid: int = None,
                                     offset: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.AxisAcsCtrler.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'InfoGet'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enumerate_digital_output(self,
                                 camId: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.DigitalOutput'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def save_digital_output_parameters(self,
                                       camId: int = None,
                                       idx: int = None,
                                       keep_setting: bool = None,
                                       normal_state: int = None,
                                       trigger_state: bool = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.DigitalOutput'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def long_polling_digital_output_status(self,
                                           camId: int = None,
                                           idx: int = None,
                                           keep: bool = None,
                                           setNormalCap: bool = None,
                                           normal: int = None,
                                           trigger: bool = None,
                                           timeOut: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.DigitalOutput'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PollState'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def trigger_external_event(self,
                               eventId: int = None,
                               eventName: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.ExternalEvent'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Trigger'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_list_io_modules(self,
                            start: int = None,
                            limit: int = None,
                            blFromList: bool = None,
                            ownerDsId: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_io_port_list(self,
                         Id: int = None,
                         Port: int = None,
                         IP: str = None,
                         User: str = None,
                         Pass: str = None,
                         Vendor: str = None,
                         Model: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumPort'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_supported_list_io_modules(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumVendorModel'}

        return self.request_data(api_name, api_path, req_param)

    def save_setting_io_module(self,
                               name: str = None,
                               id: int = None,
                               ownerDsId: int = None,
                               vendor: str = None,
                               model: str = None,
                               ip: str = None,
                               port: int = None,
                               userName: str = None,
                               enabled: bool = None,
                               status: int = None,
                               timeServer: str = None,
                               passWord: str = None,
                               ntpEnable: bool = None,
                               DIOdata: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_io_modules(self,
                            iomlist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_io_modules(self,
                          iomlist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_io_modules(self,
                          iomlist: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def test_connection_to_io_module(self,
                                     id: int = None,
                                     port: str = None,
                                     ip: str = None,
                                     userName: str = None,
                                     passWord: str = None,
                                     model: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'TestConn'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_capability_io_module(self,
                                 vendor: str = None,
                                 model: str = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCap'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def configure_io_port_setting(self,
                                  id: int = None,
                                  DIOdata: Any = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PortSetting'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def poll_trigger_state_io_module(self,
                                     Id: int = None,
                                     list: Any = None,
                                     timeOut: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PollingDI'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def poll_do_trigger_module(self,
                               id: int = None,
                               idx: int = None,
                               normal: int = None,
                               trigger: bool = None,
                               timeOut: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'PollingDO'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_number_of_devices(self) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetDevNumOfDs'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_category_count_io_module(self,
                                     start: int = None,
                                     limit: int = None,
                                     ownerDsId: int = None,
                                     blFromList: bool = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.IOModule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountByCategory'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_search_io_module(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.IOModule.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Start'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_search_io_module_info(self,
                                  pid: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.IOModule.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'InfoGet'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_current_camera_status(self,
                                  id_list: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Camera.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'OneTime'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_preset_camera_list(self,
                                cameraId: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_preset_camera_capability(self,
                                     cameraId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def record_current_camera_position(self,
                                       cameraId: int = None,
                                       position: int = None,
                                       speed: int = None,
                                       name: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetPreset'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_list_preset_camera(self,
                                  cameraId: Any = None,
                                  position: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DelPreset'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def go_specific_preset_by_given_speed(self,
                                          cameraId: Any = None,
                                          position: int = None,
                                          speed: int = None,
                                          type: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Execute'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def set_current_camera_position(self,
                                    cameraId: Any = None,
                                    bindPosition: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Preset'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SetHome'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_patrol_list(self,
                         cam: Any = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enum_patrol_name_list(self,
                              camId: Any = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnumPartial'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def load_patrol_detail(self,
                           id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def add_or_modify_patrol(self,
                             camId: Any = None,
                             id: int = None,
                             stayTime: int = None,
                             speed: int = None,
                             name: str = None,
                             presetList: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_specific_patrol(self,
                               camId: Any = None,
                               patrolId: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def run_patrol(self,
                   camId: Any = None,
                   id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Execute'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def stop_patrol(self,
                    camId: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.PTZ.Patrol'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Stop'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)



    def toggle_home_mode(self,
                         on: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.HomeMode'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Switch'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_home_mode_settings(self,
                               need_mobiles: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.HomeMode'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_transaction_list(self,
                             filterIds: str = None,
                             filterDsIds: str = None,
                             filterEnable: bool = None,
                             filterStatus: int = None,
                             start: int = None,
                             limit: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Transactions.Device'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_all_transaction_list(self,
                                 filterIds: str = None,
                                 dsId: int = None,
                                 filterTimeFrom: Any = None,
                                 filterStatus: int = None,
                                 filterLock: bool = None,
                                 filterTimeTo: Any = None,
                                 filterTimeRangeIntersect: bool = None,
                                 filterKeyword: str = None,
                                 start: int = None,
                                 limit: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enum'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_history_records(self,
                             filterIds: str = None,
                             dsId: int = None,
                             filterStatus: int = None,
                             filterLock: bool = None,
                             filterTimeFrom: Any = None,
                             filterTimeTo: Any = None,
                             filterTimeRangeIntersect: bool = None,
                             filterKeyword: str = None,
                             start: int = None,
                             limit: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_history_records(self,
                               filterIds: str = None,
                               dsId: int = None,
                               filterStatus: int = None,
                               filterLock: bool = None,
                               filterTimeFrom: Any = None,
                               filterTimeTo: Any = None,
                               filterTimeRangeIntersect: bool = None,
                               filterKeyword: str = None,
                               start: int = None,
                               limit: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_history_records(self,
                               filterIds: str = None,
                               dsId: int = None,
                               filterStatus: int = None,
                               filterLock: bool = None,
                               filterTimeFrom: Any = None,
                               filterTimeTo: Any = None,
                               filterTimeRangeIntersect: bool = None,
                               filterKeyword: str = None,
                               start: int = None,
                               limit: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_session_with_specified_session_id(self,
                                                device_name: str = None,
                                                session_id: str = None,
                                                timeout: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Begin'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def complete_session_with_specified_id(self,
                                           device_name: str = None,
                                           session_id: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Complete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def cancel_session_with_specified_session_id(self,
                                                 device_name: str = None,
                                                 session_id: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Cancel'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def carry_data_into_session_id(self,
                                   device_name: str = None,
                                   session_id: str = None,
                                   content: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Transactions.Transaction'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'AppendData'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def add_edit_active_vault_task(self,
                                   blCustomFolder: bool = None,
                                   blLimitBySize: bool = None,
                                   blRotateFile: bool = None,
                                   blSrcRecNoOverlap: bool = None,
                                   blUseRecDet: bool = None,
                                   camId: Any = None,
                                   camInfo: Any = None,
                                   dayLimit: int = None,
                                   didCode: str = None,
                                   dsSerial: str = None,
                                   execTime: Any = None,
                                   hostname: str = None,
                                   id: int = None,
                                   name: str = None,
                                   passwd: str = None,
                                   port: str = None,
                                   recEndTm: Any = None,
                                   recMode: str = None,
                                   recSchedule: str = None,
                                   recStartTm: Any = None,
                                   schedule: str = None,
                                   storagePath: str = None,
                                   type: int = None) -> dict[str, object] | str:  # TODO to check
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def login_source_server_get_info(self,
                                   port: str = None,
                                   hostname: str = None,
                                   protocol: bool = None,
                                     username: str = None,
                                     passwd: str = None,
                                     archId: int = None,
                                     didCode: str = None,
                                     srcDsId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'LoginSourceDS'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_archive_vault_task(self,
                                   id: int = None,
                                   keepRec: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_exist_archive_vault(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_archive_vault_task(self,
                                  id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_archive_vault_task(self,
                                  id: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DisableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_archive_vault_batchedit_task(self,
                                             taskIds: str = None,
                                             attrs: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'BatchEditTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_batch_edit_progress(self,
                                pid: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'BatchEditProgress'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_batchedit_proress_info(self,
                                   pid: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetBatchEditProgress'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clean_batchedit_progress_data(self,
                                   pid: int = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.Archiving.Pull'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'BatchEditProgressDone'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_youtube_live_broadcast_setting(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.YoutubeLive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Load'}

        return self.request_data(api_name, api_path, req_param)

    def set_youtube_live_broadcast_info(self,
                                        rtmp_path: str = None,
                                        key: str = None,
                                        cam_id: int = None,
                                        stream_profile: int = None,
                                        live_on: bool = None) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.YoutubeLive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Save'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def close_youtube_live_broadcast(self) -> dict[str, object] | str:
        api_name = 'SYNO.SurveillanceStation.YoutubeLive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CloseLive'}

        return self.request_data(api_name, api_path, req_param)

    def get_deep_video_analytic(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        return self.request_data(api_name, api_path, req_param)

    def create_edit_DVA_task(self,
                             analyze_type: int = None,
                             actFromHost: bool = None,
                             name: str = None,
                             camera_id: int = None,
                             enable: bool = None,
                             enable_recording: bool = None,
                             pre_rec_time: int = None,
                             post_rec_time: int = None,
                             event_integration: int = None,
                             region_type: int = None,
                             det_region_cnt: int = None,
                             det_region: int = None,
                             people_mode: int = None,
                             reset_cnt_frequency: int = None,
                             reset_weekday: int = None,
                             reset_date: int = None,
                             reset_time_minute: int = None,
                             reset_time_hour: int = None,
                             fence_dir_flag: int = None,
                             people_display_pos: int = None,
                             stream_profile: int = None,
                             people_enable_stay_max: bool = None,
                             intrusion_detect_target: int = None,
                             min_obj_size: Any = None,
                             min_obj_size_option: int = None,
                             enable_min_duration: int = None,
                             people_display_info: int = None,
                             people_enter: int = None,
                             people_stay_max: int = None,
                             people_region: str = None,
                             people_hint_pos: str = None,
                             blEditMode: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_dva_task(self,
                        ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_dva_task(self,
                        ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_dva_task(self,
                         ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DisableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def reset_counter_people_counting_task(self,
                                           taskId: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ResetPplCntCounter'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_people_enter_leave_count(self,
                                     ids: str = None,
                                     timeStart: str = None,
                                     timeEnd: str = None,
                                     timezone: int = None,
                                     ) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.Report'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_people_count_of_day(self,
                                ids: str = None,
                                interval: int = None,
                                intervalUnit: int = None,
                                timezone: int = None,
                                timestamp: int = None,
                                blOccupancy: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.Report'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetReport'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_people_counting_task(self,
                                taskList: str = None,
                                limit: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_recording_file_of_detection(self,
                                slaveDsParam: str = None,
                                deleteMethod: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_info_of_task_and_frame(self,
                                   eventId: int = None,
                                   taskId: int = None,
                                   blAlertEvt: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetAnalyticResult'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_recording_file_of_detection(self,
                                         dsId: int = None,
                                         idList: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_recording_file_of_detection(self,
                                           dsId: int = None,
                                           idList: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.Recording'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_info_people_counting_task(self) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_people_counting_task(self,
                                    enable: bool = None,
                                    task_ids: str = None,
                                    owner_ds_id: int = None,
                                    name: str = None,
                                    people_display_info: str = None,
                                    people_enable_stay_max: int = None,
                                    reset_cnt_frequency: int = None,
                                    resert_date: int = None,
                                    resert_weekday: int = None,
                                    resert_tome_hour: int = None,
                                    resert_tome_minute: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Create'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def modify_setting_of_people_counting_task(self,
                                               enable: bool = None,
                                               id: int = None,
                                               task_ids: str = None,
                                               name: str = None,
                                               people_display_info: int = None,
                                               people_enable_max: int = None,
                                               reset_cnt_frequency: int = None,
                                               resert_date: int = None,
                                               resert_weekday: int = None,
                                               resert_tome_hour: int = None,
                                               resert_tome_minute: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Edit'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_task_group(self,
                          ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def start_count_people_task_in_groups(self,
                                          ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Enable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def stop_count_people_task_in_groups(self,
                                         ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Disable'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_number_counting_task_group(self,
                                       id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetPeopleCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_recording_file_result(self,
                                   id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.IVA.TaskGroup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ResetPeopleCount'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_face_list_task(self,
                           ids: str = None,
                           ownerDsId: int = None,
                           blOnlyEnableDs: bool = None,
                           ) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_or_edit_task(self,
                            id: int = None,
                            id_on_rec_server: int = None,
                            camera_id: int = None,
                            camera_id_on_rec: int = None,
                            owner_ds_id: int = None,
                            enable: bool = None,
                            blEditMode: bool = None,
                            stream_profile: int = None,
                            name: str = None,
                            similarity: float = None,
                            allowed_color: int = None,
                            allowed_list: Any = None,
                            blocked_color: int = None,
                            blocked_list: Any = None,
                            vip_color: int = None,
                            vip_list: Any = None,
                            recognized_color: int = None,
                            unrecognized_color: int = None,
                            deleted: bool = None,
                            det_region: str = None,
                            det_region_cnt: int = None,
                            region_type: int = None,
                            display_info: int = None,
                            display_type: int = None,
                            frame_display_info: int = None,
                            enable_min_ogj_size: bool = None,
                            min_ogj_size: float = None,
                            post_rec_time: int = None,
                            pre_rec_time: int = None,
                            schedule: str = None,
                            scheduleOn: bool = None,
                            ignore_bad_quality: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_face_task(self,
                         ids: str = None,
                         keepRecording: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def enable_task_to_start_detection_recording(self,
                                                 ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EnableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_task_to_stop_detection_recording(self,
                                                 ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DisableTask'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_task_with_privilege_to_watch(self,
                                          ids: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListPlayableTsk'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_face_group(self,
                          name: str = None,
                          description: str = None,
                          update_registered_face: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CreateFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def disable_face_grooup(self,
                            ids: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def edit_face_group(self,
                        name: str = None,
                        description: str = None,
                        update_registered_face: Any = None,
                        id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EditFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_face_group_list(self,
                            id_only: bool = None,
                            filter: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_face_groups(self,
                          filter: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountFaceGroup'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def detect_faces_image(self,
                           image_data: str = None,
                           image_size: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DetectImageFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_registered_face(self,
                               account: str = None,
                               name: str = None,
                               description: str = None,
                               image_data: str = None,
                               image_size: int = None,
                               face: Any = None,
                               update_face_group: Any = None,
                               captured_face_id: int = None,
                               update_unrecognized_captured_face: bool = None,
                               append_image_data: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CreateRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_registered_face(self,
                               ids: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def edit_registered_face(self,
                             id: int = None,
                             account: str = None,
                             name: str = None,
                             description: str = None,
                             image_data: str = None,
                             image_size: int = None,
                             face: Any = None,
                             update_face_group: Any = None,
                             captured_face_id: int = None,
                             update_unrecognized_captured_face: bool = None,
                             append_image_data: bool = None,
                             ) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'EditRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_registered_face(self,
                             id_only: bool = None,
                             filter: Any = None,
                             append_image_data: bool = None,
                             ) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'ListRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def count_registered_face(self,
                              filter: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'CountRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def search_registered_face(self,
                               keywords: str = None,
                               append_image_data: bool = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SearchRegisteredFace'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_face_result_list(self,
                             filter: Any = None,
                             blIncludeSnapshot: bool = None,
                             blIncludeRegisteredFace: bool = None,
                             limit: int = None,
                             slaveDsParam: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'List'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_face_result(self,
                           filter: Any = None,
                           slaveDsParam: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def lock_face_result(self,
                         filter: Any = None,
                         slaveDsParam: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Lock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def unlock_face_result(self,
                           filter: Any = None,
                           slaveDsParam: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Unlock'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_recording_file_of_face_info(self,
                                        capturedFaceId: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetEventInfo'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_recognition_face_information(self,
                                         taskId: int = None,
                                         eventId: int = None,
                                         startTime: int = None,
                                         endTime: int = None,
                                         blIncludeRegisteredFace: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'GetAnalyticResult'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def correct_face_result(self,
                            id: int = None,
                            registered_face_id: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'Correct'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def mark_face_result_as_stranger(self,
                                     ids: str = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Face.Result'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'MarkAsStranger'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def add_new_bookmark(self,
                         id: int = None,
                         eventId: int = None,
                         cameraId: int = None,
                         archId: int = None,
                         name: str = None,
                         timestamp: Any = None,
                         comment: str = None,
                         ) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording.Bookmark'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'SaveBookmark'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_bookmark(self,
                        bookmarkIds: Any = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording.Bookmark'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteBookmark'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_bookmark_detail(self,
                             offset: int = None,
                             limit: int = None,
                             cameraIds: str = None,
                             fromTime: int = None,
                             toTime: int = None) -> dict[str, object] | str:  # TODO not working
        api_name = 'SYNO.SurveillanceStation.Recording.Bookmark'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'DeleteBookmark'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def list_audio_pattern(self) -> dict:
        """Get list of audio patterns
        
            Returns
            -------
            dict
                List of audio patterns
        
            Example return
            ----------
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
        """
    
        api_name = 'SYNO.SurveillanceStation.AudioPattern'
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": info['minVersion'],
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_share(self) -> dict:
        """List share for recordings
        
            Returns
            -------
            dict
                List of shared folder for recordings
        
            Example return
            ----------
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
        """
        
        api_name = 'SYNO.SurveillanceStation.Share'
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "ListRecShare",
            "version": info['minVersion'],
            "dsId": 0,
            "blIncldMigrating": True,
            "blIncldEncUnmount": True,
            "blIncldRemoteAbnormal": True,
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def check_license_quota(self, camList: List[dict]) -> dict:
        """Check license quota if cameras in camList in added
        
            Parameters
            ----------
            camList : List[dict]
                List of camera(s), here is example of a list of dict of the camera:
                ```json
                [{"ip": "10.13.22.141", "model": "DCS-3110", "vendor": "DLink", "port": 80}]
                ```
        
            Returns
            -------
            dict
                Infos about licenses and server
        
            Example return
            ----------
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
        """

        api_name = 'SYNO.SurveillanceStation.License'
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "BatCheckQuota",
            "version": info['minVersion'],
            "camList": json.dumps(camList)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def start_camera_search_process(self) -> dict:
        """Start the camera search process, return a PID
        
            Returns
            -------
            dict
                pid that is used in the `get_camera_search_info` as parameter
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "pid": 12773
                },
                "success": true
            }
            ```
        """

        api_name = 'SYNO.SurveillanceStation.Camera.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "Start",
            "version": info['minVersion']
        }
        
        return self.request_data(api_name, api_path, req_param)

    def get_camera_search_info(self, pid: int, offset: int = 0,
            blIncludeOverSSLCap: bool = True
        ) -> dict:
        """Get result of the search, this need to be call cyclic until result `searchStatus` is `False` (around 1min)
        
            Parameters
            ----------
            pid : int
                pid that is given in response of the `start_camera_search_process`
            offset : int, optional
                Offset in the camera found. Defaults to `0`
            blIncludeOverSSLCap : bool, optional
                Include camera that support SSL. Defaults to `True`
        
            Returns
            -------
            dict
                List of cameras with infos found between last call of the request
        
            Example return
            ----------
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
        """

        api_name = 'SYNO.SurveillanceStation.Camera.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "GetInfo",
            "version": info['minVersion'],
            "pid": pid,
            "blIpRange": False,
            "blIncludeOverSSLCap": blIncludeOverSSLCap,
            "offset": offset
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def start_camera_search_iprange_process(self,
            start_ip: str, end_ip: str, start_port: int, end_port: int,
            model_list: List[dict]
        ) -> dict:
        """Start the camera search process with IP / port range and model list, return a PID
        
            Parameters
            ----------
            start_ip : str
                Start IP address for the search
            end_ip : str
                End IP address for the search
            start_port : int
                Start port for the search.
            end_port : int
                Start port for the search.
            model_list : List[dict]
                List of dict that define models to search.
                Here is an example:
                ```json
                [{"vendor":"ONVIF","model":"Generic_ONVIF","usr":"YOUR_CAMERA_USERNAME","pass":"YOUR_CAMERA_PASSWORD","isOverHTTPS":false}]
                ```
        
            Returns
            -------
            dict
                pid that is used in the `get_camera_search_iprange_info` as parameter
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "pid": 20228
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.SurveillanceStation.Camera.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "IPRange",
            "version": info['minVersion'],
            "modelList": json.dumps(model_list),
            "startPort": start_port,
            "endPort": end_port,
            "startIP": start_ip,
            "endIP": end_ip,
            "blIpRange": True,
        }
        
        return self.request_data(api_name, api_path, req_param)
        
    def get_camera_search_iprange_info(self, pid: int, offset: int = 0,
            blIncludeOverSSLCap: bool = True
        ) -> dict:
        """Get result of the search from IP range, this need to be call cyclic until result `searchStatus` is `False` (around 200s in my test)
        
            Parameters
            ----------
            pid : int
                pid that is given in response of the `start_camera_search_iprange_process`
            offset : int, optional
                Offset in the camera found. Defaults to `0`
            blIncludeOverSSLCap : bool, optional
                Include camera that support SSL. Defaults to `True`
        
            Returns
            -------
            dict
                List of cameras with infos found between last call of the request
        
            Example return
            ----------
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
        """
        
        api_name = 'SYNO.SurveillanceStation.Camera.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "GetIPRangeInfo",
            "version": info['minVersion'],
            "pid": pid,
            "blIpRange": True,
            "blIncludeOverSSLCap": blIncludeOverSSLCap,
            "offset": offset
        }
        
        return self.request_data(api_name, api_path, req_param)
    

