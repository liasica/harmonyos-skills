---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-creating-operator-project-msopgen
title: 算子工程创建工具参数说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 算子工程创建工具参数说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:35+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5bde4b5e5494b8cbdf71f178eeb0b7df13238b02aa2ecdd1a0a0f7cbecc69f50
---

## 工具概述

完成算子分析和原型定义后，可使用msOpGen工具生成自定义算子工程，并进行编译部署。

## 命令汇总

执行如下命令，参数说明请参见表1。

说明

开发者按照输入的配置参数生成算子模板后，建议在运行前确认算子工程代码的安全性。

```
1. msopgen gen -i {*.json} -f {framework type} -c {Compute Resource} -lan cpp -out {Output Path}
```

**表1** 创建算子工程参数说明

| 参数名称 | 参数描述 | 是否必选 |
| --- | --- | --- |
| gen | 用于生成算子开发交付件。 | 是 |
| -i，--input | 算子原型定义文件（.json）路径，可配置为绝对路径或者相对路径。工具执行开发者需要有此路径的可读权限。 | 是 |
| -f，--framework | 框架类型。  - 默认为TensorFlow框架，默认值：tf或者tensorflow  - ONNX框架，参数值：onnx  **说明：** 所有参数值大小写不敏感。 | 否 |
| -c，--compute\_unit | 算子使用的计算资源。  配置格式为：ai\_core-{soc version}，ai\_core与{soc version}之间用中划线“-”连接。  请根据实际Kirin AI处理器版本进行选择。  **说明：** AI处理器的型号[/topic/body/section/table/tgroup/tbody/row/entry/p/soc\_version {""})  (soc\_version]  请通过在运行环境上通过命令行获取：  hdc -t {target} shell param get ohos.boot.chiptype。  target：设备的SN码，可以通过hdc list targets获取当前环境上所有设备的SN码。  当前支持的AI处理器型号为Kirin9020/KirinX90。 | 是 |
| -out，--output | 生成文件所在路径，可配置为绝对路径或者相对路径，并且工具执行开发者具有可读写权限。  若不配置，则默认生成在执行命令的当前路径。  **说明：** 若开发者指定的输出目录中存在与模板工程重名的文件，输出目录中的文件将会被模板工程的文件覆盖。 | 否 |
| -m，--mode | 生成交付件模式。  0：创建新的算子工程，若指定的路径下已存在算子工程，则会报错退出。  1：在已有的算子工程中追加算子。  默认值：0。 | 否 |
| -op，--operator | 配置算子的类型，如：Conv2DTik。  若不配置此参数，当算子原型定义文件中存在多个算子时，工具会提示开发者选择算子。 | 否 |
| -lan，--language | 算子编码语言。  cpp：基于AscendC编程框架，使用C/C++编程语言进行开发。  默认值：cpp。 | 否 |
| -h，--help | 输出帮助信息。 | 否 |

**表2** json文件配置参数说明

| 配置字段 | 配置字段 | 类型 | 含义 | 是否必选 |
| --- | --- | --- | --- | --- |
| op | - | string | 算子的Operator Type。 | 是 |
| input\_desc | - | list | 输入参数描述。 | 否 |
| input\_desc | name | string | 算子输入参数的名称。 | 否 |
| input\_desc | param\_type | string | 参数类型：  - required  - optional  - dynamic  未配置默认为required。 | 否 |
| input\_desc | format | list | 针对类型为tensor的参数，配置为tensor支持的数据排布格式。  包含如下取值：  ND、NHWC、NCHW、HWCN、NC1HWC0、FRACTAL\_Z等。  **说明：** format与type需一一对应。若仅填充其中一项的唯一值，msOpGen工具将会以未填充项的唯一输入值为准自动补充至已填充项的长度。例如开发者配置为format:["ND"] /type:["fp16","float","int32"]，msOpGen工具将会以format的唯一输入值（"ND"）为准自动补充至type参数的长度，自动补充后的配置为format:["ND","ND","ND"]/type:["fp16","float","int32"]。 | 否 |
| input\_desc | type | list | 算子参数的类型。  取值范围：float、half、float16 (fp16)、float32 (fp32)、int8、int16、int32、int64、uint8、uint16、uint32、uint64、qint8、qint16、qint32、quint8、quint16、bool、double、string、resource、complex64、complex128、bf16、numbertype、realnumbertype、quantizedtype、all、BasicType、IndexNumberType等。  **注意：** Kirin9020与KirinX90暂不支持float类型作为输入。  **说明：** format与type需一一对应。 | 否 |
| input\_desc | value\_depend | string | 该配置字段可选。若配置该字段，表示算子输入为Const类型。取值范围：  - required：表示算子的输入必须是Const类型。会校验算子的输入是否是Const类型。若校验通过，则将此输入的值下发到算子，否则报错。  - optional：表示算子的输入可以是Const类型，也可以不是Const类型。如果输入是Const类型，则将输入的值下发到算子，否则不下发。 | 否 |
| output\_desc | - | list | 输出参数描述。 | 是 |
| output\_desc | name | string | 算子输出参数的名称。 | 是 |
| output\_desc | param\_type | string | 参数类型：  - required  - optional  - dynamic  未配置默认为required。 | 是 |
| output\_desc | format | list | 针对类型为tensor的参数，配置为tensor支持的数据排布格式。  包含如下取值：  ND、NHWC、NCHW、HWCN、NC1HWC0、FRACTAL\_Z等。  **说明：** format与type需一一对应。若仅填充其中一项的唯一值，msOpGen工具将会以未填充项的唯一输入值为准自动补充至已填充项的长度。例如开发者配置为format:["ND"] /type:["fp16","float","int32"]，msOpGen工具将会以format的唯一输入值（"ND"）为准自动补充至type参数的长度，自动补充后的配置为format:["ND","ND","ND"]/type:["fp16","float","int32"]。 | 是 |
| output\_desc | type | list | 算子参数的类型。  取值范围：float、half、float16 (fp16)、float32 (fp32)、int8、int16、int32、int64、uint8、uint16、uint32、uint64、qint8、qint16、qint32、quint8、quint16、bool、double、string、resource、complex64、complex128、bf16、numbertype、realnumbertype、quantizedtype、all、BasicType、IndexNumberType等。  **注意：** Kirin9020与KirinX90暂不支持float类型作为输入。  **说明：** format与type需一一对应。 | 是 |
| attr | - | list | 属性描述。 | 否 |
| attr | name | string | 算子属性参数的名称。 | 否 |
| attr | param\_type | string | 参数类型：  - required  - optional  未配置默认为required。 | 否 |
| attr | type | string | 算子参数的类型。  包含如下取值：  int、bool、float、string、list\_int、list\_float、list\_bool，其他请参考[OpAttrDef](cannkit-opattrdef.md)进行修改。 | 否 |
| attr | default\_value | - | 默认值。 | 否 |
