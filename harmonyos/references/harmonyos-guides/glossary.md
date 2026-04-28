---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/glossary
title: HarmonyOS术语
breadcrumb: 指南 > 基础入门 > HarmonyOS术语
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b45c75f7d1ab2a4bb5d6f14dc6f2a3fdd915b7868aa0f0c5e35ffab9ab6c8e3
---

## A

### abc文件

方舟字节码（ArkCompiler Bytecode）文件，是ArkCompiler的编译工具链以源代码作为输入编译生成的产物，其文件后缀名为.abc。在发布态，abc文件会被打包到HAP中。

### ANS

Advanced Notification Service，通知增强服务，是HarmonyOS中负责处理通知的订阅、发布和更新等操作的系统服务。

### Atomic Service，元服务

原名元服务，是HarmonyOS提供的一种面向未来的服务提供方式，是有独立入口的（用户可通过点击服务卡片打开元服务）、免安装的（无需显式安装，由系统程序框架后台安装后即可使用）用户应用程序形态。

### ArkUI

方舟开发框架，是为HarmonyOS平台开发极简、高性能、跨设备应用设计研发的UI开发框架，支撑开发者高效地构建跨设备应用UI界面。

### ArkCompiler

方舟编译器，是华为自研的统一编程平台，包含编译器、工具链、运行时等关键部件，支持高级语言在多种芯片平台的编译与运行，可支撑传统应用、元服务运行在手机、个人电脑、平板、电视、汽车和智能穿戴等多种设备上的需求。

## D

### DFX

Design For X（也称Design For eXcellence），是面向产品生命周期各环节的设计，其中X代表产品生命周期的某一个环节或特性。例如DFR表示Design for Reliability，即可靠性设计；DFT表示Design for Testability，即可测试性设计。DFX设计涵盖了产品所有的非功能性设计，包括研发、制造、运维、服务等环节，对产品效率、成本、质量、体验等至关重要。

### DV

Device Virtualization，设备虚拟化，通过虚拟化技术可以实现不同设备的能力和资源融合。

## E

### ExtensionAbility

Stage模型中的组件类型名，即ExtensionAbility组件，提供特定场景（如卡片、输入法）的扩展能力，满足更多的使用场景。

## F

### FA模型

HarmonyOS早期版本开始支持的应用模型，已经不再主推。建议使用新的[Stage模型](glossary.md#stage模型)进行开发。

## H

### HAP

Harmony Ability Package，一个HAP文件包含应用的所有内容，由代码、资源、三方库及应用配置文件组成，其文件后缀名为.hap。

### HarmonyOS

HarmonyOS是新一代的智能终端操作系统，为不同设备的智能化、互联与协同提供了统一的语言。带来简洁、流畅、连续、安全可靠的全场景交互体验。

2024年HarmonyOS以全新架构发布，命名为HarmonyOS NEXT。HarmonyOS NEXT于2024年6月21日公开发布首个Developer Beta版本，并于2024年10月22日正式公开发布首个Release版本（版本号5.0.0）。HarmonyOS NEXT采用[OpenHarmony](glossary.md#openharmony)作为操作系统底座，并通过OpenHarmony兼容性标准认证。全新架构下的HarmonyOS实现了对全场景体验的底层优化，系统更流畅，隐私安全能力更强大。给消费者带来更高效、更流畅、更便捷、更安全的智能化操作体验。

### HDF

Hardware Driver Foundation，硬件驱动框架，用于提供统一外设访问能力和驱动开发、管理框架。

### HML

HarmonyOSMarkup Language，是一套类HTML的标记语言。通过组件、事件构建出页面的内容。页面具备数据绑定、事件绑定、列表渲染、条件渲染等高级能力。

### Hop，流转

在HarmonyOS中泛指涉及多端的分布式操作。流转能力打破设备界限，多设备联动，使用户应用程序可分可合、可流转，实现如邮件跨设备编辑、多设备协同健身、多屏游戏等分布式业务。

流转为开发者提供更广的使用场景和更新的产品视角，强化产品优势，实现体验升级。

## I

### IDN

Intelligent Distributed Networking，是HarmonyOS特有的分布式组网能力单元。开发者可以通过IDN获取分布式网络内的设备列表和设备状态信息，以及注册分布式网络内设备的在网状态变化信息。

## K

### Kit

是一个功能内聚的开放能力集合，可以支撑开发者完成一个特定场景的功能开发。

## M

### Manual hop，用户手动流转

是指开发者在用户应用程序中内嵌规范的流转图标，使用户可以手动选择合适的可选设备进行流转。用户点击图标后，会调起系统提供的流转面板。面板中会展示出用户应用程序的信息及可流转的设备，引导用户进行后续的流转操作。

### MSDP

Mobile Sensing Development Platform，移动感知平台。MSDP子系统提供分布式融合感知能力，借助HarmonyOS分布式能力，汇总融合来自多个设备的多种感知源，从而精确感知用户的空间状态、移动状态、手势、运动健康等多种状态，构建全场景泛在基础感知能力，支撑智慧生活新体验。

### Multi-device collaboration，多端协同

是一种实现用户应用程序流转的技术方案。指多端上的不同UIAbility协同运行或接力运行以实现完整业务；或者，多端上的相同UIAbility同时运行以实现完整业务；或者，UIAbility跨端调用ExtensionAbility以实现完整业务。

## O

### OpenHarmony

2020年，华为将HarmonyOS基础能力捐赠给开放原子开源基金会，形成HarmonyOS开源项目。HarmonyOS能够提供操作系统底层能力，包括应用框架及UI框架，基础服务（如分布式管理、数据、文件等），基础应用（如桌面、设置的基本能力，以及日历、联系人等基础应用）。

## P

### PC/2in1

即PC设备，主要交互方式以多窗口、多任务及键盘鼠标操作为主，可充分发挥设备的生产力属性。在HarmonyOS文档中，所有“2in1”均指“PC/2in1”。

## S

### SDK

Software Development Kit，软件开发工具包，是用于创建应用软件的开发工具和开放能力的集合。

### Service widget，服务卡片

简称卡片，将用户应用程序的重要信息以卡片的形式展示在桌面等系统入口，用户可通过点击卡片实现功能快捷操作，以达到服务直达、减少层级跳转的目的。

### Stage模型

HarmonyOS 3.1 Developer Preview版本开始新增的应用模型，提供UIAbility、ExtensionAbility两大类应用组件。由于该模型还提供了AbilityStage、WindowStage等类作为应用组件和Window窗口的“舞台”，因此称之为Stage模型。

### Super virtual device，超级虚拟终端

亦称超级终端，通过分布式技术将多个终端的能力进行整合，存放在一个虚拟的硬件资源池里，根据业务需要统一管理和调度终端能力，来对外提供服务。

### System suggested hop，系统推荐流转

是指当用户使用用户应用程序时，所处环境中存在使用体验更优的可选设备，则系统自动为用户推荐该设备，用户可确认是否启动流转。

## U

### UIAbility

Stage模型中的组件类型名，即UIAbility组件，包含UI，提供展示UI的能力，主要用于和用户交互。

### UX

也称UE，即User Experience，用户体验，是用户在使用一个产品或系统之前、使用期间和使用之后的全部感受。
