---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-json-object-api
title: jsonObject（Entity返回参数说明）
breadcrumb: API参考 > AI > Natural Language Kit（自然语言理解服务） > ArkTS API > jsonObject（Entity返回参数说明）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7628256c048d43904a8c644ac63df45151b340f0b76dfe6c4c460191d57fa6a4
---

[Entity](natural-language-text-processing-api.md#entity)返回值中jsonObject的参数详细说明。

## 基础类

### 时间实体

识别文本中出现的时间，返回类型为JSONObject，键为“time”，键对应的值类型为JSONArray，数组里值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| repeat | string | 否 | 周期。 |
| rrule | string | 否 | 周期标识，不一定准确，具体以repeat为准（参考数据，不建议使用）。 |
| start | string | 否 | 开始时间。  示例如下：  1. 2021-08-28T08:00:00（日期和精确时间）  2. 2021-08-28TM（日期和模糊时间）  3. 2021-08-28（日期）  4. T08:00:00（周期时间，没有明确日期，例如“每天8点”）  5. TM（周期时间，没有明确日期，例如“每天早上”）  **说明：**  T为分隔符，T前面为年月日，T后面为时间点，可以是精确时间，可以是用粒度表示的模糊时间。 |
| suggestStart | string | 否 | 具体开始时间。  大多数情况下，suggestStart与start相同，但在某些表面上是单个时间，但实际是时间段的时候两者有区别。当文本描述的是一个时间段（如“1月”）时，suggestStart提供该时间段的起始具体日期。  示例如下：  1. “1月”，start（2021-01），end（2021-01），suggestStart（2021-01-01），suggestEnd（2021-01-31）  2. “1月到3月”，start（2021-01），end（2021-03），suggestStart（2021-01-01），suggestEnd（2021-03-31） |
| startTimestamp | number | 否 | 开始时间戳（单位：ms）。当start为模糊时间时，该时间戳可能不准确，建议以suggestStart为准。 |
| end | string | 否 | 结束时间。 |
| suggestEnd | string | 否 | 具体结束时间。大多数情况下，suggestEnd与end相同，但在某些表面上是单个时间，但实际是时间段的时候两者有区别。 |
| endTimestamp | number | 否 | 结束时间戳（单位：ms）。当end为模糊时间时，该时间戳可能不准确，建议以suggestEnd为准。 |
| maxSection | string | 否 | 最大时间粒度。  P：精确时间。  M：早晨。  F：上午。  N：中午。  A：下午。  L：傍晚。  E：晚上。  W：凌晨。 |
| minSection | string | 否 | 最小时间粒度。 |
| isContainFuzzyTime | boolean | 是 | 是否包含模糊时间。true：包含；false：不包含。默认为false。 |
| containFuzzySection | string | 是 | 模糊时间粒度，不包含模糊时间粒度时默认为D。D表示“天”粒度，即按天处理模糊时间。 |
| inferType | string | 否 | 时间推理类型枚举。 |
| rangeDecoration | string | 否 | 范围描述。 |
| rangeText | string | 否 | 带范围描述的文本。 |
| isFestival | boolean | 否 | 是否节日。true：是；false：不是。 |
| normalFestival | string | 否 | 节日归一化值。 |
| isLunarTime | boolean | 否 | 是否包含农历时间。true：包含；false：不包含。 |
| startLunarTime | string | 否 | 包含的农历时间。 |
| isSolarTerm | boolean | 否 | 是否节气。true：是；false：不是。 |
| isIllegal | boolean | 否 | 是否非法。true：是；false：不是。默认为false。  **说明**：对于不符合规范的时间，通常不会进行识别。只有在特定业务场景下，出现较多且特殊的情况时，才会进行识别并设置非法标识。绝大多数不规范时间仍会被忽略或识别不正确，但这不会对整体功能造成影响。  示例如下：  1. “2月30号”，会把start设置为29号或28号，isIllegal设为true。  2. “每周上午8点”，缺少每周具体周几，周期会默认设置成当前周几，isIllegal设为true。  3. “每月周一8点”，缺少每月具体几号。  4. “每年8号上午9点”，缺少每年具体几月。 |
| isChangedIllegal | boolean | 是 | 是否自动修正了非法时间。true：是；false：不是。 |
| isPlusTwelveHour | boolean | 是 | 是否包含天以内模糊时间。true：是；false：不是。 |
| sequence | number | 是 | 对应实体出现频率。 |
| oriFestival | string | 否 | 时间里包含的节日文本。 |
| timestampZone | string | 是 | 时间戳所在时区，即设备上报时区。 |
| originTimestamp | number | 是 | 入参文本时间戳，即设备上报时间。 |

### 地点实体

识别文本中出现的地点，返回类型为JSONObject，键为“location”，键对应的值类型为JSONArray，数组里值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 地点类型：首层核心地点的实际类型。比如: “银行旁边的邮政局”，  type：参考邮政局的类型。 |
| coreLocation | JSONObject | 是 | 核心地点信息组成元素集合。  coreLocation：“邮政局”对应的组成元素分析结果。 |
| adornLocation | JSONObject | 否 | 修饰核心地点的组成元素集合，引用location定义。  adornLocation：“银行旁边的”对应的组成元素分析结果。 |
| isAbstract | number | 否 | 0：非抽象地点。  1：和意图相关的抽象地点。  默认为0。 |

地点实体内，coreLocation参数的定义，具体字段如下表。

| **子参数** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| oriText | string | 是 | 地点实体。 |
| value | string | 否 | 核心地点信息（地点原文去除修饰地点、修饰词后（旁边|附近）的地点信息）。  value：邮政局。  当词性为nsf 、nsw开头时，只填value字段。 |
| province | JSONObject | 否 | 省份，原文中出现的省份。 |
| city | JSONObject | 否 | 城市，原文中出现的城市。 |
| county | JSONObject | 否 | 县，原文中出现的县。 |
| district | JSONObject | 否 | 行政区，原文中出现的行政区，如“江宁区”。 |
| subDistrict | JSONObject | 否 | 街道/社区。 |
| town | JSONObject | 否 | 乡/镇。 |
| village | JSONObject | 否 | 村。 |
| subVillage | JSONObject | 否 | 村组。 |
| region | JSONObject | 否 | 参考物，固定商区、片区（不包含行政区）的概念 ，对应大众点评region字段（识别范围大于大众点评的对应字段）。 |
| road | JSONObject | 否 | 道路。 |
| default | JSONObject | 否 | 未分类区域，语义无法区分出该区域类地点属于哪个类型，比如 福永既可能是镇、也可能是街道，文本中只出现福永且上下文无法判断类型时输出到该字段。 |
| location | JSONObject | 否 | 地图poi信息/组织机构/抽象地点。 |

coreLocation内，参数类型为JSONObject的参数的定义，具体字段如下表。

| **子参数** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| value | string | 否 | 地点类型对应的地点信息。 |
| extend | JSONObject | 否 | 地点扩展信息。 |

### 姓名实体

识别文本中出现的人名，返回类型为JSONObject，键为“name”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | nr（正式），nrn（昵称），nrt（称谓），nrx（其他）。 |

### 手机号实体

识别文本中出现的电话号码，返回类型为JSONObject，键为“phoneNum”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| type | number | 是 | 号码类型，0（固话）、1（手机）。 |
| number | string | 是 | 号码（去除分机号）。  手机号示例：138\*\*\*\*\*78  固话示例：010-1\*\*\*\*\*78 |
| extNumber | string | 否 | 分机号，当类型为固话时可能存在该字段。 |

### 邮箱实体

识别文本中出现的邮箱，返回类型为JSONObject，键为“email”，键对应的值为空。

### URL实体

识别文本中出现的URL，返回类型为JSONObject， 键为“url”，键对应的值为空。

## 娱乐类

### 火车车次实体

识别文本中出现的火车车次，返回类型为JSONObject， 键为“trainNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| sequence | number | 是 | 对应实体出现频率。 |

### 航班号实体

识别文本中出现的飞机航班，返回类型为JSONObject， 键为“flightNo”，键对应的值为空。

## 生活类

### 快递单号实体

识别文本中出现的快递单号，返回类型为JSONObject，键为“expressNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| isTailNum | number | 是 | 是否为单号尾号，0（不是尾号）、1（是尾号）。 |

### 身份证号实体

识别文本中出现的身份证号，返回类型为JSONObject， 键为“idNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| number | string | 是 | 身份证号码字串。 |
| sequence | number | 是 | 对应实体出现频率。 |
| type | number | 是 | 0（身份证）、1（护照）。 |
| isComplete | number | 是 | “1”（证件号是完整的，不含\*等字符），“0”（证件号不是完整的，含有\*等字符，例如321\*\*\*\*\*\*\*\*\*\*\*1234）。 |

### 验证码实体

识别文本中出现的验证码，返回类型为JSONObject， 键为“verificationCode”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 验证码类型（取原文内容，如：验证码、校验码等）。 |
| supplier | string | 否 | 验证码提供商。 |

### 银行卡号实体

识别文本中出现的银行卡号，返回类型为JSONObject， 键为“bankCardNo”，键对应的值类型为JSONArray，数组里的值类型为JSONObject，具体字段如下表。

| **参数名** | **类型** | **是否必选** | **说明** |
| --- | --- | --- | --- |
| number | number | 是 | 银行卡号中的数字。 |
| sequence | number | 是 | 对应实体出现频率。 |
| validDate | string | 否 | 银行卡号有效期。 |
