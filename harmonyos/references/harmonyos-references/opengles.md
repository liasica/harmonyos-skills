---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengles
title: OpenGL ES
breadcrumb: API参考 > 标准库 > OpenGL ES
category: harmonyos-references
scraped_at: 2026-04-28T08:19:31+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:59e301575b7ac3455628b201115092469d9aa5c2b976d1fca4630d97744d17ad
---

OpenGL 是一种跨平台的图形 API，用于为 3D 图形处理硬件指定标准的软件接口。[OpenGL ES](https://www.khronos.org/opengles/) 是 OpenGL 规范的一种形式，适用于嵌入式设备。HarmonyOS 现已支持 OpenGL ES 3.2。

## 支持的能力

OpenGL ES 3.2

## 标准库中导出的符号列表

[native api中导出的OpenGL ES 3.2符号列表](openglesv3-symbol.md)

## 引入OpenGL能力

如果开发者使用OpenGL的相关能力，需要添加相关动态链接库和头文件。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libace_ndk.z.so
2. libace_napi.z.so
3. libGLESv3.so
4. libEGL.so
```

**头文件**

```
1. #include <ace/xcomponent/native_interface_xcomponent.h>
2. #include <EGL/egl.h>
3. #include <EGL/eglext.h>
4. #include <EGL/eglplatform.h>
5. #include <GLES3/gl3.h>
```

## 相关参考

针对OpenGL ES的使用和相关开发，需要同步了解NDK的开发过程，以及XComponent组件等的使用。具体可参考:

* [NDK开发参考](../harmonyos-guides/ndk-development-overview.md)
* [Node-API参考](napi.md)
* [XComponentNode参考](js-apis-arkui-xcomponentnode.md)
* [XComponent参考](ts-basic-components-xcomponent.md)

## OpenGL ES扩展接口

* OpenGL ES扩展接口的官方参考文档：[OpenGL ES扩展接口](https://registry.khronos.org/OpenGL/index_es.php)
* 开发者可以调用glGetString查询芯片厂商支持的扩展接口，调用之前务必初始化上下文。具体示例如下：

```
1. EGLDisplay display;
2. EGLConfig config;
3. EGLContext context;
4. EGLSurface surface;
5. EGLint majorVersion;
6. EGLint minorVersion;
7. EGLNativeWindowType win;
8. display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
9. eglInitialize(display, &majorVersion, &minorVersion);
10. EGLint attribs[] = {
11. EGL_RENDERABLE_TYPE,
12. EGL_OPENGL_ES2_BIT,
13. EGL_BLUE_SIZE, 8,
14. EGL_GREEN_SIZE, 8,
15. EGL_RED_SIZE, 8,
16. EGL_NONE
17. };
18. eglChooseConfig(display, attribs, &config, 1, &numConfigs);
19. context = eglCreateContext(display, config, EGL_NO_CONTEXT, NULL);
20. surface = eglCreatePbufferSurface(display, config, NULL);
21. eglMakeCurrent(display, surface, surface, context);

23. char *strTest = new char[1024];
24. strTest = (char *)glGetString(GL_EXTENSIONS); // 返回值strTest中会列出所有的扩展接口，并且用空格分隔开
25. bool isHave = strTest.find("GL_OES_matrix_palette") != -1 ?
26. true :
27. false; // 查询是否有某个扩展接口，有则isHave为true，没有则为false
```

## 简单示例

```
1. void enableVertexAttrib(GLuint index, float *data, int32_t len)
2. {
3. GLuint buffer;
4. glGenBuffers(1, &buffer);
5. glBindBuffer(GL_ARRAY_BUFFER, buffer);
6. glBufferData(GL_ARRAY_BUFFER, len, data, GL_STATIC_DRAW);
7. glVertexAttribPointer(index, TRIANGLES_POINT, GL_FLOAT, GL_FALSE, 0, 0);
8. glEnableVertexAttribArray(index);
9. return;
10. }

12. int32_t Init(void *window, int32_t width,  int32_t height)
13. {
14. EGLNativeWindowType mEglWindow;
15. EGLDisplay mEGLDisplay = EGL_NO_DISPLAY;
16. EGLConfig mEGLConfig = nullptr;
17. EGLContext mEGLContext = EGL_NO_CONTEXT;
18. EGLContext mSharedEGLContext = EGL_NO_CONTEXT;
19. EGLSurface mEGLSurface = nullptr;
20. EGLint configsNum;
21. mEglWindow = reinterpret_cast<EGLNativeWindowType>(window);

23. // 初始化EGL Display
24. mEGLDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);
25. EGLint eglMajVers;
26. EGLint eglMinVers;
27. eglInitialize(mEGLDisplay, &eglMajVers, &eglMinVers);

29. // 配置EGL
30. EGLint attribList[] = {
31. EGL_SURFACE_TYPE, EGL_WINDOW_BIT, EGL_RENDERABLE_TYPE, EGL_OPENGL_ES3_BIT,
32. EGL_RED_SIZE, 8,
33. EGL_GREEN_SIZE, 8,
34. EGL_BLUE_SIZE, 8,
35. EGL_NONE
36. };
37. eglChooseConfig(mEGLDisplay, attribList, &mEGLConfig, 1, &configsNum);

39. EGLint winAttribs[] = {EGL_GL_COLORSPACE_KHR, EGL_GL_COLORSPACE_SRGB_KHR, EGL_NONE};

41. // 创建EGL Surface
42. mEGLSurface = eglCreateWindowSurface(mEGLDisplay, mEGLConfig, mEglWindow, winAttribs);

44. // 创建EGL Context
45. EGLint attrib3_list[] = {
46. EGL_CONTEXT_CLIENT_VERSION, 3,
47. };
48. mEGLContext = eglCreateContext(mEGLDisplay, mEGLConfig, mSharedEGLContext, attrib3_list);

50. // 绑定EGL Context和Surface
51. eglMakeCurrent(mEGLDisplay, mEGLSurface, mEGLSurface, mEGLContext);

53. // 创建着色点程序
54. const char* g_vertexShader =
55. "#version 300 es\n"
56. "in vec4 a_pos;\n"
57. "in vec4 a_color;\n"
58. "uniform mat4 a_mx;\n"
59. "uniform mat4 a_my;\n"
60. "out vec4 v_color;\n"
61. "void main() {\n"
62. "    gl_Position = a_mx * a_my * a_pos;\n"
63. "    v_color = a_color;\n"
64. "}";

66. const char* g_fragmentShader =
67. "#version 300 es\n"
68. "precision mediump float;\n"
69. "in vec4 v_color;\n"
70. "out vec4 fragColor;\n"
71. "void main() {\n"
72. "    fragColor = v_color;\n"
73. "}";

75. // 创建顶点着色器
76. GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
77. glShaderSource(vertexShader, 1, &g_vertexShader, nullptr);
78. glCompileShader(vertexShader);

80. // 创建片段着色器
81. GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
82. glShaderSource(fragmentShader, 1, &g_fragmentShader, nullptr);
83. glCompileShader(fragmentShader);

86. // 创建着色器程序
87. mProgramHandle = glCreateProgram();
88. glAttachShader(mProgramHandle, vertexShader);
89. glAttachShader(mProgramHandle, fragmentShader);
90. glLinkProgram(mProgramHandle);

92. // 使用着色器程序
93. glUseProgram(mProgramHandle);

95. // 清理
96. glDeleteShader(vertexShader);
97. glDeleteShader(fragmentShader);

99. return 0;
100. }

102. void Update(float angleXOffset, float angleYOffset)
103. {
104. const float pi = 3.141592;

106. // 创建顶点位置数据数组vertexData
107. float g_vertexData[] = {
108. -0.75, -0.50, -0.43, 0.75, -0.50, -0.43, 0.00,  -0.50, 0.87,  0.75, -0.50, -0.43,
109. 0.00,  -0.50, 0.87,  0.00, 1.00,  0.00,  0.00,  -0.50, 0.87,  0.00, 1.00,  0.00,
110. -0.75, -0.50, -0.43, 0.00, 1.00,  0.00,  -0.75, -0.50, -0.43, 0.75, -0.50, -0.43,
111. };

113. // 创建顶点颜色数组colorData
114. float g_colorData[] = {
115. 1, 0, 0, 1, 0, 0, 1, 0, 0, /* 红色——面1 */
116. 1, 0, 0, 1, 0, 0, 1, 0, 0, /* 红色——面2 */
117. 1, 0, 0, 1, 0, 0, 1, 0, 0, /* 红色——面3 */
118. 1, 0, 0, 1, 0, 0, 1, 0, 0  /* 红色——面4 */
119. };

121. // 顶点法向量数组normalData
122. float g_normalData[] = {
123. 0.00,  -1.00, 0.00,  0.00,  -1.00, 0.00,  0.00,  -1.00, 0.00, -0.83, -0.28, -0.48,
124. -0.83, -0.28, -0.48, -0.83, -0.28, -0.48, -0.83, 0.28,  0.48, -0.83, 0.28,  0.48,
125. -0.83, 0.28,  0.48,  0.00,  -0.28, 0.96,  0.00,  -0.28, 0.96, 0.00,  -0.28, 0.96,
126. };

128. // 设置视口大小
129. glViewport(0, 0, m_width, m_height);

131. // 清除颜色缓存
132. glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
133. glClear(GL_COLOR_BUFFER_BIT);

135. // 获取着色器程序中变量的位置句柄
136. GLint aPos = glGetAttribLocation(mProgramHandle, "a_pos");
137. GLint aColor = glGetAttribLocation(mProgramHandle, "a_color");
138. GLint aNormal = glGetAttribLocation(mProgramHandle, "a_normal");
139. GLint uLightColor = glGetUniformLocation(mProgramHandle, "u_lightColor");
140. GLint uLightDirection = glGetUniformLocation(mProgramHandle, "u_lightDirection");
141. GLint aMx = glGetUniformLocation(mProgramHandle, "a_mx");
142. GLint aMy = glGetUniformLocation(mProgramHandle, "a_my");

144. angleX = angleXOffset;
145. angleY = angleYOffset;

147. // y轴旋转度
148. float radianY = (angleY * pi) / 180.0;
149. float cosY = cosf(radianY);
150. float sinY = sinf(radianY);
151. float myArr[] = {
152. cosY, 0, -sinY, 0,
153. 0, 1, 0, 0,
154. sinY, 0, cosY, 0,
155. 0, 0, 0, 1
156. };

158. // 向着色器传递4x4矩阵数据
159. glUniformMatrix4fv(aMy, 1, false, myArr);

161. // x轴旋转度
162. float radianX = (angleX * pi) / 180.0;
163. float cosX = cosf(radianX);
164. float sinX = sinf(radianX);
165. float mxArr[] = {
166. 1, 0, 0, 0, 0, cosX, -sinX, 0, 0, sinX, cosX, 0, 0, 0, 0, 1
167. };

169. glUniformMatrix4fv(aMx, 1, false, mxArr);

171. // 给平行光传入颜色和方向数据，RGB(1,1,1),单位向量(x,y,z)
172. glUniform3f(uLightColor, 1.0, 1.0, 1.0);

174. // 保证向量(x,y,z)的长度为1，即单位向量
175. float x = 2.0 / sqrt(15);
176. float y = 2.0 / sqrt(15);
177. float z = 3.0 / sqrt(15);

179. glUniform3f(uLightDirection, x, -y, z);

181. // 创建缓冲区buffer，传入顶点位置数据g_vertexData
182. enableVertexAttrib(aPos, g_vertexData, sizeof(g_vertexData));
183. enableVertexAttrib(aNormal, g_normalData, sizeof(g_normalData));
184. // 创建缓冲区colorBuffer，传入顶点颜色数据g_colorData
185. enableVertexAttrib(aColor, g_colorData, sizeof(g_colorData));

187. glEnable(GL_DEPTH_TEST);

189. // 绘制四棱锥
190. glDrawArrays(GL_TRIANGLES, 0, TETRAHEDRON_POINT);

192. // 交换缓冲区
193. eglSwapBuffers(mEGLDisplay, mEGLSurface);
194. }
```

该示例通过EGL创建和设置整个OpenGL ES渲染环境，实现一个3D四棱锥的渲染程序，下面详细地解释下每个步骤。

### 使用eglGetDisplay连接渲染目标设备

```
1. EGLDisplay eglGetDisplay(EGLNativeDisplayType display_id);
```

eglGetDisplay是EGL库中的函数，它返回EGLDisplay对象用于表示与渲染目标设备的连接。当显示连接不可用时，将返回EGL\_NO\_DISPLAY表示连接不可用。

display\_id 参数通常是一个表示显示设备的本地显示类型，EGLNativeDisplayType是为了匹配窗口显示类型，在各个平台有不同的定义。如果您只是希望使用默认的显示设备，那么您可以直接使用 EGL\_DEFAULT\_DISPLAY，而不需要显式地指定 display\_id。

### 使用eglInitialize初始化EGL

当成功打开连接之后则需要调用eglInitialize初始化EGL。

```
1. EGLBoolean eglInitialize(EGLDisplay display,    // 指定EGL显示连接
2. EGLint *majorVersion,  // 指定EGL实现返回的主版本号，可能为NULL
3. EGLint *minorVersion); // 指定EGL实现返回的次版本号，可能为NULL
```

这个函数用于初始化EGL内部数据结构，将返回EGL的版本号，并将其保存在majorVersion和minorVersion中。

如果初始化成功，则返回EGL\_TRUE，否则返回EGL\_FALSE。另外还可以通过EGLint eglGetError()，查询EGL的错误状态：

* EGL\_BAD\_DISPLAY：表示没有指定有效的EGLDisplay。
* EGL\_NOT\_INITIALIZED：表示EGL不能初始化。

### 使用eglChooseConfig确定渲染配置

EGL初始化成功之后，需要确定可用渲染表面的类型和配置，目前支持两种方法：

* 可以指定一组需要的配置，使用eglChooseConfig使EGL推荐最佳配置。

  当没有特殊配置需求时建议使用此种方法，因为这样更容易获得最佳配置。

  ```
  1. EGLBoolean eglChooseConfig(EGLDisplay dpy,     // EGL显示连接句柄，标识了要进行配置选择的显示连接。
  2. const EGLint *attrib_list, // 一个以EGL_NONE结尾的整数数组，用于指定所需配置的属性。属性列表中的每个元素都由属性名称（如EGL_RED_SIZE）和相应的属性值组成。如{EGL_RED_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_BLUE_SIZE, 8, EGL_NONE}。
  3. EGLConfig *configs,     // 一个用于存储选择配置的指针数组。eglChooseConfig函数将从可用配置中选择适合条件的配置，并将其存储在此数组中。
  4. EGLint config_size,     // configs数组的大小
  5. EGLint *num_config);    // 存储满足attrib_list需求，得到的满足需求的实际配置数量。
  ```

  ```
  1. // 如以上代码所示这里指定所需配置的属性为
  2. EGLint attribList[] = {
  3. EGL_SURFACE_TYPE, EGL_WINDOW_BIT, EGL_RENDERABLE_TYPE, EGL_OPENGL_ES3_BIT,  // 指定了渲染类型为 OpenGL ES 3
  4. EGL_RED_SIZE, 8,    // 指定红色缓冲区的位数是8位
  5. EGL_GREEN_SIZE, 8,  // 指定绿色缓冲区的位数是8位
  6. EGL_BLUE_SIZE, 8,   // 指定蓝色缓冲区的位数是8位
  7. EGL_NONE
  8. };
  9. eglChooseConfig(mEGLDisplay, attribList, &mEGLConfig, 1, &configsNum);
  ```

  在调用eglChooseConfig函数后，系统将根据指定的配置属性attribList返回满足需求的EGL配置，这些配置将存储在mEGLConfig参数中。示例代码中的configsNum参数传入值为1，表明mEGLConfig数组的大小为1，即仅能保存一组可用配置。尽管此设置限制了返回配置的数量，但在大多数应用场景下已能满足基本需求。同时，configsNum参数将实际保存满足指定属性的配置总数，为开发者提供完整的可选配置数量信息。
* 也可以使用eglGetConfigs查询支持的所有配置，并使用eglGetConfigAttrib筛选需要的配置。

  以下提供使用此种方法得到满足需求的配置，具体可见示例：

  ```
  1. #include <EGL/egl.h>
  2. #include <iostream>
  3. #include <vector>
  4. int main() {
  5. // 初始化 EGL
  6. EGLDisplay display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
  7. eglInitialize(display, nullptr, nullptr);

  9. // 获取所有配置
  10. EGLint numConfigs;
  11. eglGetConfigs(display, nullptr, 0, &numConfigs);
  12. std::vector<EGLConfig> configs(numConfigs);
  13. eglGetConfigs(display, configs.data(), numConfigs, &numConfigs);

  15. // 选择合适的配置
  16. EGLConfig chosenConfig = nullptr;
  17. for (const auto& config : configs) {
  18. EGLint redSize, greenSize, blueSize;
  19. eglGetConfigAttrib(display, config, EGL_RED_SIZE, &redSize);
  20. eglGetConfigAttrib(display, config, EGL_GREEN_SIZE, &greenSize);
  21. eglGetConfigAttrib(display, config, EGL_BLUE_SIZE, &blueSize);
  22. if (redSize == 8 && greenSize == 8 && blueSize == 6) {
  23. chosenConfig = config;
  24. break;
  25. }
  26. }

  28. // 如果未选择配置，则打印错误信息并退出
  29. if (!chosenConfig) {
  30. std::cerr << "Failed to find a suitable EGL configuration." << std::endl;
  31. return 1;
  32. }
  33. return 0;
  34. }
  ```

  ```
  1. EGLBoolean eglGetConfigs(EGLDisplay display, // EGL显示连接句柄，标识了要进行配置选择的显示连接。
  2. EGLConfig *configs, // 用于保存得到配置的数组
  3. EGLint config_size, // configs的数组大小
  4. EGLint *num_config);// 得到的EGL所有可用配置数量
  ```

  eglGetConfigs接口有以下两种用法：

  + 当我们传递configs为nullptr时，接口会返回EGL\_TRUE，并将得到的EGL所有可用配置数量保存在num\_config中，这时即可根据得到的数量初始化configs来保存这些配置了，具体见如上代码。
  + 当传递configs数组接受所有配置时，将得到所有配置并保存在configs，这样即可得到所有的可用配置，接下来可以根据具体需求筛选一组config保存下来。

  ```
  1. // 选择合适的配置
  2. EGLConfig chosenConfig = nullptr;
  3. for (const auto& config : configs) {
  4. EGLint redSize, greenSize, blueSize;
  5. eglGetConfigAttrib(display, config, EGL_RED_SIZE, &redSize);
  6. eglGetConfigAttrib(display, config, EGL_GREEN_SIZE, &greenSize);
  7. eglGetConfigAttrib(display, config, EGL_BLUE_SIZE, &blueSize);
  8. if (redSize == 8 && greenSize == 8 && blueSize == 6) {
  9. chosenConfig = config;
  10. break;
  11. }
  12. }
  ```

  如上所示遍历configs每个配置，使用eglGetConfigAttrib查询该配置下特定属性的值，将该值保存在第4个参数中，并判断值是否是自己需要的，如果需要则保存该配置，以待使用。调用成功则返回EGL\_TRUE，调用失败则返回EGL\_FALSE。 如果返回EGL\_FALSE，可以使用eglGetError查询失败的原因，如果返回EGL\_BAD ATTRIBUTE则attribute不是有效的属性。

  ```
  1. EGLBoolean eglGetConfigAttrib(EGLDisplay display,     // EGL 显示连接句柄，标识了要进行配置选择的显示连接
  2. EGLConfig config,  // EGLConfig 对象，表示要查询的 EGL 配置
  3. EGLint attribute,  // EGLint 类型的属性标识符，表示要查询的属性
  4. EGLint *value);    // 指向 EGLint 类型变量的指针，用于存储查询到的属性值。
  ```

### 使用eglCreateWindowSurface创建窗口表面

得到符合渲染需求的EGLConfig之后，可以使用eglCreateWindowSurface创建窗口表面。

```
1. EGLSurface eglCreateWindowSurface(EGLDisplay dpy,             // EGLDisplay对象，表示与窗口表面关联的显示连接。
2. EGLConfig config,           // EGLConfig对象，表示要创建窗口表面的EGL配置。
3. EGLNativeWindowType win,    // EGLNativeWindowType类型的参数，表示窗口的句柄或标识符，用于与EGL表面关联。
4. const EGLint *attrib_list); // 指向EGL属性列表的指针，用于指定窗口表面的属性。是一个以EGL_NONE结尾的整数数组。
```

eglCreateWindowSurface接受的属性attrib\_list的值如下所示：

```
1. EGL_RENDER_BUFFER EGL_SINGLE_BUFFER或EGL_BACK_BUFFER
2. EGL_SINGLE_BUFFER // 表示渲染表面将只有一个渲染缓冲区，在绘制完成后，渲染缓冲区中的内容将直接显示到屏幕上，不会进行双缓冲，可能会出现闪烁或撕裂的现象。
3. EGL_BACK_BUFFER   // 表示渲染表面将具有双缓冲区，即前缓冲区和后缓冲区。在绘制完成后，渲染缓冲区中的内容首先会绘制到后缓冲区，然后通过交换缓冲区的操作将后缓冲区的内容显示到屏幕上，这样可以避免闪烁和撕裂现象。
4. // 默认情况下是EGL_BACK_BUFFER，当设置为null，则为默认属性。
```

eglCreateWindowSurface创建窗口表面失败的可能原因如下：

* EGL\_BAD\_MATCH：表示窗口属性与提供的 EGLConfig 不匹配。这可能是因为EGLConfig不支持渲染到窗口（即EGL\_SURFACE\_TYPE 属性没有设置为 EGL\_WINDOW\_BIT）。
* EGL\_BAD\_CONFIG：如果提供的EGLConfig没有得到系统的支持，则会发生这种错误。
* EGL\_BAD\_NATIVE\_WINDOW：如果提供的窗口句柄无效，则会发生这种错误。
* EGL\_BAD\_ALLOC：如果eglCreateWindowSurface无法为新的EGL窗口分配资源，或者已经有与提供的窗口关联的EGLConfig，则会发生这种错误。

```
1. EGLint attribList[] = { EGL_RENDER_BUFFER, EGL_BACK_BUFFER, EGL_NONE };
2. EGLSurface surface = eglCreateWindowSurface(display, config, nativeWindow, attribList);
3. if (surface == EGL_NO_SURFACE) {
4. switch (eglGetError()) {
5. case EGL_BAD_MATCH:
6. // 检查窗口和 EGLConfig 属性以确定兼容性，或者验证 EGLConfig 是否支持渲染到窗口
7. break;
8. case EGL_BAD_CONFIG:
9. // 验证提供的 EGLConfig 是否有效
10. break;
11. case EGL_BAD_NATIVE_WINDOW:
12. // 验证提供的 EGLNativeWindow 是否有效
13. break;
14. case EGL_BAD_ALLOC:
15. // 资源不足；处理并恢复
16. break;
17. default:
18. // 处理任何其他错误
19. break;
20. }
21. }
```

在使用XComponent获取nativeWindow的过程中，通常涉及以下步骤：

1. 首先需要在ArkTS 中定义XComponent并设置 XComponentController。XComponent组件用于在UI中嵌入基于OpenGL或Vulkan等图形API实现的渲染内容。

   ```
   1. Column() {
   2. XComponent({
   3. id: 'myXComponent',
   4. type: XComponentType.SURFACE,
   5. controller: this.xComponentController
   6. })
   7. }
   ```
2. 创建 XComponentController子类，实现回调方法：

   ```
   1. class MyXComponentController extends XComponentController {
   2. onSurfaceCreated(surfaceId: string): void {
   3. console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
   4. nativeRender.SetSurfaceId(BigInt(surfaceId));
   5. // 之后会使用 surfaceId 关联 native window
   6. }

   8. onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
   9. console.info(`onSurfaceChanged surfaceId: ${surfaceId}`);
   10. }

   12. onSurfaceDestroyed(surfaceId: string): void {
   13. console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
   14. }
   15. }
   ```
3. 使用surfaceId获取NativeWindow：surfaceId是在XComponent创建过程中生成的。在onSurfaceCreated 回调中，可以使用OH\_NativeWindow\_CreateNativeWindowFromSurfaceId函数通过surfaceId获取nativeWindow。

   ```
   1. napi_value PluginManager::SetSurfaceId(napi_env env, napi_callback_info info)
   2. {
   3. int64_t surfaceId = ParseId(env, info);
   4. OHNativeWindow *nativeWindow;
   5. PluginRender *pluginRender;
   6. if (windowMap_.find(surfaceId) == windowMap_.end()) {
   7. OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &nativeWindow);
   8. windowMap_[surfaceId] = nativeWindow;
   9. } else {
   10. return nullptr;
   11. }
   12. if (pluginRenderMap_.find(surfaceId) == pluginRenderMap_.end()) {
   13. pluginRender = new PluginRender(surfaceId);
   14. pluginRenderMap_[surfaceId] = pluginRender;
   15. }
   16. pluginRender->InitNativeWindow(nativeWindow);
   17. return nullptr;
   18. }
   ```

### 使用eglCreateContext创建渲染上下文

eglCreateContext函数用于创建一个新的EGL上下文，并将其与特定的显示设备（display）和配置（config）关联起来。允许指定共享上下文（shareContext），以便与已经存在的OpenGL上下文共享状态信息。该函数的参数说明如下：

```
1. EGLContext eglCreateContext(EGLDisplay display,        // EGLDisplay类型，表示要创建上下文的EGL显示连接。
2. EGLConfig config,          // EGLConfig类型，表示与上下文关联的EGL配置。
3. EGLContext shareContext,   // EGLContext类型，表示要与新创建的上下文共享状态信息的现有上下文。如果不想共享状态信息，可以传递EGL_NO_CONTEXT。
4. const EGLint *attribList); // 指向属性列表的指针，用于指定上下文的属性。属性列表是以EGL_NONE结尾的一系列属性值对。
```

eglCreateContext 的attribList属性列表如下：

```
1. EGLint attrib3_list[] = {
2. EGL_CONTEXT_CLIENT_VERSION, 3, // 指定使用的openglES版本3相关的上下文类型
3. EGL_NONE
4. };
```

eglCreateContext 创建渲染上下文失败的原因为EGL\_BAD\_CONFIG，即提供的EGLConfig无效。

### 使用eglMakeCurrent将EGL上下文与绘图表面进行关联

```
1. EGLBoolean eglMakeCurrent(EGLDisplay display, // EGL显示连接的句柄，用于标识渲染设备。
2. EGLSurface draw,    // EGL绘图表面的句柄，指定要渲染到的目标表面。
3. EGLSurface read,    // EGL读取表面的句柄，用于像素读取等操作。通常情况下，可以将其设为与 draw 相同的值。
4. EGLContext context);// 要与指定表面关联的 EGL 上下文的句柄。
```

### 创建并使用着色器程序

```
1. // 创建顶点着色器
2. GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
3. glShaderSource(vertexShader, 1, &g_vertexShader, nullptr);
4. glCompileShader(vertexShader);

6. // 创建片段着色器
7. GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
8. glShaderSource(fragmentShader, 1, &g_fragmentShader, nullptr);
9. glCompileShader(fragmentShader);

11. // 创建着色器程序
12. mProgramHandle = glCreateProgram();
13. glAttachShader(mProgramHandle, vertexShader);
14. glAttachShader(mProgramHandle, fragmentShader);
15. glLinkProgram(mProgramHandle);

17. // 使用着色器程序
18. glUseProgram(mProgramHandle);
```

```
1. GLuint glCreateShader(GLenum shaderType);
```

glCreateShader用于创建一个指定类型（顶点着色器、片段着色器等）的着色器对象，并返回该对象的句柄。其中shaderType参数指定要创建的着色器类型，可以是GL\_VERTEX\_SHADER（顶点着色器）或 GL\_FRAGMENT\_SHADER（片段着色器）等。

```
1. void glShaderSource(GLuint shader, GLsizei count, const GLchar \**string, const GLint *length);
```

glShaderSource函数用于设置着色器对象的源代码。其中各参数含义如下：

* shader：要设置源代码的着色器对象的标识符。
* count：源代码字符串的数量。
* string：指向源代码字符串的指针数组。
* length：指向包含每个源代码字符串长度的整数数组，可以为nullptr，表示每个字符串都以null结尾。

```
1. void glCompileShader(GLuint shader);
```

glCompileShader函数用于编译指定的着色器对象，其中shader参数是要编译的着色器对象的标识符。

```
1. GLuint glCreateProgram(void);
```

glCreateProgram函数用于创建一个新的着色器程序对象，该函数返回一个新创建的着色器程序对象的标识符。

```
1. void glAttachShader(GLuint program, GLuint shader);
```

glAttachShader函数用于将一个着色器对象附加到一个着色器程序对象上，参数program是目标着色器程序对象的标识符，参数shader是要附加的着色器对象的标识符。

```
1. void glLinkProgram(GLuint program);
```

glLinkProgram函数用于链接一个着色器程序对象，将附加到该程序对象的着色器链接成一个可执行的渲染管线。

参数program是要链接的着色器程序对象的标识符。链接着色器程序时，OpenGL将会执行以下操作：将各个着色器对象中的代码合并成一个可执行的渲染管线。执行连接器优化，以优化渲染管线的性能。并将Uniform变量和Uniform块的信息进行绑定。

```
1. void glUseProgram(GLuint program);
```

glUseProgram函数用于激活指定的着色器程序对象。在调用glUseProgram 之后，所有的渲染调用将会使用该着色器程序进行处理。

在使用glCompileShader时可以使用以下代码检查是否正常。

```
1. // 编译着色器
2. glCompileShader(shader);

4. // 检查编译状态
5. glGetShaderiv(shader, GL_COMPILE_STATUS, &compiled);

7. if (!compiled)
8. {
9. GLint infoLen = 0;
10. // 获取着色器信息日志的长度
11. glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &infoLen);
12. if ( infoLen > 1 )
13. {
14. // 分配存储信息日志的内存
15. char *infoLog = malloc(sizeof(char) * infoLen);
16. // 获取并打印着色器信息日志
17. glGetShaderInfoLog(shader, infoLen, NULL, infoLog);
18. esLogMessage("Error compiling shader:\n%s\n", infoLog);
19. // 释放分配的内存
20. free(infoLog);
21. }
22. // 删除编译失败的着色器
23. glDeleteShader(shader);
24. return 0;
25. }
```

在使用glLinkProgram可使用如下代码检查是否正常。

```
1. // 链接程序对象
2. glLinkProgram(programObject);

4. // 检查链接状态
5. glGetProgramiv(programObject, GL_LINK_STATUS, &linked);

7. if (!linked)
8. {
9. GLint infoLen = 0;
10. // 获取程序对象信息日志的长度
11. glGetProgramiv(programObject, GL_INFO_LOG_LENGTH, &infoLen);
12. if (infoLen > 1)
13. {
14. // 分配存储信息日志的内存
15. char *infoLog = malloc(sizeof(char) * infoLen);
16. // 获取并打印程序对象的信息日志
17. glGetProgramInfoLog(programObject, infoLen, NULL, infoLog);
18. esLogMessage("Error linking program:\n%s\n", infoLog);
19. // 释放分配的内存
20. free(infoLog);
21. }
22. // 删除链接失败的程序对象
23. glDeleteProgram(programObject);
24. return FALSE;
25. }
```

### 使用glViewport设置视口大小

```
1. void glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
```

glViewport函数用于设置视口，指定OpenGL ES渲染区域在窗口的位置和大小。其中x、y指定视口的左下角在窗口中的坐标，width、height参数则指定视口的宽度和高度。

### 使用glClearColor设置清除颜色缓冲区时使用的颜色

```
1. void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
```

glClearColor(1.0f, 1.0f, 1.0f, 1.0f)此时设置清除颜色缓冲区时使用的颜色为 (1.0, 1.0, 1.0)，即红色分量为1.0、绿色分量为1.0、蓝色分量为1.0、透明度为1.0（不透明）。

### 使用glClear执行清除操作

```
1. void glClear(GLbitfield mask);
```

glClear函数用于清除指定的缓冲区。参数mask指定需要清除的缓冲区，可以是以下值的组合：

* GL\_COLOR\_BUFFER\_BIT：清除颜色缓冲区。
* GL\_DEPTH\_BUFFER\_BIT：清除深度缓冲区。
* GL\_STENCIL\_BUFFER\_BIT：清除模板缓冲区。

可调用glClear(GL\_COLOR\_BUFFER\_BIT)清除颜色缓冲区，并用之前glClearColor设置的颜色填充整个缓冲区。清除颜色缓冲区是在开始绘制新帧之前的一个常见操作，这可以确保屏幕上的每个像素都被初始化为指定的颜色值，以便绘制新的图像。也是绘制新帧的准备工作，类似于在画布上涂上底色，以便开始新的绘画。

### 使用glGetAttribLocation获取属性变量位置

```
1. GLint glGetAttribLocation(GLuint program, const GLchar *name);
```

glGetAttribLocation函数用于获取顶点着色器中某个属性的位置，这个位置在编译链接顶点着色器程序后就已经确定了，它是根据属性的名称来确定的。其中program指要查询的程序对象，name指要查询其位置的属性变量的名称。

### 使用glGetUniformLocation获取统一变量位置

```
1. GLint glGetUniformLocation(GLuint program, const GLchar *name);
```

glGetUniformLocation函数用于查询特定统一变量在程序对象中的位置。其中program指要查询的程序对象，name指要查询其位置的统一变量的名称。

### 使用glUniformMatrix4fv传递4×4矩阵

```
1. void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
```

glGetUniformLocation函数用于获取着色器中uniform变量的位置。其中各个参数含义如下：

* location：要修改的uniform变量的位置。
* count：要修改的矩阵的数量。如果目标uniform变量不是数组，则此值应为1；如果是数组，则应大于等于1。
* transpose：是否转置矩阵。如果是GL\_FALSE，则矩阵按列优先(column major)顺序传递；如果是GL\_TRUE，则矩阵按行优先(row major)顺序传递。
* value：由count个元素组成的数组的指针，这些元素将用于更新指定的uniform变量。

### 使用glUniform3f向着色器传递颜色和方向

```
1. void glUniform3f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2);
```

glUniform3f函数为当前程序对象指定Uniform变量的值。其中location指明要更改的变量位置，v0、v1、v2表示变量中要使用的新值。

### 创建缓冲区并上传数据到GPU

```
1. GLuint buffer;
2. glGenBuffers(1, &buffer);                                                  // 生成一个缓冲区对象
3. glBindBuffer(GL_ARRAY_BUFFER, buffer);                                     // 绑定缓冲区，将缓冲区设置为当前操作的缓冲区
4. glBufferData(GL_ARRAY_BUFFER, len, data, GL_STATIC_DRAW);                  // 上传数据到GPU
5. glVertexAttribPointer(index, TRIANGLES_POINT, GL_FLOAT, GL_FALSE, 0, 0);   // 设置顶点属性指针
6. glEnableVertexAttribArray(index);                                          // 启用顶点属性数组
```

```
1. void glBindBuffer(GLenum target,   // target：指定要绑定的缓冲目标,可为以下值之一：
2. // GL_ARRAY_BUFFER：用于存储顶点属性数据；
3. // GL_ELEMENT_ARRAY_BUFFER：用于存储索引数据等其他。
4. GLuint buffer);  // buffer为要绑定的顶点缓冲对象的名称。
```

```
1. void glBufferData(GLenum target,       // target：指定缓冲对象的类型，可为以下值之一：
2. // GL_ARRAY_BUFFER：用于存储顶点属性数据;
3. // GL_ELEMENT_ARRAY_BUFFER：用于存储索引数据。
4. GLsizeiptr size,     // 指定要分配的缓冲区的大小（以字节为单位）。
5. const GLvoid* data,  // 指定要复制到缓冲区的初始数据。
6. GLenum usage);       // 指定缓冲区的预期使用方式，可为以下值之一：
7. // GL_STATIC_DRAW：数据不会或几乎不会被修改，并且被绘制命令多次使用；
8. // GL_DYNAMIC_DRAW：数据会被频繁修改，并且被绘制命令多次使用；
9. // GL_STREAM_DRAW：数据会被修改，并且被绘制命令少量使用。
```

一旦调用glBufferData函数，数据就被复制到了OpenGL的缓冲对象中，并存储在GPU的显存中。这意味着数据可以在GPU上被高效地访问和处理，而无需频繁地从CPU内存传输数据，从而提高了渲染性能。

```
1. void glVertexAttribPointer(GLuint index,         // 指定要修改的顶点数组的起始索引，索引它与顶点着色器中的属性变量绑定。（layout (location = 0) in vec3 aPos;）
2. GLint size,           // 指定每个顶点属性的分量个数
3. GLenum type,          // 指定每个顶点属性分量的类型
4. GLboolean normalized, // 指定在访问顶点数据时是否将其映射到[0, 1]或[-1, 1]范围内
5. GLsizei stride,       // 指定顶点属性之间的偏移量,如果是精密性排列可以设置为0
6. const void *offset);  // 属性在缓冲区中的偏移量，允许在缓冲区中指定一个位置开始读取数据。
```

```
1. void glEnableVertexAttribArray(GLuint index);
```

glEnableVertexAttribArray函数用于启用指定索引的顶点属性数组。例如，调用glEnableVertexAttribArray(0)可以启用位置索引为0的顶点属性数组。

### 启用功能

```
1. void glEnable(GLenum cap);
```

glEnable函数用于启用各种功能，具体功能由参数cap决定，cap可为以下值：

* GL\_BLEND：启用颜色混合，例如实现半透明效果。
* GL\_DEPTH\_TEST：启用深度测试，根据坐标的远近自动隐藏被遮住的图形。
* GL\_CULL\_FACE：根据多边形在窗口坐标中的缠绕来剔除多边形。

### 绘制图元并显示

```
1. void glDrawArrays(GLenum mode,   // 参数指定要绘制的图元的类型，比如GL_TRIANGLES表示绘制三角形。
2. GLint first,   // 参数指定要绘制的顶点数组的起始索引。
3. GLsizei count  // 参数指定要绘制的顶点数量
4. );
```

glDrawArrays函数用于根据当前绑定的顶点数组和顶点属性以及其他设置来绘制图元。

```
1. EGLBoolean eglSwapBuffers(EGLDisplay dpy,      // EGL显示连接
2. EGLSurface surface); // 要交换其缓冲区的EGL表面
```

eglSwapBuffers函数用于交换前后缓冲区的内容，并将渲染结果显示在屏幕上。

## 示例代码

* [基于OpenGL图形库实现绘制三棱锥功能](https://gitcode.com/HarmonyOS_Samples/ndk-opengl)
