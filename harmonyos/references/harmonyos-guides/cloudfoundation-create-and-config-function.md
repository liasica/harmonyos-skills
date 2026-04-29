---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-create-and-config-function
title: 创建函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 创建函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d39175f3226618c0f0a1c042e8f7b11566cd19274bb3032877154036487f750e
---

## 创建函数

开通云函数服务后，首先需要在AGC中创建函数，并添加函数执行的代码。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击需要创建云函数的项目。
3. 在左侧导航栏选择“云开发（Serverless） > 云函数”，进入云函数主界面。
4. 选择“函数”页签，点击“创建函数”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/6eD1H8nSSFCQi-I1O17x3Q/zh-cn_image_0000002558765344.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=98BA86338518636538C76C080BE140E652E0ED15843C4AE9613EB7B302D06DE7)
5. 页面右侧抽屉式滑出“创建函数”窗口，按照“函数配置 -> 触发器 -> 函数代码 -> 层配置”引导顺序配置函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/2SrYNOsWRbOSxda7AyatUg/zh-cn_image_0000002558605688.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=6FA7E2E5D5B855FAF379F75CA7767231CBC4755A4DA1F15EB097E444549367DB)

## 函数配置

1. 在“函数配置”页面，配置“函数名称”、“触发方式”、“超时时长”等函数信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/-Mr1C4wSSaiS6ukmxlRa5g/zh-cn_image_0000002589325215.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=4D7C8274480992CAB8AC9AE6329BE2DE24A599A95CE4A806DB39D586B684127E)

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

     点击“新增变量”，输入key和value值，如下图中所示，env1为环境变量的key值，test为value值。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/zUnx7nPXTGaXwbJ7uGh6Xg/zh-cn_image_0000002589245151.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=0AD53096CA80F88EEFBF279354BAC4E19D29586FB3B63F0DDF381644552DA701)可将变量删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/GVK5wgKYRnCUWakKZz6Djg/zh-cn_image_0000002558765346.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=5DFEBD341FF778DC2D33431A4CFE05FF16D7111BCA5A87C7AD6B12E57861B8B9)
   * JSON格式编辑

     选中“JSON格式编辑”，在文本框中以key-value键值对JSON格式添加环境变量。当添加的环境变量比较多时，为了方便核对，可点击“format”对变量进行格式化排列。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/qs0nYKE4T8y9oUxG_2Ofxg/zh-cn_image_0000002558605690.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=E9D037927B23A4983B0B8B889D07D9D81713B672B6D23D8F1E7C928051C3AB70)
3. “函数配置”页面配置完成后点击“下一步”。

## 触发器

进入“触发器”页面，可基于函数触发场景配置需要的触发器，本场景下添加HTTP触发器。“触发器类型”和“请求方式”保持默认选择，并配置“认证类型”，配置完成后点击“下一步”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ePz18ACCTpO_hIf7RiexiA/zh-cn_image_0000002589325217.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=F8664EBDD8194B22274935AEF9D4DF434B011C514066C422DD59854897D3310E)

| 参数 | 说明 |
| --- | --- |
| 触发器类型 | HTTP触发器。 |
| 请求方式 | HTTP触发器目前仅支持POST请求方式。 |
| 认证类型 | HTTP触发器的认证类型。  - API客户端鉴权（Client适用）：端侧网关认证，适用于来自APP客户端侧（即本地应用或者项目）的函数调用。  - API客户端鉴权（Server适用）：云侧网关认证，适用于来自APP服务器侧（即云函数）的函数调用。 |
| 启用decode | 通过HTTP触发器触发函数时，对于contentType为“application/x-www-form-urlencoded”的触发请求，是否使用URLDecoder对请求body进行解码再传入到函数中。 |

## 函数代码

进入“函数代码”页面，配置“运行环境”、“内存配置”、“代码输入类型”等信息，配置完成后点击“下一步”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/aCKFwdojRMi3rwnZGhljuQ/zh-cn_image_0000002589245153.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=DFEE0E46E93FF6E765F162087527D0F8794DCCF0355A289B02733222FE00AA03)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/-4VXoFyhS9amB-yZKiTycQ/zh-cn_image_0000002558605692.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=6CD6FC1EA9720953A0052818CF2CF87231E0B387334ED71E4A3E113B3228B524)

| 组成 | 说明 |
| --- | --- |
| 目录树 | 目录树支持如下能力：  - 新增文件夹：选中一个文件或文件夹，点击右上角新增文件夹按钮“”。若选中的是文件夹，则新增一个子文件夹。若选中的是文件，则新增一个同级文件夹。  - 新增文件：选中一个文件或文件夹，点击右上角新增文件按钮“”。若选中的是文件夹，则新增一个子文件。若选中的是文件，则新增一个同级文件。  - 删除文件：选中一个文件或文件夹，点击右侧删除按钮“”，删除文件或文件夹。不允许删除根目录。  - 重命名：双击文件或文件夹，输入新名称（仅支持字母、数字、下划线和中划线），完毕后按Enter键完成重命名。 |
| 编辑器 | 编辑器具有如下能力：  - 语法高亮：按照node.js语法高亮显示代码。  - 语法校验：语法有错误时会给出错误提示。  - 代码提示：输出代码自动给出相关代码提示。  - 代码填充：选择后系统代码可自动填充。  - 格式化：快捷键Ctrl+Shift+B。  - 支持快捷键操作：Ctrl+v, Ctrl+c, Ctrl+z, Ctrl+x, Ctrl+f, Ctrl+/等。 |
| 最大化 | 点击最大化按钮，可以最大化在线编辑区，再次点击按钮或按ESC键退出最大化。 |

## 层配置

层可以提供公共依赖库的发布与部署能力。开发者可以将函数依赖的公共库和相关依赖项提炼到层，通过为函数绑定层，便可以在函数中使用库，而不必将库包含在函数的代码包中，从而达到缩小函数代码包体积与缩短函数部署时间的效果，也避免了使用函数代码安装和打包依赖项时可能出现的错误。详细的层管理功能，请参见[层管理](../AppGallery-connect-Guides/agc-cloud-function-layer-0000001517762624.md)。

如果尚未创建层，可跳过下述步骤，直接点击页面底部的“创建”完成函数定义，后续创建层之后可在函数详情页再进行层配置，为函数绑定层。如果在创建函数之前已创建层，可按照下述步骤进行操作。

1. 进入“层配置”页面，点击“绑定层”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/nvhiUSFfR1a3LbWE6Ettag/zh-cn_image_0000002589245157.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=ED1F35917A5956407F42B3B26EBC87E14730FD2E8214FE35E2D6A205EF856BB5)
2. 在右侧弹出的“绑定层”界面中，下拉框选择“层名称”和“版本”，“层范围”等信息根据层的配置将被自动填充，完成层绑定后点击“确定”。一个函数最多可以绑定5个层。

   说明

   选择层时，层的兼容运行时需与函数运行环境相符，系统会自动完成过滤。如果无匹配的层，请参考[创建层](../AppGallery-connect-Guides/agc-cloud-function-layer-0000001517762624.md#section11358162018572)创建相同运行环境的层后再进行绑定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Zoy_Q28qT5iVPcavrpyERQ/zh-cn_image_0000002558765352.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=EFE13BB5A3749F4F33E7970CE2D5D2124831B1217BF86CA06B9F342CD6B3211D)

   | 参数 | 说明 |
   | --- | --- |
   | 层名称 | 层的名称。重复时自动在同名的层中创建一个新版本。 |
   | 版本 | 存在多个层版本时，选择函数绑定的层版本。 |
   | 层范围 | 层的共享范围。  - 项目内共享  - 团队内共享 |
   | 兼容运行时 | 层使用的语言环境。请选择“nodejs”。 |
   | 层描述 | 层的附加说明，长度不超过1024位。 |
3. 返回到“层配置”界面，绑定成功的层将展示在层列表中。如果需要解除层与函数的绑定关系，点击“解绑”即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/GdDVZ4yeTc-6wqqCCLLQNA/zh-cn_image_0000002558605696.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=384128F4379626F3A371928533458A0C9066B0A6FB3B31A832C4AD4BA4E30CB4)
4. 按照“函数配置 -> 触发器 -> 函数代码 -> 层配置”顺序配置过程中，如果需要修改前面步骤中的配置，可点击“上一步”进行回退，配置完成后点击“创建”提交函数定义。

## 更多信息

函数配置完成后，可以[修改函数高级配置](../AppGallery-connect-Guides/modify-function-advanced-config-0000001734287937.md)。
