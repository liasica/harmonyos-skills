---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/protocol-specification
title: 协议规格
breadcrumb: 指南 > 应用体验建议 > 应用基础功能和兼容性体验建议 > 系统特性与基础功能 > 协议规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:59+08:00
doc_updated_at: 2026-01-19
content_hash: sha256:b0cbc62dd9b14fc139bbe53b7e79c1db4a9449d24828c4a1f50caa53ee922b3e
---

## 蜂窝通信体验

|  |  |
| --- | --- |
| **描述** | 联网应用遵循默认网络切换，比如WiFi切换到蜂窝网络，或者蜂窝切换到WiFi网络，或者蜂窝主卡切换到副卡网络，实现数据传输平滑迁移到默认网络上，避免网络切换后无法上网等问题; |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [网络连接能力](network-kit-network-management.md) |

|  |  |
| --- | --- |
| **描述** | 联网应用，插SIM卡，不连接WIFI，应用可正常上网； |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [数据传输能力](network-kit-data-transmission.md) |

|  |  |
| --- | --- |
| **描述** | 联网应用数传策略分层，包括但不限定于缓存、调速、请求大小资源等，遵循通信感知API(网络状态和通信建议)来调整数传策略； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [网络质量评估](networkboost-qoscallback.md)、[弱网感知判决](networkboost-qoscallback.md) |

|  |  |
| --- | --- |
| **描述** | 联网应用应通过通信感知API真实反馈引发用户体验异常的网络传输质量，包括但不限于服务器错误、无数据、丢包、乱序、抖动、高时延等信息； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [应用传输体验反馈](networkboost-appreportqoe.md) |

## 短距通信体验

|  |  |
| --- | --- |
| **描述** | * Host-based Card Emulation（HCE，基于主机的卡模拟）应用需要调用hasHceCapability()接口判断是否支持HCE功能； * HCE应用使用动态注册AID时，应用进入前台后，调用start(elementName: ElementName, aidList: string[])接口，注册为前台应用，应用退出前台后，调用stop(elementName: ElementName)接口取消注册前台应用；HCE应用使用静态注册AID时，应在应用的metadata中声明对应应用关注的AID； * HCE应用需要申请NFC卡模拟权限（ohos.permission.NFC\_CARD\_EMULATION），应声明HCE特定的action（"ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE"）； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [HCE卡模拟开发指南](nfc-hce-guide.md) |

|  |  |
| --- | --- |
| **描述** | 应用应根据用户实际使用场景，严格按照API定义请求所需位置信息，具体而言：   * 新闻资讯、网购、点餐类等对定位精度要求不高的应用在使用getCurrentLocation接口时，参数 SingleLocationRequest.locatingPriority应指定LocatingPriority.PRIORITY\_LOCATING\_SPEED； * 非导航、运动、出行类APP调用定位接口时，参数 ContinuousLocationRequest.locationScenario建议指定UserActivityScenario.DAILY\_LIFE\_SERVICE。 * 非导航、运动、出行类APP建议启动定位不超过10分钟，且不启动location类型的长时任务； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [获取设备的位置信息开发指导](location-guidelines.md) |

|  |  |
| --- | --- |
| **描述** | 添加围栏优先使用addGnssGeofence(fenceRequest: GnssGeofenceRequest): Promise<number>;接口，该接口限制了围栏触发后与用户的交互方式，只允许弹通知提醒； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [地理围栏开发指导](geofence-guidelines.md) |

|  |  |
| --- | --- |
| **描述** | * 建议应用按需获取Wi-Fi扫描结果，避免频繁获取扫描结果；建议应用监听Wi-Fi扫描结果上报事件来获取Wi-Fi扫描结果，使用Wi-Fi扫描结果应满足用户隐私保护要求； * 应用需要合理使用添加建议网络配置接口（addCandidateConfig）、发起网络连接接口（ connectToCandidateConfig）、删除网络配置接口（removeCandidateConfig），避免频繁的进行网络切换以及存储了大量网络配置信息，降低了Wi-Fi使用效率，建议网络配置使用完后及时删除； * 应用合理使用Wi-Fi连接状态和Wi-Fi网络状态查询，建议通过监听接口获取状态变化，避免频繁调用影响Wi-Fi业务体验； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | 无 |

|  |  |
| --- | --- |
| **描述** | 联网类应用，在不插SIM卡的情况下，连接Wi-Fi后，应用可正常上网； |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | 无 |

|  |  |
| --- | --- |
| **描述** | 非运动健康类的应用不建议调用startBluetoothDiscovery，stopBluetoothDiscovery， setBluetoothScanMode接口； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | 无 |

|  |  |
| --- | --- |
| **描述** | 应用不应该频繁连接和断开蓝牙设备，建议连接失败后重试间隔超过10s，失败重试次数<=3次； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | 无 |

|  |  |
| --- | --- |
| **描述** | 应用合理使用BLE扫描参数，应遵循如下要求：   * 建议使用BLE扫描过滤器参数，避免扫描不相关设备； * 建议使用SCAN\_MODE\_LOW\_POWER或SCAN\_MODE\_BALANCED参数，减少SCAN\_MODE\_LOW\_LATENCY（高占空比类型）的BLE扫描，减少蓝牙资源使用冲突影响用户体验； |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | [广播与扫描开发指导](../atomic-guides/atomic-bluetooth-advertising.md) |
