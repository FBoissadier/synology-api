---
sidebar_position: 3
title: Structures
---
<div class="---">
### `StreamSettingType`
Dataclass that represent the parameters of a stream of a camera  
  
#### Parameters
<div class="padding-left--md">
**_fps_** `int`  
Frames per second of the stream. Defaults to `None`  
  
**_resolution_** `str`  
Denoted as width * height. Defaults to `None`  
  
**_bitrateCtrl_** `int`  
The bitrate control type. Defaults to `None`
- 0: None
- 1: Variable bitrate
- 2: Constant bitrate  
  
**_quality_** `int`  
An integer ranged from 1 to 5 to indicate the quality of the stream. Defaults to `None`  
`This parameter only valid when using variable bitrate.`  
  
**_constantBitrate_** `int`  
The constant bitrate value. Defaults to `None`  
`This parameter only valid when using constant bitrate.`  
  

</div>

</div>



---


<div class="---">
### `SaveCameraParamType`
Dataclass that represent the parameters of the `camera_save` function  
  
#### Parameters
<div class="padding-left--md">
**_id_** `int`  
Camera id to be edited. If equal to 0, add new camera according to request parameter. Defaults to `None`  
  
**_name_** `str`  
Camera name to be edited. Note that this parameter is only valid when `id` is not specified and `dsId` is specified. Defaults to `None`  
  
**_dsId_** `int`  
Camera owner ds id. Defaults to `None`  
  
**_newName_** `str`  
`Needed when add case` Camera new name. Defaults to `None`  
  
**_ip_** `str`  
`Needed when add case` Camera ip. Defaults to `None`  
  
**_port_** `int`  
`Needed when add case` Camera port. Defaults to `None`  
  
**_vendor_** `str`  
`Needed when add case` Camera vendor. Defaults to `None`  
  
**_model_** `str`  
`Needed when add case` Camera model. Defaults to `None`  
  
**_userName_** `str`  
`Needed when add case` Camera login user name. Defaults to `None`  
  
**_password_** `str`  
`Needed when add case` Camera login password. Defaults to `None`  
  
**_videoCodec_**  [`VideoCodecEnum`](/apis/enumerations.md#videocodecenum)   
Camera video codec. Defaults to `None`  
  
**_audioCodec_**  [`AudioCodecEnum`](/apis/enumerations.md#audiocodecenum)   
Camera audio codec. Defaults to `None`  
  
**_tvStandard_**  [`TvStandardEnum`](/apis/enumerations.md#tvstandardenum)   
Camera tv standard. Defaults to `None`  
  
**_channel_** `str`  
Camera channel. Defaults to `None`  
  
**_userDefinePath_** `str`  
`Needed when add user define camera` Camera streaming path. This parameter only valid when camera vendor is `User` and model is `Define`.
Defaults to `None`  
  
**_fov_** `str`  
Camera field of view. Defaults to `None`  
  
**_stream1_**  [`StreamSettingType`](/apis/structures.md#streamsettingtype)   
Stream 1 parameters. Defaults to `None`  
  
**_stream2_**  [`StreamSettingType`](/apis/structures.md#streamsettingtype)   
Stream 2 parameters. Defaults to `None`  
  
**_stream3_**  [`StreamSettingType`](/apis/structures.md#streamsettingtype)   
Stream 3 parameters. Defaults to `None`  
  
**_recordTime_** `int`  
The recording length in minute. Defaults to `None`  
  
**_preRecordTime_** `int`  
Extra recording time before the start of each recording in second. Defaults to `None`  
  
**_postRecordTime_** `int`  
Extra recording time after the end of each recording in second. Defaults to `None`  
  
**_enableRecordingKeepDays_** `bool`  
Does the rotation occur when the limit time is reached. Defaults to `None`  
  
**_recordingKeepDays_** `int`  
The upper bound indicating how long a file can be store before rotation. Defaults to `None`  
  
**_enableRecordingKeepSize_** `bool`  
Does the rotation occur when the limit space is reached. Defaults to `None`  
  
**_recordingKeepSize_** `int`  
The upper bound that total file size can reach before rotation. Defaults to `None`  
  
**_enableLowProfile_** `bool`  
Does low bandwidth profile enabled. Defaults to `None`  
  
**_recordSchedule_** `List[int]`  
A string consists of 48*7 digits to represent the scheduling. Note that each digit stands for the schedule type of half-hour:
    - 0: No scheduled plan
    - 1: Continuous Recording
    - 2: Motion Detection Recording
    - 3: Custom Detection 1
    - 4: Custom Detection 2
    
Defaults to `None`  
  
**_rtspPathTimeout_**  [`RtpsPathTimeoutEnum`](/apis/enumerations.md#rtpspathtimeoutenum)   
The timeout of share stream. Defaults to `None`  
  

</div>

</div>



---


