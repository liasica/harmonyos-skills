---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-implementation-class
title: 预加载实现类
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 添加预加载依赖类 > 预加载实现类
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ce62eb978af846cccb8e499827918455792409948c429ec2a1a166205f62910d
---

在“entry/src/main/ets/prefetchUtil”目录下新增PrefetchUtil.ets和PrefetchWrapper.ets。

PrefetchUtil和PrefetchWrapper实现类功能如下：

* PrefetchUtil：预加载API的封装类，为PrefetchWrapper提供预加载API封装接口。

  + 提供安装预加载的数据获取接口
  + 提供周期性预加载的任务注册接口和数据获取接口
  + 提供周期性预加载是否已拉取数据的判断接口
* PrefetchWrapper：预加载包装类，为页面提供预加载封装接口。

  + 提供安装预加载数据获取和渲染接口
  + 提供周期性预加载数据获取和渲染接口
  + 提供安装预加载和周期性预加载数据获取和渲染接口

## PrefetchUtil

周期性预加载任务注册间隔需要大于12小时，建议按照如下示例取值为24小时。

```
1. import { cloudResPrefetch } from '@kit.CloudFoundationKit'
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { PreferenceUtil } from '../common/PreferenceUtil';
4. import { GlobalContext } from '../common/GlobalContext';

6. const PREFERENCES_PREFETCH_STORE_NAME = 'defaultStore';
7. const PREFERENCES_PREFETCH_FIRST_REGISTER_TIME = 'prefetchTaskFirstRegisterTime'; // 首次注册时间
8. const PREFERENCES_PREFETCH_TASK_EXPIRE_TIME = 'prefetchTaskExpireTime'; // 任务过期时间
9. const PREFETCH_TASK_REGISTER_INTERVAL = 24 * 60 * 60 * 1000; // 24小时 < 72小时
10. const PREFETCH_DATA_UPDATE_INTERVAL = 12 * 60 * 60 * 1000; // 12小时
11. const HILOG_DOMAIN = 0x0000;
12. const TAG = 'Prefetch';

14. export class PrefetchUtil {
15. private static timeoutId: number = (0 - Number.MAX_VALUE);
16. private static hasPrefetchedData: boolean = false;
17. private static isPrefetchTaskRegistered: boolean = false;
18. private static now: number = (0 - Number.MAX_VALUE);

20. private constructor() {
21. }

23. /**
24. * 预加载数据获取
25. * @param type 安装预加载/周期预加载数据
26. * @throws 预加载getPrefetchResult API异常
27. * @returns PrefetchResult
28. */
29. public static async getPrefetchResult(type: cloudResPrefetch.PrefetchMode) {
30. return cloudResPrefetch.getPrefetchResult(type);
31. }

33. /**
34. * 周期性预加载应用注册任务，间隔24小时
35. * @param token 应用/用户级token，可以为空
36. * @param params 自定义筛选参数，定义为JSON格式，可以为空
37. * @param forceRegister 是否强制注册
38. */
39. public static async registerPrefetchTask(token: string, params: string | object,
40. forceRegister: boolean = false) {
41. await PrefetchUtil.updatePrefetchTaskInfo();
42. if (!forceRegister) {
43. await PrefetchUtil.registerPrefetchTaskNotForced(token, params);
44. return;
45. }
46. await PrefetchUtil.registerPrefetchTaskForced(token, params);
47. }

49. /**
50. * 是否有周期性预加载数据：如果是首次注册，12小时后才有周期性预加载数据
51. * @returns boolean
52. */
53. public static hasPrefetchTaskData() : boolean {
54. return PrefetchUtil.hasPrefetchedData;
55. }

57. private static async updatePrefetchTaskInfo() {
58. PrefetchUtil.now = Date.now();
59. if (PrefetchUtil.timeoutId != 0 - Number.MAX_VALUE) {
60. clearTimeout(PrefetchUtil.timeoutId);
61. }
62. let firstRegisterTime = await PreferenceUtil.getValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
63. PREFERENCES_PREFETCH_FIRST_REGISTER_TIME) as number;
64. if (firstRegisterTime) {
65. PrefetchUtil.isPrefetchTaskRegistered = true;
66. // 判断任务是否已获取数据(首次注册后12小时，之后数据每隔12小时更新一次)
67. if (PrefetchUtil.now - firstRegisterTime >= PREFETCH_DATA_UPDATE_INTERVAL) {
68. PrefetchUtil.hasPrefetchedData = true;
69. }
70. }
71. if (!PrefetchUtil.isPrefetchTaskRegistered) {
72. hilog.info(HILOG_DOMAIN, TAG, `first register time: ${PrefetchUtil.now}`);
73. await PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
74. PREFERENCES_PREFETCH_FIRST_REGISTER_TIME, PrefetchUtil.now);
75. }
76. }

78. private static async registerPrefetchTaskForced(token: string, params: string | object) {
79. // 过期或强制更新任务注册
80. let expireTime = PrefetchUtil.now + PREFETCH_TASK_REGISTER_INTERVAL;
81. hilog.info(HILOG_DOMAIN, TAG, `new expireTime: ${expireTime}`);
82. await PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
83. PREFERENCES_PREFETCH_TASK_EXPIRE_TIME, expireTime);
84. // 更新任务注册和定时器
85. PrefetchUtil.registerPrefetchTaskWithApi(token, params);
86. PrefetchUtil.updateTaskTimer(PREFETCH_TASK_REGISTER_INTERVAL);
87. }

89. private static async registerPrefetchTaskNotForced(token: string, params: string | object) {
90. // 判断任务到期，重新注册
91. let expireTime = await PreferenceUtil.getValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
92. PREFERENCES_PREFETCH_TASK_EXPIRE_TIME) as number;
93. if (expireTime && (PrefetchUtil.now < expireTime)) {
94. // 任务没有过期：只更新定时器
95. let delay = expireTime - PrefetchUtil.now;
96. hilog.info(HILOG_DOMAIN, TAG, `not expire, delay:${delay}`);
97. PrefetchUtil.updateTaskTimer(delay);
98. return;
99. }
100. await PrefetchUtil.registerPrefetchTaskForced(token, params);
101. }

103. private static registerPrefetchTaskWithApi(token: string, params: string | object) {
104. try {
105. cloudResPrefetch.registerPrefetchTask({
106. token: token,
107. params: params
108. });
109. hilog.info(HILOG_DOMAIN, TAG, `register success`);
110. } catch (error) {
111. hilog.error(HILOG_DOMAIN, TAG, `register catch = ${error.message}`);
112. }
113. }

115. private static updateTaskTimer(delay: number) {
116. PrefetchUtil.timeoutId = setTimeout(() => {
117. if (PrefetchUtil.timeoutId != (0 - Number.MAX_VALUE)) {
118. clearInterval(PrefetchUtil.timeoutId)
119. PrefetchUtil.timeoutId = (0 - Number.MAX_VALUE);
120. }
121. }, delay);
122. }
123. }
```

## PrefetchWrapper

* 预加载数据获取成功时，需要增加页面的渲染逻辑。
* 预加载数据获取失败时，需要做数据降级处理。如下示例代码以cloudFunctionCall接口触发云函数为例获取数据，请根据实际业务实现进行修改。

  需要注意以下两点：

  1. 使用cloudFunctionCall接口之前，请先[设置云函数配置项](cloudfoundation-call-function.md#设置云函数配置项)。
  2. 测试周期性预加载时，需要将下文示例代码periodicPrefetch方法中的如下代码块注释。若不注释，则需等待12h才能获取周期性预加载数据。

     ```
     1. if (!PrefetchUtil.hasPrefetchTaskData()) { // 是否有周期性预加载数据：如果是首次注册，12小时后才有周期性预加载数据
     2. hilog.info(HILOG_DOMAIN, TAG, 'not has prefetch data');
     3. this.cloudFunctionCall(); // 使用普通方式获取应用数据
     4. return;
     5. }
     ```

     测试完成后，取消上述代码块注释即可。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { cloudFunction, cloudResPrefetch } from '@kit.CloudFoundationKit';
3. import { PrefetchUtil } from './PrefetchUtil';
4. import { PreferenceUtil } from '../common/PreferenceUtil';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import { GlobalContext } from '../common/GlobalContext';
7. import { deferredLink } from '@kit.AppLinkingKit';

9. const HILOG_DOMAIN = 0x0000;
10. const TAG = 'PrefetchWrapper';
11. const PREFETCH_MODE = "prefetchMode";
12. const PREFETCH_LINK_MODE = "prefetchLinkMode";
13. const PREFERENCES_PREFETCH_STORE_NAME = 'defaultStore';

15. export class PrefetchWrapper {
16. private static instance: PrefetchWrapper;
17. private prefetchMode: number = 0;
18. private linkPrefetchMode: number = 0;

20. private constructor() {
21. }

23. public static getInstance(): PrefetchWrapper {
24. if (!PrefetchWrapper.instance) {
25. PrefetchWrapper.instance = new PrefetchWrapper();
26. }
27. return PrefetchWrapper.instance;
28. }

30. // 支持所有预加载类型
31. public async doPrefetch() {
32. // 应用安装后首次打开：优先使用跳链安装预加载
33. await this.doLinkPrefetch();
34. // 初始化prefetchMode
35. this.initPrefetchMode();
36. if (!this.prefetchMode) {
37. // 应用安装后首次打开：使用安装预加载
38. hilog.info(HILOG_DOMAIN, TAG, 'installPrefetch');
39. this.installPrefetch();
40. this.setPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
41. } else {
42. // 应用安装后非首次打开：使用周期性预加载
43. hilog.info(HILOG_DOMAIN, TAG, 'periodicPrefetch: %{public}d', this.prefetchMode);
44. this.periodicPrefetch();
45. }
46. }

48. // 仅支持安装预加载
49. public doInstallPrefetch() {
50. // 初始化prefetchMode
51. this.initPrefetchMode();
52. if (!this.prefetchMode) {
53. // 应用安装后首次打开：使用安装预加载
54. hilog.info(HILOG_DOMAIN, TAG, 'installPrefetch');
55. this.installPrefetch();
56. this.setPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
57. }
58. }

60. // 仅支持周期性预加载
61. public doPeriodicPrefetch() {
62. // 初始化prefetchMode
63. this.initPrefetchMode();
64. if (!this.prefetchMode) {
65. this.setPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
66. } else {
67. // 应用安装后非首次打开：使用周期性预加载
68. hilog.info(HILOG_DOMAIN, TAG, 'periodicPrefetch: %{public}d', this.prefetchMode);
69. this.periodicPrefetch();
70. }
71. }

73. // 支持跳链安装预加载：应用安装后10分钟内有效
74. public async doLinkPrefetch(): Promise<boolean> {
75. try {
76. let link = await this.popPrefetchLink();
77. if (link.length < 1) {
78. hilog.error(HILOG_DOMAIN, TAG, `get install link null`);
79. return Promise.resolve(false);
80. }
81. let params: cloudResPrefetch.PrefetchParams = {
82. link: link
83. }
84. let dataResult = await cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.LINK_PREFETCH, params);
85. // todo 处理dataResult，跳转应用详情页并渲染
86. hilog.info(HILOG_DOMAIN, TAG, 'get install link prefetch dataResult: %{public}s', JSON.stringify(dataResult));
87. return Promise.resolve(true);
88. } catch (err) {
89. return Promise.resolve(false);
90. }
91. }

93. private installPrefetch() {
94. PrefetchUtil.getPrefetchResult(cloudResPrefetch.PrefetchMode.INSTALL_PREFETCH)
95. .then((data: cloudResPrefetch.PrefetchResult) => { // 接口调用成功，处理缓存的应用数据
96. hilog.info(HILOG_DOMAIN, TAG, 'get install prefetch cache successfully');
97. let dataResult = data.result; // data.result即是缓存的应用数据
98. // todo 处理dataResult
99. hilog.info(HILOG_DOMAIN, TAG, 'get install prefetch dataResult: %{public}s', JSON.stringify(dataResult));
100. })
101. .catch((err: BusinessError) => {
102. hilog.error(HILOG_DOMAIN, TAG, `get install prefetch cache failed: ${err.message}, ${err.code}`);
103. this.cloudFunctionCall(); // 应用走原有逻辑获取数据，示例使用云函数获取
104. })
105. }

107. private initPrefetchMode() {
108. if (!this.prefetchMode) {
109. let context = GlobalContext.getContext();
110. this.prefetchMode =
111. PreferenceUtil.getValueSync(context, PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_MODE) as number;
112. }
113. }

115. private setPrefetchMode(mode: number) {
116. PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_MODE, mode);
117. }

119. private initLinkPrefetchMode() {
120. if (!this.linkPrefetchMode) {
121. let context = GlobalContext.getContext();
122. this.linkPrefetchMode =
123. PreferenceUtil.getValueSync(context, PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_LINK_MODE) as number;
124. }
125. }

127. private setLinkPrefetchMode(mode: number) {
128. PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_LINK_MODE, mode);
129. }

131. private initPeriodPrefetch() {
132. let token = ''; // 应用自定义token参数，通常作为鉴权参数使用。在开发云侧云函数时，可以提取鉴权信息，也可以不进行鉴权。如果不需要鉴权，该参数可以为空
133. let params = ''; // 应用自定义params参数，通常作为筛选参数使用，可以定义为JSON格式。在开发云侧云函数时，可以提取该参数进行筛选。如果不需要筛选，该参数可以为空
134. PrefetchUtil.registerPrefetchTask(token, params);
135. }

137. private periodicPrefetch() {
138. this.initPeriodPrefetch();
139. if (!PrefetchUtil.hasPrefetchTaskData()) { // 是否有周期性预加载数据：如果是首次注册，12小时后才有周期性预加载数据
140. hilog.info(HILOG_DOMAIN, TAG, 'not has prefetch data');
141. this.cloudFunctionCall(); // 使用普通方式获取应用数据
142. return;
143. }
144. PrefetchUtil.getPrefetchResult(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH)
145. .then((data: cloudResPrefetch.PrefetchResult) => { // 接口调用成功，处理缓存的应用数据
146. hilog.info(HILOG_DOMAIN, TAG, 'get periodic prefetch cache successfully');
147. let dataResult = data.result; // data.result即是缓存的应用数据
148. let timestamp = data.timestamp; // data.timestamp即是缓存拉取时间
149. let token = data.token; // data.token即是注册任务token
150. // todo 处理dataResult
151. hilog.info(HILOG_DOMAIN, TAG, 'get periodic prefetch dataResult: %{public}s', JSON.stringify(dataResult));
152. hilog.info(HILOG_DOMAIN, TAG, 'get periodic prefetch timestamp: %{public}s', timestamp.toString());
153. hilog.info(HILOG_DOMAIN, TAG, 'get periodic prefetch token: %{public}s', token)
154. })
155. .catch((err: BusinessError) => {
156. hilog.error(HILOG_DOMAIN, TAG, `get periodic prefetch cache failed: ${err.message}, ${err.code}`);
157. this.cloudFunctionCall(); // 应用走原有逻辑获取数据，示例使用云函数获取
158. })
159. }

161. // 获取跳链安装预加载的链接信息
162. private async popPrefetchLink(): Promise<string> {
163. this.initLinkPrefetchMode();
164. if (this.linkPrefetchMode) {
165. return Promise.resolve("");
166. }
167. this.setLinkPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
168. try {
169. let link = await deferredLink.popDeferredLink();
170. return Promise.resolve(link);
171. } catch (err) {
172. return Promise.resolve("");
173. }
174. }

176. private cloudFunctionCall() {
177. hilog.info(HILOG_DOMAIN, TAG, 'cloudFunctionCall start');
178. cloudFunction.call({
179. name: "function_name", // 需修改为实际的云函数名称
180. timeout: 5 * 1000
181. }).then((data: cloudFunction.FunctionResult) => {
182. hilog.info(HILOG_DOMAIN, TAG, 'call function successfully');
183. let dataResult = data.result; // data.result即是缓存的应用数据
184. // todo 处理dataResult
185. hilog.info(HILOG_DOMAIN, TAG, 'call function get: %{public}s', JSON.stringify(dataResult));
186. }).catch((err: BusinessError) => {
187. hilog.error(HILOG_DOMAIN, TAG, 'call function failed: %{public}s', err.message);
188. })
189. }
190. }
```
