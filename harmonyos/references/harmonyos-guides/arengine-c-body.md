---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-body
title: 人体跟踪与骨骼关键点识别（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人体骨骼点识别与跟踪 > 人体跟踪与骨骼关键点识别（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:5cc4a6c6a551f9f6224032f603306632c8be9c519f5c84c85f660a645263587d
---

## 约束与限制

从6.1.0(23)开始，人体跟踪与骨骼关键点识别能力支持部分Phone、部分Tablet设备、TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持人体骨骼点识别与跟踪特性（[ARENGINE\_FEATURE\_TYPE\_BODY](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

人体跟踪与骨骼关键点识别主要依赖ARBody，以下接口为AR Engine人体跟踪与骨骼关键点识别相关接口，详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARBody\_GetSkeletonConfidence](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconfidence) | 获取人体对象每个骨骼点检测的置信度。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonConnection](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconnection) | 获取人体对象骨骼点之间的链接关系数据。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonConnectionSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconnectionsize) | 获取人体对象骨骼点之间的链接关系总数。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonTypes](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletontypes) | 获取识别出的人体对象骨骼点类型。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonPointCount](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointcount) | 获取人体对象的骨骼点个数。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonPointData2D](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointdata2d) | 当运行2D骨骼跟踪算法时，返回人体骨骼点的坐标数据。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonPointIsValid](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointisvalid) | 获取人体对象骨骼点的坐标是否有效，返回有效性数组。 |
| [HMS\_AREngine\_ARBody\_GetBodyTrackId](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getbodytrackid) | 获取指定人体对象的标识。 |
| [HMS\_AREngine\_ARBody\_GetBodyTimeStamp](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getbodytimestamp) | 获取人体对象的检测时间点，表示触发检测人体对象距离启动相机的时间间隔，单位为ns。 |
| [HMS\_AREngine\_ARConfig\_SetBodyDetectedNum](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setbodydetectednum) | 设置追踪人数。 |

## 开发步骤

### 创建UI界面

创建一个UI界面，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示相机预览画面，定时触发每一帧绘制。

```typescript
import { arEngine, arViewController } from '@kit.AREngine';
import { display } from '@kit.ArkUI';
import { systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo, { Landmark } from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARBodyBuilder() {
  ARBody();
}

const DEFAULT_WIDTH: number = 1440;
const DEFAULT_HEIGHT: number = 1080;
const DEFAULT_ROTATION: number = 0;

interface ARBodyBoneLine {
  start: arEngine.ARBodyLandmarkType,
  end: arEngine.ARBodyLandmarkType,
}

@Entry
@ComponentV2
struct ARBody {
  @Local context: Context = this.getUIContext().getHostContext() as Context;
  @Local displayWidth: number = DEFAULT_WIDTH;
  @Local displayHeight: number = DEFAULT_HEIGHT;
  @Local rotation: number = DEFAULT_ROTATION;
  @Local arContext?: arViewController.ARViewContext = undefined;
  @Local landmarks: Landmark[][] = [];
  @Local boneLines: ARBodyBoneLine[][] = [];
  private interval: number = -1;
  private idStr: string = systemDateTime.getTime(false).toString() + 'ARBody';
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  private isUpdate: boolean = false;
  private DEFAULT_CONVERT_FACTOR: number = 4 / 3;
  private boneLineNum: number = 26;
  private landMarkNum: number = 20;
  private uiContext: UIContext = this.getUIContext();
  private maxDetectedBodyNum: number = 1;

  @Builder
  drawBodyPerception() {
    Shape() {
      ForEach(this.landmarks, (landmarks: Landmark[], index: number) => {
        this.drawBodyLandmarks(index);
        this.drawBodyBones(index);
      })
    }
    .width(this.uiContext.px2vp(this.displayWidth))
    .height(this.uiContext.px2vp(this.displayHeight))
  }

  @Builder
  drawBodyLandmarks(bodyIndex: number) {
    ForEach(this.landmarks[bodyIndex], (landmark: Landmark) => {
      Circle({ width: 4, height: 4 })
        .position({
          x: this.uiContext.px2vp(landmark.x),
          y: this.uiContext.px2vp(landmark.y)
        })
        .fill(Color.White)
    })
  }

  @Builder
  drawBodyBones(bodyIndex: number) {
    if (this.boneLines.length > bodyIndex && this.landmarks[bodyIndex].length > 0) {
      ForEach(this.boneLines[bodyIndex], (bone: ARBodyBoneLine) => {
        this.drawBodyBoneLine(bone.start, bone.end, this.getLineColorByLineEnd(bone.end), bodyIndex);
      })
    }
  }

  @Builder
  drawBodyBoneLine(start: arEngine.ARBodyLandmarkType, end: arEngine.ARBodyLandmarkType, color: Color, index: number) {
    Line()
      .startPoint([this.uiContext.px2vp(this.landmarks[index][start - 1]?.x),
        this.uiContext.px2vp(this.landmarks[index][start - 1]?.y)])
      .endPoint([this.uiContext.px2vp(this.landmarks[index][end - 1]?.x),
        this.uiContext.px2vp(this.landmarks[index][end - 1]?.y)])
      .stroke(color)
      .strokeWidth(3)
  }

  build() {
    NavDestination() {
      RelativeContainer() {
        Stack() {
          XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
            .width(this.uiContext.px2vp(this.displayWidth))
            .height(this.uiContext.px2vp(this.displayHeight))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
          this.drawBodyPerception()
        }
        .width('100%')
        .height('100%')
      }
    }
    .onAppear(async () => {
      try {
        this.displayWidth = display.getDefaultDisplaySync().availableWidth;
        this.displayHeight = display.getDefaultDisplaySync().availableHeight;
        this.rotation = display.getDefaultDisplaySync().rotation;
      } catch (e) {
        logger.error(`display.getDefaultDisplaySync failed error.message:${e?.message}, error.code:${e?.code}`);
      }
      this.runArBodyCheck();
    })
    .onWillDisappear(() => {
      clearInterval(this.interval);
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.idStr);
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
    .width('100%')
    .height('100%')
  }

  private processLandMarks(res: Landmark[]): Landmark[][] {
    let preWidth = this.displayWidth;
    let preHeight = this.displayHeight;
    try {
      if (display.getDefaultDisplaySync().availableWidth < display.getDefaultDisplaySync().availableHeight) {
        this.displayWidth = display.getDefaultDisplaySync().availableWidth;
        this.displayHeight = this.displayWidth * this.DEFAULT_CONVERT_FACTOR;
      } else {
        this.displayHeight = display.getDefaultDisplaySync().availableHeight;
        this.displayWidth = this.displayHeight * this.DEFAULT_CONVERT_FACTOR;
      }
    } catch (e) {
      logger.error(`display.getDefaultDisplaySync failed error.message:${e?.message}, error.code:${e?.code}`);
      this.displayWidth = preWidth;
      this.displayHeight = preHeight;
    }

    let ret: Landmark[][] = [];
    let num = 0;
    for (let i = 0; i < Math.min(this.maxDetectedBodyNum, res.length / this.landMarkNum); i++) {
      ret.push([]);
      for (let j = 0; j < this.landMarkNum; j++) {
        ret[i].push({
          x: res[num].x * this.displayWidth,
          y: res[num].y * this.displayHeight
        })
        num++;
      }
    }
    return ret;
  }

  private getBoneLines(res: number[]): ARBodyBoneLine[][] {
    let ret: ARBodyBoneLine[][] = [];
    let num = 0;
    for (let i = 0; i < Math.min(this.maxDetectedBodyNum, res.length / this.boneLineNum); ++i) {
      ret.push([]);
      for (let j = 0; j < this.boneLineNum; j += 2) {
        ret[i].push({
          start: res[num],
          end: res[num + 1]
        });
        num += 2;
      }
    }
    return ret;
  }

  private runArBodyCheck(): void {
    arEngineDemo.init(this.resMgr);
    let config: Int32Array = new Int32Array([1, this.rotation]);
    arEngineDemo.start(this.idStr, config);
    this.interval = setInterval(() => {
      if (!this.isUpdate) {
        return;
      }
      arEngineDemo.update(this.idStr);
      this.landmarks = this.processLandMarks(arEngineDemo.getLandmark(this.idStr));
      const boneLines: number[] = arEngineDemo.getBoneLine(this.idStr).skeletonConnections;
      this.boneLines = this.getBoneLines(boneLines);
    }, 33);
  }

  private getLineColorByLineEnd(lineEnd: arEngine.ARBodyLandmarkType): Color {
    switch (lineEnd) {
      case arEngine.ARBodyLandmarkType.LEFT_ELBOW:
      case arEngine.ARBodyLandmarkType.LEFT_WRIST:
      case arEngine.ARBodyLandmarkType.LEFT_KNEE:
      case arEngine.ARBodyLandmarkType.LEFT_ANKLE:
        return Color.Green;
      case arEngine.ARBodyLandmarkType.RIGHT_ELBOW:
      case arEngine.ARBodyLandmarkType.RIGHT_WRIST:
      case arEngine.ARBodyLandmarkType.RIGHT_KNEE:
      case arEngine.ARBodyLandmarkType.RIGHT_ANKLE:
        return Color.Blue;
      case arEngine.ARBodyLandmarkType.RIGHT_SHOULDER:
      case arEngine.ARBodyLandmarkType.RIGHT_HIP:
      case arEngine.ARBodyLandmarkType.LEFT_SHOULDER:
      case arEngine.ARBodyLandmarkType.LEFT_HIP:
      default:
        return Color.Orange;
    }
  }
}
```

### 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

### 创建AR会话

创建AR会话，配置人体跟踪模式。使用人体跟踪与骨骼关键点识别能力时请使用[HMS\_AREngine\_ARSession\_Create\_Human\_Perception](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create_human_perception)创建AR会话。

```
int32_t maxBodyDetectedNum = 1;
uint32_t previewWidth = 1440;
uint32_t previewHeight = 1080;
CHECK(HMS_AREngine_ARSession_Create_Human_Perception(nullptr, nullptr, &mArSession));
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARConfig_SetARType(mArSession, arConfig, ARENGINE_TYPE_BODY));
CHECK(HMS_AREngine_ARConfig_SetBodyDetectedNum(mArSession, arConfig, maxBodyDetectedNum));
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);
```

### 创建可跟踪对象列表

创建一个可跟踪对象列表targetList，用于存放AR Engine运行过程中检测到的所有可跟踪对象。

```
AREngine_ARTrackableList *arTrackableList = nullptr;
CHECK(HMS_AREngine_ARTrackableList_Create(mArSession, &arTrackableList));
```

### 获取人体追踪对象

调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有人体追踪对象，并将结果存放在targetList中。

```
CHECK(HMS_AREngine_ARSession_GetAllTrackables(mArSession, ARENGINE_TRACKABLE_BODY, arTrackableList));
```

### 获取可跟踪对象数量

调用[HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)函数获取当前可跟踪对象数量，结果存放在targetSize中。

```
int32_t trackableListSize = 0;
CHECK(HMS_AREngine_ARTrackableList_GetSize(mArSession, arTrackableList, &trackableListSize));
```

### 获取骨骼点相关信息

创建一个骨骼点信息列表skeletonValid2Ds，用于存放骨骼点信息数据。

```
for (int i = 0; i < trackableListSize; i++) {
    AREngine_ARTrackable *arTrackable = nullptr;
    CHECK(HMS_AREngine_ARTrackableList_AcquireItem(mArSession, arTrackableList, i, &arTrackable));
    AREngine_ARBody *arBody = reinterpret_cast<AREngine_ARBody *>(arTrackable);
    int32_t pointCnt = 0;
    int32_t pointSize = 2;
    CHECK(HMS_AREngine_ARBody_GetSkeletonPointCount(mArSession, arBody, &pointCnt));
    const float *skeletonPoints2D = nullptr;
    CHECK(HMS_AREngine_ARBody_GetSkeletonPointData2D(mArSession, arBody, &skeletonPoints2D));
    std::vector<float> skeletonPoints2Ds;
    for (int j = 0; j < pointCnt * pointSize; j++) {
        skeletonPoints2Ds.push_back(skeletonPoints2D[j]);
    }
    coord.push_back(skeletonPoints2Ds);
    const float *skeletonConfidences = nullptr;
    CHECK(HMS_AREngine_ARBody_GetSkeletonConfidence(mArSession, arBody, &skeletonConfidences));
    std::vector<float> skeletonConfidence2Ds;
    for (int j = 0; j < pointCnt; j++) {
        skeletonConfidence2Ds.push_back(skeletonConfidences[j]);
    }
    confidence.push_back(skeletonConfidence2Ds);
    const int32_t *isValids = nullptr;
    CHECK(HMS_AREngine_ARBody_GetSkeletonPointIsValid(mArSession, arBody, &isValids));
    std::vector<int32_t> skeletonValid2Ds;
    for (int j = 0; j < pointCnt; j++) {
        skeletonValid2Ds.push_back(isValids[j]);
    }
    valid.push_back(skeletonValid2Ds);
    int32_t outBodyTrackId = 0;
    CHECK(HMS_AREngine_ARBody_GetBodyTrackId(mArSession, arBody, &outBodyTrackId));
    int64_t timeStampNanoSec = 0;
    CHECK(HMS_AREngine_ARBody_GetBodyTimeStamp(mArSession, arBody, &timeStampNanoSec));
    LOGI("ArBodyApp bodyTrackId = %{public}d, timeStampNanoSec = %{public}ld", outBodyTrackId, timeStampNanoSec);
}
```

### 获取骨骼点之间的连接关系数据

创建一个骨骼点连接关系数据列表connections，用于存放骨骼点之间相连关系数据。

```
for (int i = 0; i < trackableListSize; i++) {
    AREngine_ARTrackable *arTrackable = nullptr;
    CHECK(HMS_AREngine_ARTrackableList_AcquireItem(mArSession, arTrackableList, i, &arTrackable));
    AREngine_ARBody *arBody = reinterpret_cast<AREngine_ARBody *>(arTrackable);
    int32_t connectionSize = 0;
    int32_t connectionPointSize = 2;
    CHECK(HMS_AREngine_ARBody_GetSkeletonConnectionSize(mArSession, arBody, &connectionSize));
    const AREngine_ARBodySkeletonType *skeletonConnections2D = nullptr;
    CHECK(HMS_AREngine_ARBody_GetSkeletonConnection(mArSession, arBody, &skeletonConnections2D));
    const AREngine_ARBodySkeletonType *skeletonTypes = nullptr;
    CHECK(HMS_AREngine_ARBody_GetSkeletonTypes(mArSession, arBody, &skeletonTypes));
    std::vector<int32_t> skeletonValid2Ds;
    for (int j = 0; j < connectionSize * connectionPointSize; j++) {
        skeletonValid2Ds.push_back(skeletonConnections2D[j]);
    }
    std::vector<int32_t> skeletonTypesVec;
    for (int j = 0; j < sizeof(std::underlying_type_t<AREngine_ARBodySkeletonType>); j++) {
        skeletonTypesVec.push_back(skeletonConnections2D[j]);
    }
    connections.push_back(skeletonValid2Ds);
    types.push_back(skeletonTypesVec);
}
```

### 销毁可跟踪对象列表

可跟踪对象列表targetList不再使用后需销毁：

```
HMS_AREngine_ARTrackableList_Destroy(arTrackableList);
```
