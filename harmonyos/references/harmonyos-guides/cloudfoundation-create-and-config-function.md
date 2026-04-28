---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-create-and-config-function
title: 创建函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 创建函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:16498205673a137e889e1d9b73d40dc351fb97046b3f3104ae0ab5f7e33a3865
---

## 创建函数

开通云函数服务后，首先需要在AGC中创建函数，并添加函数执行的代码。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击需要创建云函数的项目。
3. 在左侧导航栏选择“云开发（Serverless） > 云函数”，进入云函数主界面。
4. 选择“函数”页签，点击“创建函数”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/V-yLFkH0QyK2MYjH4vLPOw/zh-cn_image_0000002552958844.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=6A7134210A1942B0D8E888007A29CDF13D78D1CB9E5A0A8A3E47825CD70D6C8E)
5. 页面右侧抽屉式滑出“创建函数”窗口，按照“函数配置 -> 触发器 -> 函数代码 -> 层配置”引导顺序配置函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/eWNt-g-WRRatL35hEdPKxw/zh-cn_image_0000002583478845.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=EC6C2E6CFE0F4FB0A38383D7D7EBF93096E23A498C65CFED55390B03F1FBF3E9)

## 函数配置

1. 在“函数配置”页面，配置“函数名称”、“触发方式”、“超时时长”等函数信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/RWWcY2IDS0GG2IV1zPJ3WA/zh-cn_image_0000002552799196.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=D7BBB86D87FD9C286BA03727C64659CAFFDF252B8506CDE8F5C1980744AC4546)

   | 配置项 | **说明** |
   | --- | --- |
   | 函数名称 | 函数的名称。 |
   | 描述 | 函数的描述信息。 |
   | 触发方式 | **请配置为“事件调用”。**  “事件调用”表示通过触发器方式调用函数。 |
   | 超时时长 | 函数最大运行时长，超过该时长，则默认函数执行失败，单位为秒，取值范围为1~1800。不同调用方式下，函数最大运行时长不同：  - “同步”调用方式时，函数最大运行时长为55秒。  - “异步”调用方式时，函数最大运行时长为1800秒。 |
   | 实例并发 | 函数请求并发量上限，单位为个，取值范围为1~10000。 |
   | 环境变量 | key-value形式，可以将需要的变量配置信息传入函数执行环境中，用于函数在运行时读取和使用。 |
2. （可选）可根据需要添加环境变量，支持**表单格式**和**JSON格式**两种编辑方式。添加完成后，还可以点击“JSON格式导出”，导出以“函数名称.json”格式命名的环境变量文件，以备后续使用。

   说明

   * 环境变量的key值具有唯一性，且“PROJECT\_CREDENTIAL”和“AGC\_”为系统级环境变量标识，不允许添加以其命名或以其为前缀的环境变量。
   * 环境变量总数不超过1000个。

   * 表单格式编辑

     点击“新增变量”，输入key和value值，如下图中所示，env1为环境变量的key值，test为value值。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/NRmt9qZ2QbW6FmIb7BK-lQ/zh-cn_image_0000002583438891.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=D4983D4F13EAE61B9624E50365C88D15A7430DF24A2A614F8CC34C69ED0BEDA0)可将变量删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/YbEmJet8TRCKri1T7DNNEg/zh-cn_image_0000002552958846.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=D7A18F94CC8D5662FFEC801C710893978138DCD8FA777D213FC4E415736890B2)
   * JSON格式编辑

     选中“JSON格式编辑”，在文本框中以key-value键值对JSON格式添加环境变量。当添加的环境变量比较多时，为了方便核对，可点击“format”对变量进行格式化排列。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/P6MmttecTty5wLSBHTAjaw/zh-cn_image_0000002583478847.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=72B6CA07C41922AFB45B900A8D45BDA6FE3F22E80291DC4C04C00A50CE2FBA16)
3. “函数配置”页面配置完成后点击“下一步”。

## 触发器

进入“触发器”页面，可基于函数触发场景配置需要的触发器，本场景下添加HTTP触发器。“触发器类型”和“请求方式”保持默认选择，并配置“认证类型”，配置完成后点击“下一步”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/S2k2Mh_jS3-_GYPlt3kFog/zh-cn_image_0000002552799198.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=07FF756D47C5ACE7643909361473EC11B40F1007C8B0F4A15678CCC6411D50F2)

| 参数 | 说明 |
| --- | --- |
| 触发器类型 | HTTP触发器。 |
| 请求方式 | HTTP触发器目前仅支持POST请求方式。 |
| 认证类型 | HTTP触发器的认证类型。  - API客户端鉴权（Client适用）：端侧网关认证，适用于来自APP客户端侧（即本地应用或者项目）的函数调用。  - API客户端鉴权（Server适用）：云侧网关认证，适用于来自APP服务器侧（即云函数）的函数调用。 |
| 启用decode | 通过HTTP触发器触发函数时，对于contentType为“application/x-www-form-urlencoded”的触发请求，是否使用URLDecoder对请求body进行解码再传入到函数中。 |

## 函数代码

进入“函数代码”页面，配置“运行环境”、“内存配置”、“代码输入类型”等信息，配置完成后点击“下一步”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/XhCjI9MQR4-RLKTqzEFj2g/zh-cn_image_0000002583438893.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=657F577EFEE9608F410436D652CF910E4ED8152F3B35DEAE5A3D200F7D9B2EC7)

| 配置项 | **说明** |
| --- | --- |
| 运行环境 | 函数容器的运行环境。请选择nodejs 20.x/latest，其中latest表示使用最新版本。 |
| 内存配置 | 函数容器所占有的内存大小，单位为MB，取值范围：500，1000，2000，4000。 |
| 代码输入类型 | 包括“在线编辑”与“\*.zip文件”两种方式，默认值为“在线编辑”。  选择“\*.zip文件”方式部署云函数时，入口方法文件的编写方法请参见[入口方法](cloudfoundation-develop-function-nodejs.md#入口方法)。 |
| 函数入口 | 包括入口文件名称和入口方法名称，通过“.”连接。例如handler.myHandler，其中handler为入口文件名称，myHandler为入口方法名称。  nodejs运行环境下入口文件必须放置在函数部署包的根目录下，具体请参见[准备函数部署包](cloudfoundation-develop-function-nodejs.md#准备函数部署包)。 |
| 代码文件 | 用于在线编辑函数代码或上传函数部署包。  - “代码输入类型”配置项选择“在线编辑”时，可在创建函数界面集成的WebIDE区域在线编辑函数代码。WebIDE的详细使用方法见下文。  - “代码输入类型”配置项选择“\*.zip文件”时，点击即可上传函数部署包，也可直接拖曳zip文件至虚线框内。 |

**WebIDE**

当“代码输入类型”配置项选择“在线编辑”时，创建函数界面中集成了WebIDE功能，支持在线编辑函数代码。

说明

如果在函数实例已经运行的情况下进行函数代码或配置更新，AGC后台会滚动更新函数实例，请耐心等待10-20秒。

WebIDE从左至右分两个部分：目录树、代码编辑器和最大化，如下图所示。编辑完成后平台会生成部署包并上传。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/IBGdM7RMRCO2i8tHiZCs7w/zh-cn_image_0000002583478849.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=B5C3EB2CFD97E0CA22023BB526552D1CAC1A89AA6BA8C291E49822D23D91B03B)

| 组成 | 说明 |
| --- | --- |
| 目录树 | 目录树支持如下能力：  - 新增文件夹：选中一个文件或文件夹，点击右上角新增文件夹按钮“”。若选中的是文件夹，则新增一个子文件夹。若选中的是文件，则新增一个同级文件夹。  - 新增文件：选中一个文件或文件夹，点击右上角新增文件按钮“”。若选中的是文件夹，则新增一个子文件。若选中的是文件，则新增一个同级文件。  - 删除文件：选中一个文件或文件夹，点击右侧删除按钮“”，删除文件或文件夹。不允许删除根目录。  - 重命名：双击文件或文件夹，输入新名称（仅支持字母、数字、下划线和中划线），完毕后按Enter键完成重命名。 |
| 编辑器 | 编辑器具有如下能力：  - 语法高亮：按照node.js语法高亮显示代码。  - 语法校验：语法有错误时会给出错误提示。  - 代码提示：输出代码自动给出相关代码提示。  - 代码填充：选择后系统代码可自动填充。  - 格式化：快捷键Ctrl+Shift+B。  - 支持快捷键操作：Ctrl+v, Ctrl+c, Ctrl+z, Ctrl+x, Ctrl+f, Ctrl+/等。 |
| 最大化 | 点击最大化按钮，可以最大化在线编辑区，再次点击按钮或按ESC键退出最大化。 |

## 层配置

层可以提供公共依赖库的发布与部署能力。开发者可以将函数依赖的公共库和相关依赖项提炼到层，通过为函数绑定层，便可以在函数中使用库，而不必将库包含在函数的代码包中，从而达到缩小函数代码包体积与缩短函数部署时间的效果，也避免了使用函数代码安装和打包依赖项时可能出现的错误。详细的层管理功能，请参见[层管理](../AppGallery-connect-Guides/agc-cloud-function-layer-0000001517762624.md)。

如果尚未创建层，可跳过下述步骤，直接点击页面底部的“创建”完成函数定义，后续创建层之后可在函数详情页再进行层配置，为函数绑定层。如果在创建函数之前已创建层，可按照下述步骤进行操作。

1. 进入“层配置”页面，点击“绑定层”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/ZE0FlPRbQQGoz4PPotHcvg/zh-cn_image_0000002583438897.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=E2CFD2AC65E082E18C9352FD39C8D90540DAA606344CA32A9B07554E9DB65E64)
2. 在右侧弹出的“绑定层”界面中，下拉框选择“层名称”和“版本”，“层范围”等信息根据层的配置将被自动填充，完成层绑定后点击“确定”。一个函数最多可以绑定5个层。

   说明

   选择层时，层的兼容运行时需与函数运行环境相符，系统会自动完成过滤。如果无匹配的层，请参考[创建层](../AppGallery-connect-Guides/agc-cloud-function-layer-0000001517762624.md#section11358162018572)创建相同运行环境的层后再进行绑定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/wqz8iZ6jSzuNFpcFrnnjsQ/zh-cn_image_0000002552958852.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=F22887CE1B225E50FAEDE744CF7FCD69E5C1B97F675C0778D2C811433073A00E)

   | 参数 | 说明 |
   | --- | --- |
   | 层名称 | 层的名称。重复时自动在同名的层中创建一个新版本。 |
   | 版本 | 存在多个层版本时，选择函数绑定的层版本。 |
   | 层范围 | 层的共享范围。  - 项目内共享  - 团队内共享 |
   | 兼容运行时 | 层使用的语言环境。请选择“nodejs”。 |
   | 层描述 | 层的附加说明，长度不超过1024位。 |
3. 返回到“层配置”界面，绑定成功的层将展示在层列表中。如果需要解除层与函数的绑定关系，点击“解绑”即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Zbjv1v6cTYCAr3VO9b053w/zh-cn_image_0000002583478853.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=663D41DF2D91140C42E5A505A867A4615A2F88D95B9CAAA1C036A560F81ACD81)
4. 按照“函数配置 -> 触发器 -> 函数代码 -> 层配置”顺序配置过程中，如果需要修改前面步骤中的配置，可点击“上一步”进行回退，配置完成后点击“创建”提交函数定义。

## 更多信息

函数配置完成后，可以[修改函数高级配置](../AppGallery-connect-Guides/modify-function-advanced-config-0000001734287937.md)。
