---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/assessment-guide
title: 评估管理开发指南
breadcrumb: 指南 > 系统 > 基础功能 > Automatic Scene Configuration Kit（场景配置服务） > 评估管理开发指南
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:47+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:58633a00f35b75732783c364129a79d2fd0f6a9cca0b552c8969261cfe2e18b6
---

## 功能介绍

本文指导开发者接入评估管理能力，完成开始评估、查询评估状态与结束评估的开发。Kit级能力范围与约束参见[Automatic Scene Configuration Kit简介](assessment-kit-intro.md)，名词定义参见[Automatic Scene Configuration Kit术语](assessment-glossary.md)。

评估管理模块提供以下能力：

* 开始评估：调用begin接口发起评估，系统弹出确认弹窗，用户确认后设备进入评估模式。可通过评估配置指定评估最大时长与评估期间允许运行的应用白名单。
* 结束评估：调用end接口结束评估，系统解除评估模式下对系统能力的限制。
* 评估状态查询与配置获取：调用isActive接口查询当前是否处于评估状态，调用getConfiguration接口获取当前评估配置。
* 评估过程回调：通过IAssessmentCallback接收评估开始（onBegin）、评估中断（onInterrupted）、评估结束（onEnd）事件。

## 约束与限制

进入评估模式后设备功能被大幅限制，为防止第三方应用滥用该能力，调用评估管理接口需申请权限[ohos.permission.ASSESSMENT\_CONFIGURATION](restricted-permissions.md#ohospermissionassessment_configuration)。

**表1** 权限信息

| 权限名 | 权限级别 | 授权方式 | 应用开放范围 |
| --- | --- | --- | --- |
| ohos.permission.ASSESSMENT\_CONFIGURATION | system\_basic | 系统授权（system\_grant） | 普通应用 |

该权限属于受限权限，需经审批后应用才可获得，申请方式参见[申请受限权限](declare-permissions-in-acl.md)。审批需同时满足以下规则：

1. 应用主体为企业、教育机构或正规考试服务商，不支持个人账号申请。
2. 应用在应用市场的二级分类属于教育类。
3. 应用核心用途为高风险正式考试或测评类场景（如学业水平考试、职业认证、标准化测验），不用于普通课堂练习、打卡、签到、刷题、录屏监控等场景，申请时需提供考试场景的页面截图。
4. 应用无历史违规，开发者账号无严重审核违规、欺诈、作弊记录。

其他约束如下：

* 开始评估需经用户在确认弹窗中确认，用户取消则评估不会开始。
* 同一设备同一时间仅允许存在一个进行中的评估，已处于评估状态时再次调用begin接口会报错。
* 仅开启评估的应用可结束该评估，调用end接口结束其他应用开启的评估会报错。

评估配置的规格约束如下：

* duration最大值为8小时（28800000毫秒），超出该值的取值按上限生效；取值为0时按默认时长8小时处理。
* allowedApps最多支持配置20个应用包名，且所有包名拼接后的总长度不超过2048字符。

## 开发流程

1. 在配置文件中申请权限ohos.permission.ASSESSMENT\_CONFIGURATION。
2. 导入评估管理模块。
3. 配置评估参数，调用begin接口开始评估，并注册评估过程回调。
4. 根据业务需要，调用isActive、getConfiguration接口查询评估状态和配置。
5. 评估完成后，调用end接口结束评估。

## 接口说明

评估管理关键接口如下表所示，具体API说明详见[@ohos.customization.assessment (评估管理)](../harmonyos-references/js-apis-customization-assessment.md)。

**表2** 评估管理接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| [begin(context, config, callback)](../harmonyos-references/js-apis-customization-assessment.md#assessmentbegin): void | 开始评估，弹出确认弹窗，用户确认后进入评估模式。 |
| [end(context)](../harmonyos-references/js-apis-customization-assessment.md#assessmentend): void | 结束评估，解除评估模式下的系统能力限制。 |
| [isActive()](../harmonyos-references/js-apis-customization-assessment.md#assessmentisactive): boolean | 查询当前是否处于评估状态。 |
| [getConfiguration()](../harmonyos-references/js-apis-customization-assessment.md#assessmentgetconfiguration): AssessmentConfig | 获取当前评估配置。 |

## 开发步骤

### 申请权限

在模块的module.json5文件中，申请权限[ohos.permission.ASSESSMENT\_CONFIGURATION](restricted-permissions.md#ohospermissionassessment_configuration)。该权限为system\_basic级别的系统授权（system\_grant）受限权限，需先按[申请受限权限](declare-permissions-in-acl.md)完成申请，声明后在应用安装时自动授予。声明权限的详细说明参见[声明权限](declare-permissions.md)。示例如下：

```json5
{
  "module": {
    // ...
    "requestPermissions": [
      // ...
      {
        "name": "ohos.permission.ASSESSMENT_CONFIGURATION"
      }
    ]
  }
}
```

### 导入评估管理模块

导入assessment模块后即可调用评估管理接口。

```typescript
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
```

### 开始评估

配置评估参数，调用begin接口开始评估，并通过IAssessmentCallback注册评估过程回调。

调用begin后，系统会弹出确认弹窗，需用户确认后方可开始评估，评估结果及评估过程中的中断、结束事件均通过回调通知。context的获取方式参见[Context的获取方式](application-context-stage.md#context的获取方式)。示例代码如下：

```typescript
import { common } from '@kit.AbilityKit';
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

// 评估过程回调
const assessmentCallback: assessment.IAssessmentCallback = {
  onBegin: (error: assessment.AssessmentError): void => {
    // AssessmentError.message为可选字段，取值前先做空值兜底
    const message: string = error.message ?? '';
    if (error.code === assessment.AssessmentErrorCode.OK) {
      hilog.info(DOMAIN, TAG, '%{public}s', `onBegin, assessment began successfully, message: ${message}`);
    } else {
      hilog.error(DOMAIN, TAG, '%{public}s',
        `onBegin, assessment begin failed, code: ${error.code}, message: ${message}`);
    }
  },
  onInterrupted: (info: assessment.AssessmentInterruptInfo): void => {
    // 评估被中断，业务侧可根据中断原因码做相应处理，如保存答题记录
    hilog.warn(DOMAIN, TAG, '%{public}s', `onInterrupted, code: ${info.code}, message: ${info.message}`);
  },
  onEnd: (): void => {
    hilog.info(DOMAIN, TAG, '%{public}s', 'onEnd, assessment ended');
  }
};

@Entry
@Component
struct Index {
  build() {
    Button($r('app.string.begin_button'))
      .onClick(() => {
        this.beginAssessment();
      })
  }

  private beginAssessment(): void {
    // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
    const host: common.Context | undefined = this.getUIContext().getHostContext();
    if (host === undefined) {
      hilog.error(DOMAIN, TAG, '%{public}s', 'begin failed, the host context is undefined');
      return;
    }
    const context: common.UIAbilityContext = host as common.UIAbilityContext;
    // 评估配置：最大时长1小时（3600000毫秒）；
    // 评估期间允许运行包名为com.samples.assessment的应用
    const config: assessment.AssessmentConfig = {
      duration: 3600000,
      allowedApps: ['com.samples.assessment']
    };
    try {
      assessment.begin(context, config, assessmentCallback);
      hilog.info(DOMAIN, TAG, '%{public}s', 'begin called, waiting for user confirmation');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s', `begin failed, code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

### 查询评估状态与配置

在评估过程中，调用isActive接口查询当前评估状态，调用getConfiguration接口获取当前评估配置。示例代码如下：

```typescript
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

try {
  const active: boolean = assessment.isActive();
  hilog.info(DOMAIN, TAG, '%{public}s', `isActive result: ${active}`);
  if (active) {
    const config: assessment.AssessmentConfig = assessment.getConfiguration();
    hilog.info(DOMAIN, TAG, '%{public}s',
      `getConfiguration result, duration: ${config.duration}, allowedApps: ${config.allowedApps.join(',')}`);
  }
} catch (error) {
  const err: BusinessError = error as BusinessError;
  hilog.error(DOMAIN, TAG, '%{public}s', `query failed, code: ${err.code}, message: ${err.message}`);
}
```

### 结束评估

评估完成后，由开启评估的应用调用end接口结束评估，系统解除评估模式下对系统能力的限制，并触发onEnd回调。示例代码如下：

```typescript
import { common } from '@kit.AbilityKit';
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

@Entry
@Component
struct Index {
  build() {
    Button($r('app.string.exam_submit'))
      .onClick(() => {
        this.endAssessment();
      })
  }

  // 结束由当前应用开启的评估，仅开启评估的应用可以结束该评估
  private endAssessment(): void {
    // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
    const host: common.Context | undefined = this.getUIContext().getHostContext();
    if (host === undefined) {
      hilog.error(DOMAIN, TAG, '%{public}s', 'end failed, the host context is undefined');
      return;
    }
    const context: common.UIAbilityContext = host as common.UIAbilityContext;
    try {
      assessment.end(context);
      hilog.info(DOMAIN, TAG, '%{public}s', 'end called');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s', `end failed, code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## 应用侧加固建议

评估模式由系统统一管控部分系统能力，但应用窗口形态、应用窗口的截屏录屏、剪贴板与输入法面板不在系统管控范围内，需由应用自行加固，防止评估内容外泄或借助外部输入作弊。建议在进入评估页面时统一启用，退出评估页面时恢复。

**表3** 应用侧加固措施

| 加固措施 | 接口 | 作用 |
| --- | --- | --- |
| 窗口沉浸式 | setWindowLayoutFullScreen | 内容延伸至状态栏与导航栏区域，减少评估页面外的系统入口暴露 |
| PC全屏 | maximize | 主窗口进入全屏，且鼠标悬停热区不显示窗口标题栏与dock栏，减少借系统入口切出评估页面的可能 |
| 隐私模式 | setWindowPrivacyMode | 窗口无法被截屏与录屏，退至后台时在多任务视图中显示为隐私遮罩 |
| 清空剪贴板 | clearData | 清除残留的剪贴板数据，避免借助剪贴板传入答案 |
| 简单键盘模式 | setSimpleKeyboardEnabled | 输入法面板仅保留基础按键，收起候选栏与扩展功能入口，AI帮写功能随之不可用 |

PC全屏通过maximize接口实现，需传入MaximizePresentation.ENTER\_IMMERSIVE\_DISABLE\_TITLE\_AND\_DOCK\_HOVER（从API version 14开始支持），使主窗口进入全屏且鼠标悬停热区不显示窗口标题栏与dock栏；退出评估页面时调用recover接口，将窗口还原为进入全屏前的大小与位置。该接口仅在支持并处于[自由窗口](window-terminology.md#freeform-window自由窗口)状态的设备上可正常调用，在支持但不处于自由窗口状态的设备及不支持自由窗口状态的设备上调用不生效也不报错，因此无需区分设备类型即可直接调用。

简单键盘模式通过inputMethod.setSimpleKeyboardEnabled接口开启，开启后输入法面板仅保留基础按键，候选栏与扩展功能入口被收起，AI帮写功能随之不可用，避免评估期间借助AI帮写生成答案。该设置对原生文本框组件在下次点击获焦时生效，对自绘控件在下次调用attach绑定输入法时生效，因此建议在进入评估页面后、考生开始作答前完成设置，并在退出评估页面时传入false恢复。

隐私模式需申请权限ohos.permission.PRIVACY\_WINDOW，该权限为normal级别的系统授权（system\_grant）权限，声明方式与[申请权限](assessment-guide.md#申请权限)一致。窗口类接口需先获取当前窗口，加固与恢复的关键实现如下：

```typescript
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { inputMethod } from '@kit.IMEKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

export class ExamHardeningUtil {
  // 进入评估页面时启用全部加固措施
  public static async applyHardening(context: common.UIAbilityContext): Promise<void> {
    await ExamHardeningUtil.setWindowHardening(context, true);
    ExamHardeningUtil.setSimpleKeyboard(true);
    await ExamHardeningUtil.clearPasteboard();
  }

  // 退出评估页面时恢复窗口形态与输入法，并再次清空剪贴板
  public static async releaseHardening(context: common.UIAbilityContext): Promise<void> {
    await ExamHardeningUtil.setWindowHardening(context, false);
    ExamHardeningUtil.setSimpleKeyboard(false);
    await ExamHardeningUtil.clearPasteboard();
  }

  // 两项窗口措施分别捕获异常，单项失败不影响另一项生效
  private static async setWindowHardening(context: common.UIAbilityContext, enable: boolean): Promise<void> {
    let currentWindow: window.Window | undefined = undefined;
    try {
      currentWindow = await window.getLastWindow(context);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s', `getLastWindow failed, code: ${err.code}, message: ${err.message}`);
    }
    if (currentWindow === undefined) {
      return;
    }
    try {
      await currentWindow.setWindowLayoutFullScreen(enable);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s',
        `setWindowLayoutFullScreen failed, code: ${err.code}, message: ${err.message}`);
    }
    try {
      await currentWindow.setWindowPrivacyMode(enable);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s',
        `setWindowPrivacyMode failed, code: ${err.code}, message: ${err.message}`);
    }
  }

  // 输入法面板切换为简单键盘，仅保留基础按键，收起候选栏与扩展功能入口
  private static setSimpleKeyboard(enable: boolean): void {
    try {
      inputMethod.setSimpleKeyboardEnabled(enable);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s',
        `setSimpleKeyboardEnabled failed, code: ${err.code}, message: ${err.message}`);
    }
  }

  // 清空剪贴板，避免残留数据被粘贴进评估页面
  private static async clearPasteboard(): Promise<void> {
    try {
      await pasteboard.getSystemPasteboard().clearData();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s', `clearData failed, code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

在评估页面的生命周期中调用加固与恢复，示例代码如下：

```typescript
aboutToAppear(): void {
  this.applyHardening();
}

aboutToDisappear(): void {
  this.releaseHardening();
}

private applyHardening(): void {
  const context: common.UIAbilityContext | undefined = this.getAbilityContext();
  if (context === undefined) {
    return;
  }
  ExamHardeningUtil.applyHardening(context).catch((error: BusinessError) => {
    hilog.error(DOMAIN, TAG, '%{public}s', `applyHardening failed, code: ${error.code}, message: ${error.message}`);
  });
}
```

完整实现参见[相关实例](assessment-guide.md#相关实例)。

## 调测验证

1. 调用begin接口后，设备弹出评估确认弹窗；用户确认后进入评估模式，系统能力受到限制，onBegin回调返回code为0（OK）。
2. 调用isActive接口，返回true，表示当前处于评估状态。
3. 尝试打开allowedApps白名单之外的应用，验证其无法在评估期间运行。
4. 调用end接口结束评估，isActive接口返回false，系统能力限制解除，onEnd回调被触发。

## 常见问题

### 如何设计allowedApps白名单以保证评估期间业务可用

allowedApps用于指定评估期间允许运行的应用包名，白名单之外的应用在评估期间无法运行。设计白名单时建议遵循以下原则：

* 将评估过程中必须使用的应用加入白名单，如答题应用依赖的输入法、无障碍辅助应用，以及听力评估所需的音频播放应用。
* 必须将地震预警类应用加入白名单。评估期间白名单之外应用的启动与页面弹出会被系统拦截，若地震预警类应用未加入allowedApps，评估期间收到地震预警时预警页面无法弹出，存在安全风险。该类应用的包名因设备预置情况而异，请向设备厂商确认后填写。
* 必须将发起评估的应用自身包名加入allowedApps。调用begin时该应用处于前台，若不在白名单内，开始评估前的环境校验不通过，评估无法开始。

白名单的具体规格限制参见[约束与限制](assessment-guide.md#约束与限制)，配置方式参见[开始评估](assessment-guide.md#开始评估)。

### duration取值为0时评估如何退出

duration为0时系统按默认时长处理，该默认时长与duration上限一致，达到该时长后评估因超时被中断并触发onInterrupted回调，中断原因码为TIMEOUT。具体取值参见[约束与限制](assessment-guide.md#约束与限制)。

评估期间也可随时由开启评估的应用调用end接口主动结束评估，系统解除对系统能力的限制并触发onEnd回调。为避免评估长时间占用设备，建议按业务实际作答时长设置duration，具体操作参见[结束评估](assessment-guide.md#结束评估)。

### 评估被中断后应用需要做哪些处理

onEnd与onInterrupted的触发时机不同：onEnd在应用调用end接口正常结束评估后触发；onInterrupted在评估被系统主动中断时触发，携带中断原因码与描述信息。

评估被中断时系统已自动解除对系统能力的限制，应用无需再调用end接口，建议完成以下处理：

* 在onInterrupted回调中保存答题记录、剩余时长等业务数据，避免数据丢失。
* 根据中断原因码区分处理，如超时退出时提交已作答内容，用户取消时提示用户评估已结束。
* 中断后如需重新评估，重新调用begin接口发起，并由用户在确认弹窗中确认。

### 为什么调用begin后没有立即进入评估模式

begin接口调用成功后不会立即进入评估模式。系统会先弹出确认弹窗，需用户在弹窗中确认后设备才进入评估模式，用户取消则评估不会开始。

begin接口返回仅表示请求已提交，评估是否真正开始需通过onBegin回调判断：回调中code为OK表示评估已开始，为USER\_CANCEL表示用户已取消。建议在onBegin回调中再更新界面状态并启动业务计时，配置方式参见[开始评估](assessment-guide.md#开始评估)。
