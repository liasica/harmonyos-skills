---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info
title: @ohos.deviceInfo (设备信息)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.deviceInfo (设备信息)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6726292bfeb1a0173b6a7839ad02eff8b68e01fe02d507ead5bf1829bfaa04cc
---

本模块提供终端设备信息查询，开发者不可配置。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

部分参数返回值为default的，会在正式发布的版本中配置。

本模块接口返回设备常量信息，建议应用只调用一次，不需要频繁调用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { deviceInfo } from '@kit.BasicServicesKit';
```

## 常量

PhonePC/2in1TabletTVWearable

说明

未特殊说明的字段，数据长度最大值为96字节。

**系统能力**：SystemCapability.Startup.SystemInfo。

**权限**：以下各项所需要的权限有所不同，详见下表。

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| deviceType | string | 是 | 设备类型。详细请参考[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。  示例：phone |
| manufacture | string | 是 | 设备厂家名称。  示例：HUAWEI |
| brand | string | 是 | 设备品牌名称。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。  示例：HUAWEI |
| marketName | string | 是 | 外部产品系列。  示例：HUAWEI Mate 60 Pro |
| productSeries | string | 是 | 产品系列。  示例：ALN |
| productModel | string | 是 | 认证型号。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。  示例：ALN-AL00 |
| productModelAlias14+ | string | 是 | 认证型号别名。  **元服务API**：从API version 14开始，该接口支持在元服务中使用。  示例：TAS-AL00 |
| softwareModel | string | 是 | 内部软件子型号。  示例：ALN-AL00 |
| hardwareModel | string | 是 | 硬件版本号。  示例：HL1CMSM |
| hardwareProfile(deprecated) | string | 是 | 硬件Profile。  **说明**：  从API version 6 开始支持，从API version 9 开始废弃，建议使用[系统能力SystemCapability](syscap.md)替代。  示例：default |
| serial | string | 是 | 设备序列号SN(Serial Number)。  **说明**：可作为设备唯一识别码。  **需要权限**：ohos.permission.sec.ACCESS\_UDID(该权限只允许系统应用及企业定制应用申请)  示例：序列号随设备差异 |
| bootloaderVersion | string | 是 | Bootloader版本号。  示例：bootloader |
| abiList | string | 是 | 应用二进制接口（Abi）。  示例：arm64-v8a |
| securityPatchTag | string | 是 | 安全补丁级别。  示例：2024/1/1 |
| displayVersion | string | 是 | 产品版本。  示例：ALN-AL00 5.0.0.1(XXX) |
| incrementalVersion | string | 是 | 差异版本号。  示例：default |
| osReleaseType | string | 是 | 系统的发布类型，取值为：  - Canary：面向特定开发者发布的早期预览版本，不承诺API稳定性。  - Beta：面向开发者公开发布的Beta版本，不承诺API稳定性。  - Release：面向开发者公开发布的正式版本，承诺API稳定性。  示例：Canary1/Beta2/Release |
| osFullName | string | 是 | 系统版本，版本格式OpenHarmony-x.x.x.x。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。  示例：OpenHarmony-5.0.0.1(Canary1) |
| majorVersion | number | 是 | Major版本号，随主版本更新增加，值为osFullName中的第一位数值，建议直接使用deviceInfo.majorVersion获取，可提升效率，不建议开发者解析osFullName获取。  示例：5 |
| seniorVersion | number | 是 | Senior版本号，随局部架构、重大特性增加，值为osFullName中的第二位数值，建议直接使用deviceInfo.seniorVersion获取，可提升效率，不建议开发者自主解析osFullName获取。  示例：0 |
| featureVersion | number | 是 | Feature版本号，标识规划的新特性版本，值为osFullName中的第三位数值，建议直接使用deviceInfo.featureVersion获取，可提升效率，不建议开发者自主解析osFullName获取。  示例：0 |
| buildVersion | number | 是 | Build版本号，标识编译构建的版本号，值为osFullName中的第四位数值，建议直接使用deviceInfo.buildVersion获取，可提升效率，不建议开发者自主解析osFullName获取。  示例：1 |
| sdkApiVersion | number | 是 | 系统软件API版本。  **元服务API**：从API version 14开始，该接口支持在元服务中使用。  示例：12 |
| firstApiVersion | number | 是 | 首个版本系统软件API版本。  示例：3 |
| versionId | string | 是 | 版本ID。由deviceType、manufacture、brand、productSeries、osFullName、productModel、softwareModel、sdkApiVersion、incrementalVersion、buildType拼接组成。  示例：wearable/HUAWEI/HUAWEI/TAS/OpenHarmony-5.0.0.1/TAS-AL00/TAS-AL00/12/default/release:nolog |
| buildType | string | 是 | 构建类型。  示例：default |
| buildUser | string | 是 | 构建用户。  示例：default |
| buildHost | string | 是 | 构建主机。  示例：default |
| buildTime | string | 是 | 构建时间。  示例：default |
| buildRootHash | string | 是 | 构建版本Hash。  示例：default |
| udid7+ | string | 是 | 设备Udid。  **说明**：数据长度为65字节。可作为设备唯一识别码。  **需要权限**：ohos.permission.sec.ACCESS\_UDID(该权限只允许系统应用及企业类应用申请)  示例：9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412 |
| distributionOSName10+ | string | 是 | 发行版系统名称。  示例：OpenHarmony |
| distributionOSVersion10+ | string | 是 | 发行版系统版本号。格式为x.x.x，x是数字  示例：5.0.0 |
| distributionOSApiVersion10+ | number | 是 | 发行版系统api版本。  示例：50001 |
| distributionOSApiName13+ | string | 是 | 发行版系统api版本名称。 |
| distributionOSReleaseType10+ | string | 是 | 发行版系统类型。  示例：Release |
| ODID12+ | string | 是 | 开发者匿名设备标识符。  **ODID值会在以下场景重新生成**：  手机恢复出厂设置。  同一设备上同一个开发者(developerId相同)的应用全部卸载后重新安装时。  **ODID生成规则**：  根据签名信息里developerId解析出的groupId生成，developerId规则为groupId.developerId，若无groupId则取整个developerId作为groupId。  同一设备上运行的同一个开发者(developerId相同)的应用，ODID相同。  同一个设备上不同开发者(developerId不同)的应用，ODID不同。  不同设备上同一个开发者(developerId相同)的应用，ODID不同。  不同设备上不同开发者(developerId不同)的应用，ODID不同。  **说明**：数据长度为37字节(包含结束符)。  示例：1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX |
| diskSN15+ | string | 是 | 硬盘序列号。  **说明** ：该字段只能在2in1设备进行查询，其他设备查询结果为空。  **需要权限**：ohos.permission.ACCESS\_DISK\_PHY\_INFO  示例：2502EM400567 |
| performanceClass19+ | [PerformanceClassLevel](js-apis-device-info.md#performanceclasslevel19) | 是 | 描述设备能力等级，基于CPU、内存、存储读写性能和屏幕分辨率等因素综合评估。 |
| chipType21+ | string | 是 | 当前设备CPU芯片型号  示例：xxxxx |
| bootCount21+ | number | 是 | 当前设备重启次数，获取失败时返回-1  示例：100 |

**示例**

```
1. import { deviceInfo } from '@kit.BasicServicesKit';

3. let deviceTypeInfo: string = deviceInfo.deviceType;
4. // 输出结果：the value of the deviceType is :wearable
5. console.info('the value of the deviceType is :' + deviceTypeInfo);

7. let manufactureInfo: string = deviceInfo.manufacture;
8. // 输出结果：the value of the manufacture is :HUAWEI
9. console.info('the value of the manufactureInfo is :' + manufactureInfo);

11. let brandInfo: string = deviceInfo.brand;
12. // 输出结果：the value of the brand is :HUAWEI
13. console.info('the value of the device brand is :' + brandInfo);

15. let marketNameInfo: string = deviceInfo.marketName;
16. // 输出结果：the value of the marketName is :Mate XX
17. console.info('the value of the deviceInfo marketName is :' + marketNameInfo);

19. let productSeriesInfo: string = deviceInfo.productSeries;
20. // 输出结果：the value of the productSeries is :TAS
21. console.info('the value of the deviceInfo productSeries is :' + productSeriesInfo);

23. let productModelInfo: string = deviceInfo.productModel;
24. // 输出结果：the value of the productModel is :TAS-AL00
25. console.info('the value of the deviceInfo productModel is :' + productModelInfo);

27. let productModelAliasInfo: string = deviceInfo.productModelAlias;
28. console.info('the value of the deviceInfo productModelAlias is :' + productModelAliasInfo);

30. let softwareModelInfo: string = deviceInfo.softwareModel;
31. // 输出结果：the value of the softwareModel is :TAS-AL00
32. console.info('the value of the deviceInfo softwareModel is :' + softwareModelInfo);

34. let hardwareModelInfo: string = deviceInfo.hardwareModel;
35. // 输出结果：the value of the hardwareModel is :TASA00CVN1
36. console.info('the value of the deviceInfo hardwareModel is :' + hardwareModelInfo);

38. let serialInfo: string = deviceInfo.serial;
39. // 输出结果：the value of the serial is :序列号随设备差异
40. console.info('the value of the deviceInfo serial is :' + serialInfo);

42. let bootloaderVersionInfo: string = deviceInfo.bootloaderVersion;
43. // 输出结果：the value of the bootloaderVersion is :bootloader
44. console.info('the value of the deviceInfo bootloaderVersion is :' + bootloaderVersionInfo);

46. let abiListInfo: string = deviceInfo.abiList;
47. // 输出结果：the value of the abiList is :arm64-v8a
48. console.info('the value of the deviceInfo abiList is :' + abiListInfo);

50. let securityPatchTagInfo: string = deviceInfo.securityPatchTag;
51. // 输出结果：the value of the securityPatchTag is :2021/01/01
52. console.info('the value of the deviceInfo securityPatchTag is :' + securityPatchTagInfo);

54. let displayVersionInfo: string = deviceInfo.displayVersion;
55. // 输出结果：the value of the displayVersion is :XXX X.X.X.X
56. console.info('the value of the deviceInfo displayVersion is :' + displayVersionInfo);

58. let incrementalVersionInfo: string = deviceInfo.incrementalVersion;
59. // 输出结果：the value of the incrementalVersion is :default
60. console.info('the value of the deviceInfo incrementalVersion is :' + incrementalVersionInfo);

62. let osReleaseTypeInfo: string = deviceInfo.osReleaseType;
63. // 输出结果：the value of the osReleaseType is :Release
64. console.info('the value of the deviceInfo osReleaseType is :' + osReleaseTypeInfo);

66. let osFullNameInfo: string = deviceInfo.osFullName;
67. // 输出结果：the value of the osFullName is :OpenHarmony-5.0.0.1
68. console.info('the value of the deviceInfo osFullName is :' + osFullNameInfo);

70. let majorVersionInfo: number = deviceInfo.majorVersion;
71. // 输出结果：the value of the majorVersion is :5
72. console.info('the value of the deviceInfo majorVersion is :' + majorVersionInfo);

74. let seniorVersionInfo: number = deviceInfo.seniorVersion;
75. // 输出结果：the value of the seniorVersion is :0
76. console.info('the value of the deviceInfo seniorVersion is :' + seniorVersionInfo);

78. let featureVersionInfo: number = deviceInfo.featureVersion;
79. // 输出结果：the value of the featureVersion is :0
80. console.info('the value of the deviceInfo featureVersion is :' + featureVersionInfo);

82. let buildVersionInfo: number = deviceInfo.buildVersion;
83. // 输出结果：the value of the buildVersion is :1
84. console.info('the value of the deviceInfo buildVersion is :' + buildVersionInfo);

86. let sdkApiVersionInfo: number = deviceInfo.sdkApiVersion;
87. // 输出结果：the value of the sdkApiVersion is :12
88. console.info('the value of the deviceInfo sdkApiVersion is :' + sdkApiVersionInfo);

90. let firstApiVersionInfo: number = deviceInfo.firstApiVersion;
91. // 输出结果：the value of the firstApiVersion is :3
92. console.info('the value of the deviceInfo firstApiVersion is :' + firstApiVersionInfo);

94. let versionIdInfo: string = deviceInfo.versionId;
95. // 输出结果：the value of the versionId is :wearable/HUAWEI/HUAWEI/TAS/OpenHarmony-5.0.0.1/TAS-AL00/TAS-AL00/12/default/release:nolog
96. console.info('the value of the deviceInfo versionId is :' + versionIdInfo);

98. let buildTypeInfo: string = deviceInfo.buildType;
99. // 输出结果：the value of the buildType is :default
100. console.info('the value of the deviceInfo buildType is :' + buildTypeInfo);

102. let buildUserInfo: string = deviceInfo.buildUser;
103. // 输出结果：the value of the buildUser is :default
104. console.info('the value of the deviceInfo buildUser is :' + buildUserInfo);

106. let buildHostInfo: string = deviceInfo.buildHost;
107. // 输出结果：the value of the buildHost is :default
108. console.info('the value of the deviceInfo buildHost is :' + buildHostInfo);

110. let buildTimeInfo: string = deviceInfo.buildTime;
111. // 输出结果：the value of the buildTime is :default
112. console.info('the value of the deviceInfo buildTime is :' + buildTimeInfo);

114. let buildRootHashInfo: string = deviceInfo.buildRootHash;
115. // 输出结果：the value of the buildRootHash is :default
116. console.info('the value of the deviceInfo buildRootHash is :' + buildRootHashInfo);

118. let udid: string = deviceInfo.udid;
119. // 输出结果：the value of the udid is :9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412
120. console.info('the value of the deviceInfo udid is :' + udid);

122. let distributionOSName: string = deviceInfo.distributionOSName
123. // 输出结果：the value of the distributionOSName is :OpenHarmony
124. console.info('the value of the deviceInfo distributionOSName is :' + distributionOSName);

126. let distributionOSVersion: string = deviceInfo.distributionOSVersion
127. // 输出结果：the value of the distributionOSVersion is :5.0.0
128. console.info('the value of the deviceInfo distributionOSVersion is :' + distributionOSVersion);

130. let distributionOSApiVersion: number = deviceInfo.distributionOSApiVersion
131. // 输出结果：the value of the distributionOSApiVersion is :500001
132. console.info('the value of the deviceInfo distributionOSApiVersion is :' + distributionOSApiVersion);

134. let distributionOSApiName: string = deviceInfo.distributionOSApiName
135. console.info('the value of the deviceInfo distributionOSApiName is :' + distributionOSApiName);

137. let distributionOSReleaseType: string = deviceInfo.distributionOSReleaseType
138. // 输出结果：the value of the distributionOSReleaseType is :Release
139. console.info('the value of the deviceInfo distributionOSReleaseType is :' + distributionOSReleaseType);

141. let odid: string = deviceInfo.ODID;
142. // 输出结果：the value of the ODID is :1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX
143. console.info('the value of the deviceInfo odid is :' + odid);

145. let diskSN: string = deviceInfo.diskSN;
146. // 输出结果：the value of the deviceInfo diskSN is :2502EM400567
147. console.info('the value of the deviceInfo diskSN is :' + diskSN);

149. let performanceClass = deviceInfo.performanceClass;
150. // 输出结果：the value of the deviceInfo performanceClass is :0
151. console.info('the value of the deviceInfo performanceClass is :' + performanceClass);

153. let chipType: string = deviceInfo.chipType;
154. // 输出结果：the value of the deviceInfo chipType is :xxxxx
155. console.info('the value of the deviceInfo chipType is :' + chipType);

157. let bootCount: number = deviceInfo.bootCount
158. // 输出结果：the value of the bootCount is :100
159. console.info('the value of the deviceInfo bootCount is :' + bootCount);
```

## PerformanceClassLevel19+

PhonePC/2in1TabletTVWearable

表示设备能力定级的枚举。

**系统能力**：SystemCapability.Startup.SystemInfo

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLASS\_LEVEL\_HIGH | 0 | 表示设备能力定级为高。 |
| CLASS\_LEVEL\_MEDIUM | 1 | 表示设备能力定级为中。 |
| CLASS\_LEVEL\_LOW | 2 | 表示设备能力定级为低。 |

## DeviceTypes20+

PhonePC/2in1TabletTVWearable

设备类型枚举值，可用于校验deviceType的返回值。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Startup.SystemInfo

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_DEFAULT | 'default' | 默认设备。 |
| TYPE\_PHONE | 'phone' | 手机。 |
| TYPE\_TABLET | 'tablet' | 平板。 |
| TYPE\_2IN1 | '2in1' | PC/2in1。 |
| TYPE\_TV | 'tv' | 智慧屏。 |
| TYPE\_WEARABLE | 'wearable' | 智能手表。 |
| TYPE\_CAR | 'car' | 车机。 |

**示例**

```
1. let deviceTypesInfoDefault: string = deviceInfo.DeviceTypes.TYPE_DEFAULT;
2. // 输出结果：the value of the DeviceTypes is :default
3. console.info('the value of the DeviceTypes is :' + deviceTypesInfoDefault);

5. let deviceTypesInfoPhone: string = deviceInfo.DeviceTypes.TYPE_PHONE;
6. // 输出结果：the value of the DeviceTypes is :phone
7. console.info('the value of the DeviceTypes is :' + deviceTypesInfoPhone);

9. let deviceTypesInfoTablet: string = deviceInfo.DeviceTypes.TYPE_TABLET;
10. // 输出结果：the value of the DeviceTypes is :tablet
11. console.info('the value of the DeviceTypes is :' + deviceTypesInfoTablet);

13. let deviceTypesInfo2IN1: string = deviceInfo.DeviceTypes.TYPE_2IN1;
14. // 输出结果：the value of the DeviceTypes is :2in1
15. console.info('the value of the DeviceTypes is :' + deviceTypesInfo2IN1);

17. let deviceTypesInfoTV: string = deviceInfo.DeviceTypes.TYPE_TV;
18. // 输出结果：the value of the DeviceTypes is :tv
19. console.info('the value of the DeviceTypes is :' + deviceTypesInfoTV);

21. let deviceTypesInfoWearable: string = deviceInfo.DeviceTypes.TYPE_WEARABLE;
22. // 输出结果：the value of the DeviceTypes is :wearable
23. console.info('the value of the DeviceTypes is :' + deviceTypesInfoWearable);

25. let deviceTypesInfoCar: string = deviceInfo.DeviceTypes.TYPE_CAR;
26. // 输出结果：the value of the DeviceTypes is :car
27. console.info('the value of the DeviceTypes is :' + deviceTypesInfoCar);
```
