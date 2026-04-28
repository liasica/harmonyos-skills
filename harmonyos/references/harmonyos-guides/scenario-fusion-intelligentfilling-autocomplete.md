---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-autocomplete
title: 自动补全地址表单所在地区
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 自动补全地址表单所在地区
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c6f6b08eaf606e76a05b8a4beab47a3455abbb8cc196f92586527d8e0a21de40
---

在填写地址表单场景时，当应用使用了所在地区的省市区选择器，需要开发者对表单中的地址字段进行开发。

说明

* 需要在module.json5文件中设置模糊位置权限：[ohos.permission.APPROXIMATELY\_LOCATION](permissions-for-all-user.md#ohospermissionapproximately_location)。
* 所在地区地址选择器需要[开通地图服务](map-config-agc.md#开通地图服务)。
* 需要[配置签名和指纹](account-sign-fingerprints.md)。

## 效果图

地址表单中的所在地区能根据详细地址内容自动补全，当补全内容不符合预期时，可通过地址选择器进行修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/GENpmgzHRBm9rP_wtNGnwQ/zh-cn_image_0000002583439203.png?HW-CC-KV=V1&HW-CC-Date=20260427T235045Z&HW-CC-Expire=86400&HW-CC-Sign=74E168A06C75F3381FB96FF70F37CBA4C1F0F973E6BD8B99968571ADE3668E7F)

## 示例代码

```
1. import { util } from '@kit.ArkTS';
2. import { i18n } from '@kit.LocalizationKit';
3. import { sceneMap, site } from '@kit.MapKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import { geoLocationManager } from '@kit.LocationKit';
7. import { abilityAccessCtrl, autoFillManager, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
8. import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
9. import { TextInputModifier } from '@kit.ArkUI';

11. const AUTHED = 0;
12. const TIME_OUT = 100;
13. // 默认经度和纬度。以下以北京天安门的经纬度为例。
14. const INIT_LAT = 39.5;
15. const INIT_LON = 116.2;
16. const ENGLISH = 'en';
17. const SIMPLIFIED_CHINESE = 'zh_CN';
18. const PERMISSIONS: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION'];
19. const ADMINISTRATIVE_REGION: Array<string> =
20. ['countryName', 'adminLevel1', 'adminLevel2', 'adminLevel3', 'adminLevel4'];

22. interface PersonInfo {
23. name?: string;
24. phone?: string;
25. email?: string;
26. idCard?: string;
27. region?: string;
28. streetAddress?: string;
29. }

31. interface RequestParam {
32. requestTag: string;
33. requestText: string;
34. }

36. interface Location {
37. latitude: number;
38. longitude: number;
39. }

41. // 显示授权弹出窗口。
42. async function reqPermissionsFromUser(permissions: Array<Permissions>,
43. context: common.UIAbilityContext): Promise<PermissionRequestResult> {
44. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
45. return await atManager.requestPermissionsFromUser(context, permissions);
46. }

48. // 节流函数。
49. function debounce(func: () => void, wait: number = TIME_OUT): Function {
50. let timeout: number | null = null;
51. return () => {
52. timeout && clearTimeout(timeout);
53. timeout = setTimeout(() => {
54. func();
55. clearTimeout(timeout);
56. }, wait);
57. };
58. }

60. @Extend(Text)
61. function textStyle() {
62. .width(64)
63. .textAlign(TextAlign.End)
64. }

66. @Entry
67. @Component
68. struct Index {
69. @State personInfo: PersonInfo = {};
70. @State isClicked: boolean = false;
71. // 用户是否已触发信息输入。
72. private isUserInput: boolean = false;
73. private location: Location = {
74. latitude: INIT_LAT,
75. longitude: INIT_LON,
76. };
77. private currentRequestTag: string = '';
78. private handleAddressChange = (request: RequestParam) => {
79. return debounce(async () => {
80. this.autoCompleteAddress(request);
81. });
82. };

84. aboutToAppear() {
85. reqPermissionsFromUser(PERMISSIONS, this.getUIContext().getHostContext() as common.UIAbilityContext)
86. .then((permissionRequestResult: PermissionRequestResult) => {
87. if (permissionRequestResult.authResults[0] === AUTHED) {
88. // 获取位置信息的API只能在授权的情况下被调用。
89. geoLocationManager.getCurrentLocation((err, location: geoLocationManager.Location) => {
90. if (err) {
91. hilog.error(0x0000, 'testTag', `Failed to get location, code: ${err?.code}, message: ${err?.message}`);
92. return;
93. }
94. hilog.info(0x0000, 'testTag', `Succeeded in obtaining the current location of the user`);
95. this.location.latitude = location.latitude;
96. this.location.longitude = location.longitude;
97. })
98. }
99. })
100. .catch((err: BusinessError) => {
101. hilog.error(0x0000, 'testTag', `Failed request permissions, code: ${err?.code}, message: ${err?.message}`);
102. })
103. }

105. public isUsLanguage(): boolean {
106. let result: string = '';
107. try {
108. result = i18n.System.getSystemLanguage();
109. } catch (error) {
110. hilog.error(0x0000, 'testTag', 'Failed to get system language');
111. }
112. return result.toLowerCase() === 'en-latn-us';
113. }

115. async autoCompleteAddress(request: RequestParam): Promise<void> {
116. try {
117. let params: site.SearchByTextParams = {
118. query: request.requestText,
119. // 搜索结果需要偏向的经纬度。
120. location: {
121. latitude: this.location.latitude,
122. longitude: this.location.longitude
123. },
124. language: this.isUsLanguage() ? ENGLISH : SIMPLIFIED_CHINESE,
125. isChildren: true
126. };
127. const result = await site.searchByText(params);
128. if (result.sites) {
129. let region: string = '';
130. let addressComponent = result.sites[0].addressComponent;
131. // 遍历当前地址的行政区划层级。
132. for (let item of ADMINISTRATIVE_REGION) {
133. if (addressComponent[item] === undefined) {
134. break;
135. }
136. region += addressComponent[item];
137. }
138. // 防止可能导致结果不一致的重复搜索。
139. if (request.requestTag === this.currentRequestTag) {
140. this.personInfo.region = region;
141. }
142. }
143. } catch (error) {
144. hilog.error(0x0000, 'testTag', `Failed to search location, code: ${error.code}, message: ${error.message}`);
145. }
146. hilog.info(0x0000, 'testTag', 'Succeeded in searching location');
147. }

149. onRegionClick(): void {
150. // 用户选择行政区域后，仅显示该区域的搜索结果，以防止查询时间过长。
151. this.currentRequestTag = util.generateRandomUUID();
152. let districtSelectOptions: sceneMap.DistrictSelectOptions = {
153. countryCode: 'CN',
154. };
155. sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
156. hilog.info(0x0000, 'testTag', 'SelectDistrict', 'Succeeded  in selecting district.');
157. let region = '';
158. for (let i = 0; i < data?.districts?.length; i++) {
159. region += data.districts[i].name;
160. }
161. this.personInfo.region = region;
162. }).catch((err: BusinessError) => {
163. hilog.error(0x0000, 'testTag', `Failed to select district, code: ${err.code}, message: ${err.message}`);
164. });
165. }

167. searchRegionByAddress(val: string): void {
168. let tag: string = util.generateRandomUUID();
169. this.currentRequestTag = tag;
170. let param: RequestParam = {
171. requestTag: tag,
172. requestText: val
173. }
174. // 用户输入的场景需要加做抖动处理, 智能填充回填场景直接查询即可。
175. if (this.personInfo.region && this.personInfo.region !== '') {
176. return;
177. }
178. if (this.isUserInput) {
179. this.handleAddressChange(param)();
180. } else {
181. this.autoCompleteAddress(param);
182. }
183. }

185. build() {
186. Column({ space: 8 }) {
187. Row({ space: 8 }) {
188. Text('姓名').textStyle()
189. TextInput({ text: this.personInfo.name, placeholder: '姓名' })
190. .layoutWeight(1)
191. .contentType(ContentType.PERSON_FULL_NAME)
192. .onChange((val: string) => {
193. this.personInfo.name = val;
194. })
195. }

197. Row({ space: 8 }) {
198. Text('联系电话').textStyle()
199. TextInput({ text: this.personInfo.phone, placeholder: '手机号码' })
200. .layoutWeight(1)
201. .contentType(ContentType.PHONE_NUMBER)
202. .onChange((val: string) => {
203. this.personInfo.phone = val;
204. })
205. }

207. Row({ space: 8 }) {
208. Text('身份证号').textStyle()
209. TextInput({ text: this.personInfo.idCard, placeholder: '身份证信息' })
210. .layoutWeight(1)
211. .contentType(ContentType.ID_CARD_NUMBER)
212. .onChange((val: string) => {
213. this.personInfo.idCard = val;
214. })
215. }

217. Row({ space: 8 }) {
218. Text('邮件地址').textStyle()
219. TextInput({ text: this.personInfo.email, placeholder: '电子邮件信息' })
220. .layoutWeight(1)
221. .contentType(ContentType.EMAIL_ADDRESS)
222. .onChange((val: string) => {
223. this.personInfo.email = val;
224. })
225. }

227. Row({ space: 8 }) {
228. Text('所在地区').textStyle()
229. FunctionalInput({
230. params: {
231. // InputType.SELECT_DISTRICT表示输入类型为省/市/区选择器类型。
232. inputType: functionalInputComponentManager.InputType.SELECT_DISTRICT,
233. textInputValue: {
234. text: this.personInfo.region,
235. placeholder: '省、市、区、街道地址',
236. },
237. // 调整TextInput样式。
238. inputAttributeModifier: new TextInputModifier()
239. .backgroundColor(Color.Transparent)
240. .onChange((value) => {
241. if (value !== this.personInfo.region) {
242. this.personInfo.region = value;
243. }
244. })
245. },
246. // 当InputType为SELECT_DISTRICT时，回调必须为onSelectDistrict。
247. controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
248. data: functionalInputComponentManager.DistrictSelectResult) => {
249. if (err) {
250. // 错误日志处理。
251. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
252. return;
253. }
254. // 成功日志处理。
255. hilog.info(0x0000, "testTag", "succeeded in selecting district");
256. this.personInfo.region = data.inputContent;
257. })
258. })
259. }

261. Row({ space: 8 }) {
262. Text('详细地址').textStyle()
263. TextInput({ text: this.personInfo.streetAddress, placeholder: '小区门牌信息' })
264. .layoutWeight(1)
265. .contentType(ContentType.DETAIL_INFO_WITHOUT_STREET)
266. .onDidInsert(() => {
267. // 当用户通过输入方法输入数据时触发。
268. this.isUserInput = true;
269. })
270. .onDidDelete((val: DeleteValue) => {
271. // 当用户通过输入方法删除数据时触发。
272. if (val?.deleteValue?.length > 0) {
273. this.isUserInput = true;
274. }
275. })
276. .onChange((val: string) => {
277. this.personInfo.streetAddress = val;
278. if (val && val.trim().length > 0) {
279. this.searchRegionByAddress(val);
280. } else {
281. this.currentRequestTag = util.generateRandomUUID();
282. this.personInfo.region = '';
283. }
284. this.isUserInput = false;
285. })
286. }

288. Button('保存')
289. .width('50%')
290. .onClick(() => {
291. if (!this.isClicked) {
292. this.isClicked = true;
293. autoFillManager.requestAutoSave(this.getUIContext(), {
294. onSuccess: () => {
295. hilog.info(0x0000, 'testTag', 'Succeeded in saving request');
296. },
297. onFailure: () => {
298. hilog.info(0x0000, 'testTag', 'Failed to save request');
299. }
300. });
301. setTimeout(() => {
302. this.isClicked = false;
303. }, 2000);
304. }
305. })
306. }
307. .padding({ left: 16, right: 16 })
308. .backgroundColor($r('sys.color.ohos_id_color_list_card_bg'))
309. .alignItems(HorizontalAlign.Center)
310. .height('100%')
311. .width('100%')
312. }
313. }
```

说明

该示例中，使用了场景化Input作为所在地区的地址选择器，智能填充支持对该地址选择器进行填充。
