---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-waterflow
title: 使用瀑布流
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建布局 > 使用瀑布流
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3bab3bf6fe1a3d09b7c6169c462953d072186b58b49e49820475a423e79088b0
---

ArkUI开发框架在NDK接口提供了瀑布流容器组件，通过瀑布流自身的排列规则，将不同大小的"项目"自上而下如瀑布般紧密布局。

## 接入ArkTS页面

为了使用NDK接口构建UI界面，参考[接入ArkTS页面章节](ndk-access-the-arkts-page.md)，在ArkTS页面上创建用于Native页面挂载的占位组件，并实现ArkTS侧的NativeNode模块接口。

## 使用懒加载

### NodeAdapter介绍

NDK中提供了NodeAdapter对象替代ArkTS侧的[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)功能，用于按需生成子组件。详情请参阅[NodeAdapter介绍](ndk-loading-long-list.md#nodeadapter介绍)。

### 实现懒加载适配器

使用FlowItemAdapter类管理懒加载适配器。在类的构造函数中创建NodeAdapter对象，并给NodeAdapter对象设置事件监听器，在类的析构函数中，销毁NodeAdapter对象。

```
1. // FlowItemAdapter.h
2. // 懒加载功能代码。

4. #ifndef MYAPPLICATION_FLOWITEMADAPTER_H
5. #define MYAPPLICATION_FLOWITEMADAPTER_H

7. #include <arkui/native_node.h>
8. #include <stack>
9. #include <string>
10. #include <unordered_set>
11. #include <arkui/native_interface.h>

13. namespace NativeModule {
14. const int NUM = 100;
15. class FlowItemAdapter {
16. public:
17. FlowItemAdapter()
18. {
19. // 初始化函数指针结构体
20. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, nodeApi_);
21. // 创建Adapter对象
22. adapter_ = OH_ArkUI_NodeAdapter_Create();

24. // 初始化懒加载数据。
25. for (int32_t i = 0; i < NUM; i++) {
26. data_.emplace_back(std::to_string(i));
27. }
28. // 设置懒加载数据。
29. OH_ArkUI_NodeAdapter_SetTotalNodeCount(adapter_, data_.size());
30. // 设置事件监听器。
31. OH_ArkUI_NodeAdapter_RegisterEventReceiver(adapter_, this, OnStaticAdapterEvent);
32. }

34. ~FlowItemAdapter()
35. {
36. // 释放创建的组件。
37. while (!cachedItems_.empty()) {
38. cachedItems_.pop();
39. }
40. // 释放Adapter相关资源。
41. OH_ArkUI_NodeAdapter_UnregisterEventReceiver(adapter_);
42. OH_ArkUI_NodeAdapter_Dispose(adapter_);
43. }

45. ArkUI_NodeAdapterHandle GetAdapter() const { return adapter_; }

47. void RemoveItem(int32_t index)
48. {
49. // 删除第index个数据。
50. data_.erase(data_.begin() + index);
51. // 如果index会导致可视区域元素发生可见性变化，则会回调NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER事件删除元素，
52. // 根据是否有新增元素回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID和NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件。
53. OH_ArkUI_NodeAdapter_RemoveItem(adapter_, index, 1);
54. // 更新新的数量。
55. OH_ArkUI_NodeAdapter_SetTotalNodeCount(adapter_, data_.size());
56. }

58. void InsertItem(int32_t index, const std::string &value)
59. {
60. data_.insert(data_.begin() + index, value);
61. // 如果index会导致可视区域元素发生可见性变化，则会回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID和NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件，
62. // 根据是否有删除元素回调NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER事件。
63. OH_ArkUI_NodeAdapter_InsertItem(adapter_, index, 1);
64. // 更新新的数量。
65. OH_ArkUI_NodeAdapter_SetTotalNodeCount(adapter_, data_.size());
66. }

68. void MoveItem(int32_t oldIndex, int32_t newIndex)
69. {
70. auto temp = data_[oldIndex];
71. data_.insert(data_.begin() + newIndex, temp);
72. data_.erase(data_.begin() + oldIndex);
73. // 移到位置如果未发生可视区域内元素的可见性变化，则不回调事件，反之根据新增和删除场景回调对应的事件。
74. OH_ArkUI_NodeAdapter_MoveItem(adapter_, oldIndex, newIndex);
75. }

77. void ReloadItem(int32_t index, const std::string &value)
78. {
79. data_[index] = value;
80. // 如果index位于可视区域内，先回调NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER删除老元素，
81. // 再回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID和NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件。
82. OH_ArkUI_NodeAdapter_ReloadItem(adapter_, index, 1);
83. }

85. void ReloadAllItem()
86. {
87. std::reverse(data_.begin(), data_.end());
88. // 全部重新加载场景下，会回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID接口获取新的组件ID，
89. // 根据新的组件ID进行对比，ID不发生变化的进行复用，
90. // 针对新增ID的元素，调用NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件创建新的组件，
91. // 然后判断老数据中遗留的未使用ID，调用NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER删除老元素。
92. OH_ArkUI_NodeAdapter_ReloadAllItems(adapter_);
93. }

95. private:
96. static void OnStaticAdapterEvent(ArkUI_NodeAdapterEvent *event)
97. {
98. // 获取实例对象，回调实例事件。
99. auto itemAdapter = reinterpret_cast<FlowItemAdapter *>(OH_ArkUI_NodeAdapterEvent_GetUserData(event));
100. itemAdapter->OnAdapterEvent(event);
101. }

103. void OnAdapterEvent(ArkUI_NodeAdapterEvent *event)
104. {
105. auto type = OH_ArkUI_NodeAdapterEvent_GetType(event);
106. switch (type) {
107. case NODE_ADAPTER_EVENT_ON_GET_NODE_ID:
108. OnGetChildId(event);
109. break;
110. case NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER:
111. OnCreateNewChild(event);
112. break;
113. case NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER:
114. OnDisposeChild(event);
115. break;
116. default:
117. break;
118. }
119. }

121. void OnGetChildId(ArkUI_NodeAdapterEvent *event)
122. {
123. auto index = OH_ArkUI_NodeAdapterEvent_GetItemIndex(event);
124. // 设置生成组件的唯一标识符。
125. auto hash = std::hash<std::string>();
126. OH_ArkUI_NodeAdapterEvent_SetNodeId(event, hash(data_[index]));
127. }

129. void OnCreateNewChild(ArkUI_NodeAdapterEvent *event)
130. {
131. auto index = OH_ArkUI_NodeAdapterEvent_GetItemIndex(event);
132. ArkUI_NodeHandle flowItem = nullptr;
133. if (!cachedItems_.empty()) {
134. // 复用缓存
135. flowItem = cachedItems_.top();
136. cachedItems_.pop();
137. // 更新数据
138. auto *text = nodeApi_->getFirstChild(flowItem);
139. ArkUI_AttributeItem item{nullptr, 0, data_[index].c_str()};
140. nodeApi_->setAttribute(text, NODE_TEXT_CONTENT, &item);
141. } else {
142. // 重新创建。
143. auto *text = nodeApi_->createNode(ARKUI_NODE_TEXT);
144. ArkUI_AttributeItem item{nullptr, 0, data_[index].c_str()};
145. nodeApi_->setAttribute(text, NODE_TEXT_CONTENT, &item);
146. flowItem = nodeApi_->createNode(ARKUI_NODE_FLOW_ITEM);
147. ArkUI_NumberValue value[] = {100};
148. ArkUI_AttributeItem height{value, 1};
149. nodeApi_->setAttribute(flowItem, NODE_HEIGHT, &height);
150. value[0] = {1};
151. ArkUI_AttributeItem width{value, 1};
152. nodeApi_->setAttribute(flowItem, NODE_WIDTH_PERCENT, &width);
153. value[0] = {.u32 = 0xFFD3D3D3};
154. ArkUI_AttributeItem backgroundColor{value, 1};

156. nodeApi_->setAttribute(flowItem, NODE_BACKGROUND_COLOR, &backgroundColor);
157. nodeApi_->addChild(flowItem, text);
158. }
159. OH_ArkUI_NodeAdapterEvent_SetItem(event, flowItem);
160. }

162. void OnDisposeChild(ArkUI_NodeAdapterEvent *event)
163. {
164. auto *node = OH_ArkUI_NodeAdapterEvent_GetRemovedNode(event);
165. // 缓存节点
166. cachedItems_.emplace(node);
167. }

169. std::vector<std::string> data_;
170. ArkUI_NativeNodeAPI_1 *nodeApi_ = nullptr;
171. ArkUI_NodeAdapterHandle adapter_ = nullptr;

173. // 管理回收复用组件池。
174. std::stack<ArkUI_NodeHandle> cachedItems_;
175. };

177. } // namespace NativeModule

179. #endif // MYAPPLICATION_FLOWITEMADAPTER_H
```

[FlowItemAdapter.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKWaterFlowSample/entry/src/main/cpp/FlowItemAdapter.h#L15-L195)

## 创建分组

使用WaterflowSection类管理[WaterFlow](../harmonyos-references/ts-container-waterflow.md)中的分组，其中SectionOption用于描述一个分段的各项配置信息。在类的构造函数中创建[ArkUI\_WaterFlowSectionOption](../harmonyos-references/pi-arkui-nativemodule-arkui-waterflowsectionoption.md)对象，在析构函数中将其销毁。

```
1. // WaterflowSection.h

3. #ifndef MYAPPLICATION_WATERFLOWSECTION_H
4. #define MYAPPLICATION_WATERFLOWSECTION_H

6. #include <arkui/native_node.h>
7. #include <hilog/log.h>

9. namespace NativeModule {

11. struct SectionOption {
12. int32_t itemsCount = 0;
13. int32_t crossCount;
14. float columnsGap;
15. float rowsGap;
16. // {上外边距，右外边距，下外边距，左外边距}
17. ArkUI_Margin margin{0, 0, 0, 0};
18. float (*onGetItemMainSizeByIndex)(int32_t itemIndex);
19. void *userData;
20. };

22. class WaterflowSection {
23. public:
24. WaterflowSection() : sectionOptions_(OH_ArkUI_WaterFlowSectionOption_Create()){};

26. ~WaterflowSection()
27. {
28. OH_ArkUI_WaterFlowSectionOption_Dispose(sectionOptions_);
29. }

31. void SetSection(ArkUI_WaterFlowSectionOption *sectionOptions, int32_t index, SectionOption section)
32. {
33. OH_ArkUI_WaterFlowSectionOption_SetItemCount(sectionOptions, index, section.itemsCount);
34. OH_ArkUI_WaterFlowSectionOption_SetCrossCount(sectionOptions, index, section.crossCount);
35. OH_ArkUI_WaterFlowSectionOption_SetColumnGap(sectionOptions, index, section.columnsGap);
36. OH_ArkUI_WaterFlowSectionOption_SetRowGap(sectionOptions, index, section.rowsGap);
37. OH_ArkUI_WaterFlowSectionOption_SetMargin(sectionOptions, index, section.margin.top, section.margin.right,
38. section.margin.bottom, section.margin.left);
39. OH_ArkUI_WaterFlowSectionOption_RegisterGetItemMainSizeCallbackByIndex(sectionOptions, index,
40. section.onGetItemMainSizeByIndex);
41. }

43. ArkUI_WaterFlowSectionOption *GetSectionOptions() const
44. {
45. return sectionOptions_;
46. }

48. void PrintSectionOptions()
49. {
50. int32_t sectionCnt = OH_ArkUI_WaterFlowSectionOption_GetSize(sectionOptions_);
51. for (int32_t i = 0; i < sectionCnt; i++) {
52. ArkUI_Margin margin = OH_ArkUI_WaterFlowSectionOption_GetMargin(sectionOptions_, i);
53. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "CreateWaterflowExample",
54. "Section[%{public}d].margin:{%{public}f, %{public}f, %{public}f, %{public}f}", i, margin.top,
55. margin.right, margin.bottom, margin.left);
56. }
57. }

59. private:
60. ArkUI_WaterFlowSectionOption *sectionOptions_ = nullptr;
61. };
62. } // namespace NativeModule

64. #endif // MYAPPLICATION_WATERFLOWSECTION_H
```

[WaterflowSection.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKWaterFlowSample/entry/src/main/cpp/WaterflowSection.h#L15-L80)

## 创建瀑布流

使用ArkUIWaterflowNode类管理Waterflow。支持通过SetLazyAdapter为其设置一个FlowItemAdapter，通过SetSection为其设置分段。

```
1. // waterflow.h
2. #ifndef MYAPPLICATION_WATERFLOW_H
3. #define MYAPPLICATION_WATERFLOW_H

5. #include "FlowItemAdapter.h"
6. #include "WaterflowSection.h"
7. #include "ArkUINode.h"

9. namespace NativeModule {

11. class ArkUIWaterflowNode : public ArkUINode {
12. public:
13. ArkUIWaterflowNode()
14. : ArkUINode(CreateWaterflowNode()) {}

16. ~ArkUIWaterflowNode() override
17. {
18. // 先卸载 adapter
19. if (adapter_ && nativeModule_) {
20. nativeModule_->resetAttribute(handle_, NODE_WATER_FLOW_NODE_ADAPTER);
21. adapter_.reset();
22. }
23. // 销毁分段
24. section_.reset();
25. // 基类会自动 dispose handle_
26. }

28. void SetLazyAdapter(const std::shared_ptr<FlowItemAdapter> &adapter)
29. {
30. ArkUI_AttributeItem item{nullptr, 0, nullptr, adapter->GetAdapter()};
31. nativeModule_->setAttribute(handle_, NODE_WATER_FLOW_NODE_ADAPTER, &item);
32. adapter_ = adapter;
33. }

35. void SetSection(const std::shared_ptr<WaterflowSection> &section)
36. {
37. if (!section->GetSectionOptions()) {
38. return;
39. }
40. ArkUI_NumberValue start[] = {{.i32 = 0}};
41. ArkUI_AttributeItem optionsItem = {start, 1, nullptr, section->GetSectionOptions()};
42. nativeModule_->setAttribute(handle_, NODE_WATER_FLOW_SECTION_OPTION, &optionsItem);
43. section_ = section;
44. }

46. std::shared_ptr<WaterflowSection> GetWaterflowSection() { return section_; }

48. private:
49. static ArkUI_NodeHandle CreateWaterflowNode()
50. {
51. ArkUI_NativeNodeAPI_1* api = nullptr;
52. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, api);
53. if (!api) {
54. return nullptr;
55. }
56. return api->createNode(ARKUI_NODE_WATER_FLOW);
57. }

59. std::shared_ptr<WaterflowSection> section_ = nullptr;
60. std::shared_ptr<FlowItemAdapter> adapter_;
61. };

63. } // namespace NativeModule

65. #endif // MYAPPLICATION_WATERFLOW_H
```

[waterflow.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKWaterFlowSample/entry/src/main/cpp/waterflow.h#L15-L81)

## 使用瀑布流

创建一个ArkUIWaterflowNode类的实例，设置其宽高，并绑定NodeAdapter和分段。

```
1. // CreateWaterflowExample.h

3. #ifndef MYAPPLICATION_CREATEWATERFLOWEXAMPLE_H
4. #define MYAPPLICATION_CREATEWATERFLOWEXAMPLE_H
5. #include "waterflow.h"

7. namespace NativeModule {
8. const int UI_WIDTH = 400;
9. const int UI_HEIGHT = 600;
10. const int SECTION_COUNT = 10;
11. const int SECTION_2_ID = 2;

13. inline void SetupSections(std::shared_ptr<WaterflowSection> sections)
14. {
15. SectionOption MARGIN_GAP_SECTION_1 = {10, 2, 10, 10, {20, 30, 40, 50}, nullptr, nullptr};
16. SectionOption MARGIN_GAP_SECTION_2 = {10, 4, 10, 10, {20, 30, 40, 50}, nullptr, nullptr};
17. for (int i = 0; i < SECTION_COUNT; i++) {
18. sections->SetSection(sections->GetSectionOptions(), i,
19. i % SECTION_2_ID ? MARGIN_GAP_SECTION_1 : MARGIN_GAP_SECTION_2);
20. }
21. }

23. inline std::shared_ptr<ArkUIWaterflowNode> CreateWaterflowExample(napi_env env)
24. {
25. auto waterflow = std::make_shared<ArkUIWaterflowNode>();
26. waterflow->SetHeight(UI_HEIGHT);
27. waterflow->SetWidth(UI_WIDTH);
28. waterflow->SetLazyAdapter(std::make_shared<FlowItemAdapter>());
29. auto sections = std::make_shared<WaterflowSection>();
30. SetupSections(sections);
31. waterflow->SetSection(sections);
32. return waterflow;
33. }
34. } // namespace NativeModule

36. #endif // MYAPPLICATION_CREATEWATERFLOWEXAMPLE_H
```

[CreateWaterflowExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKWaterFlowSample/entry/src/main/cpp/CreateWaterflowExample.h#L15-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/CoonG5TgQlyFcOxIYFltmQ/zh-cn_image_0000002583478065.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234014Z&HW-CC-Expire=86400&HW-CC-Sign=4EBE6012B39FB37DDC2F003041C22BC498D630EB4F4792A95EA95D2065164D6E)
