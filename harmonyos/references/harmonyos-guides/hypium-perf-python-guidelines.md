---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-perf-python-guidelines
title: 自定义性能脚本测试（基于Python）
breadcrumb: 指南 > 应用测试 > 单元测试和UI测试 > 自定义性能脚本测试（基于Python）
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:20+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:fa82818379b8f86e36b38f1484149f41440af4a3db8f9896fe34a5dc711de480
---

## **概述**

DevEco Testing场景化的性能测试服务，基于Hypium自动化测试框架，为开发者提供性能测试能力，支持使用Python编写应用的性能测试脚本。本指南主要讲解性能测试脚本的开发。

Hypium基本API接口功能介绍，请参考指导：[Hypium框架-API使用方法](hypium-python-guidelines.md#section1141818121333)。

测试服务执行测试脚本详情介绍，请参考指导：[场景化性能测试](performance-testing.md#section8642101711299)。

## **环境搭建**

**1、系统要求**

**Windows**

操作系统：Windows 10/11 64 位

内存：推荐使用16GB及以上（可用内存大于8G）

处理器：i7-10700@2.9GHz或者同等性能的型号

硬盘：可用硬盘空间100GB以上

**Mac**

操作系统：MacOS 13及以上

内存：推荐使用16GB及以上（可用内存大于8G）

处理器：i7-10700@2.9GHz及以上或Apple silicon M系列

硬盘：可用硬盘空间100GB以上

**2、环境配置**

**安装Python及Hypium**

参考指导：[应用UI测试-安装指导](hypium-python-guidelines.md)。

**安装hypium\_perf**

1）打开DevEco Testing客户端-测试服务-性能测试-场景化性能测试卡片，点击获取安装包，打开安装包目录，如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/P4efHjqlS3anCMJQz7pAig/zh-cn_image_0000002633533164.png "点击放大")

2）由于存在依赖关系，需要依次步骤1目录下的hypium、hypium-perf、perf\_analyzer等安装包。

安装命令示例

```screen
pip install hypium-6.1.0.201.tar.gz
pip install hypium-perf-6.1.0.201.tar.gz
pip install perf_analyzer-6.1.0.12b0-py3-none-any.whl perf_collector-6.1.0.12b0-py3-none-any.whl perf_common-6.1.0.12b0-py3-none-any.whl perf_resource-6.1.0.12b0-py3-none-any.whl
```

**注意** 

1、以上命令中安装包的版本仅供示例，具体版本号请参照实际下载版本。

2、若安装 paddlepaddle 失败，请先安装当前目录下提供的 paddlepaddle 的 whl 包，然后再安装其他 Python 包。

3）安装完成后，可前往查看PyCharm-设置-项目-Python解释器中的软件包与已安装版本是否一致。

## **脚本写作&调试**

## 脚本写作

**1、下载工程模板**

1）打开DevEco Testing客户端-测试服务-性能测试-场景化性能测试卡片，在测试前准备中，点击创建工程模板按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/vNH0XGpYQWi_VYv1pZfN6Q/zh-cn_image_0000002663932247.png "点击放大")

2）填写工程项目名称，选择工程存放路径，点击开始生成按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/61tP4nQ3QIWHEuKTI8OhFg/zh-cn_image_0000002664012301.png "点击放大")

3）在步骤2中填写的项目路径下，将自动生成用例模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/cZERT43wSMWV4V7d0GL5zg/zh-cn_image_0000002664012295.png)

**注意** 

已创建的工程模板可在PyCharm中直接调试，或根据实际测试场景编写脚本。调试成功后，即可在DevEco Testing上执行性能测试。详细步骤请参阅本地脚本调试及测试执行章节。

**2、场景用例和原子用例使用说明**

（1）测试步骤

用户的一次操作定义为一个测试步骤。

（2）原子用例

多个测试步骤组合完成一套操作，形成一个原子用例。原子用例存放在models目录中，对应脚本中的一个模型，具有独立的编号。原子用例是最小的用例单元，且可以被重复使用。

（3） 场景用例

用户完成一件事情定义为一个场景用例。例如：用户在小红书浏览后去淘宝搜索购物。

一个场景用例对应一个用例文件，编号与文件名一致，存放在testcases目录下。场景用例是测试执行的入口，一个场景用例可以由多个原子用例组成。例如，上述场景可以由两个原子用例组成：1）用户浏览小红书；2）用户在淘宝搜索并购物。这两个原子用例独立且可被重用。

如果有另一个场景用例：用户在小红书浏览后去京东购物，那么“用户浏览小红书”这个原子用例即可被重用。

测试的执行入口和结果反馈均以场景用例为单位。

**注意** 

* 1个性能场景用例由1-N个原子用例(Model)组成，1个原子用例对应1-N个测试步骤。
* 每个场景用例都需要一个配对的json配置文件。
* 场景用例包含的步骤数建议在30个步骤以下，步骤数过多可能会导致执行异常，建议进行用例拆分。
* 原子用例可以放在models目录下，推荐按照APP进行区分。

**3、场景用例写作指导**

**Testcase编写规范：**

Testcase对应的是测试场景中的一系列相关的原子用例操作序列。

（1）命名规范：

一个Testcase是一个独立的Python文件，Testcase编号与Python文件名一致，例：OH\_PerfDemoTest.py。

（2）继承规范：

Testcase必须继承PerfBaseCase类，PerfBaseCase会负责用例开始时的初始化流程，进行一些设备环境检查操作。

（3）注释规范：

将Testcase的场景描述放置在用例最上方，方便审视测试场景所包含的原子用例执行步骤对应关系。

**场景用例示例：**

```screen
import os
from hypium.advance.perf.application_model.perf_basecase import PerfBaseCase
from models.browse_huawei_video import BrowseHuaweiVideo
# 场景用例名，和py文件名一致，可以自定义，但有推荐命名格式，需同步生成同名的json文件
# 测试用例应继承PerfBaseCase
'''
@场景用例
浏览视频应用界面
@预置条件
无
@原子用例
视频页面浏览
'''
class OH_PerfDemoTest(PerfBaseCase):
    def __init__(self, controllers):  # 初始化操作，这里一般情况下不作变动
        self.TAG = self.__class__.__name__
        self.tests = [  # 指定场景用例执行入口
            "test_step"
        ]
        self.case_id = os.path.splitext(os.path.basename(__file__))[0]  # 文件名, 类名, case_id 三者保持一致
        self.case_scene_name = '浏览视频应用界面'  # 指定场景用例名称，用于显示在报告中
        case_pkg = 'com.huawei.hmsapp.himovie'  # 指定被测试应用，用于采集应用资源使用信息，如果未配置，则不采集
        PerfBaseCase.__init__(self, controllers, case_pkg)  # 调用父类初始化方法
        self.log.info("Case id is %s" % self.case_id)
    def setup(self):
        # 场景用例前置化操作，在test_step前执行的一些操作
        self.log.info("预置工作:初始化设备开始................." + self.devices[0].device_sn)
    def test_step(self):
        # 组装需要调用的原子用例，使用原子化用例构建场景步骤，可以一个场景用例添加多个相关的原子用例
        steps = [
            # 原子用例需要传入driver，case_id
            BrowseHuaweiVideo(self.driver, self.case_id)
        ]
        # 按顺序执行原子用例
        for item in steps:
            item.execute()
    def teardown(self):
        # 获取用例测试结果
        result = self.get_case_result()
        # 场景用例结束后执行该teardown操作
        self.log.info("收尾工作................., result is {}".format(result))
        # 此处为用例结尾时执行的PerfBaseCase的teardown方法，处理一些结束操作
        PerfBaseCase.teardown(self)
```

OH\_PerfDemoTest.json 配置文件示例

```screen
{
    "description": "Config for OpenHarmony devicetest test cases",
    "environment": [
        {
            "type": "device"
        }
    ],
    "driver": {
        "type": "DeviceTest",
        "py_file": ["OH_PerfDemoTest.py"]
    }
}
```

**注意** 

py\_file 的值表示场景用例文件相对于 testcases 文件夹的路径。

例如，若场景用例文件直接位于 testcases 文件夹下，则 py\_file 的值为 ["OH\_PerfDemoTest.py"]，若场景用例文件位于 testcases 下的 test\_01 文件夹中，则 py\_file 的值为 ["test\_01/OH\_PerfDemoTest.py"]。

**4、原子用例写作指导**

**Model编写规范：**

Model对应的是原子用例中的一组操作序列，在脚本编写时对应一个Model类。

（1）命名规范：

一个Model是一个原子用例，Model类命名要有一定业务含义，例如：”视频页面浏览”命名为BrowseHuaweiVideo。

（2）继承规范：

Model类必须继承基类ModelBase，ModelBase会负责与采集器的交互，并且处理Model类抛出的异常。

（3）注释规范：

将原子用例操作步骤放置在用例最上方，方便审视Model类步骤和用例执行步骤对应关系。

**原子用例示例：**

```screen
from hypium import BY
from hypium.advance.perf.application_model.model_base import ModelBase
from hypium.advance.perf.driver_perf.idriver_perf import IDriverPerf
from hypium.advance.perf.driver_perf.tag import SceneType
from hypium.model import UiParam
'''
@原子用例
视频页面浏览
@预置条件
无
@用例步骤
1.冷启动视频
2.上滑1次浏览界面
3.下滑1次浏览界面
4.切换到影院界面
5.精确的向上滑动界面
6.抛滑，向下滑动界面
7.侧滑返回
8.点击我的
9.上滑返回桌面
'''
APP_NAME = "视频"
class BrowseHuaweiVideo(ModelBase):  # 原子用例统一继承ModelBase
    def __init__(self, uidriver: IDriverPerf, case_id):  # 进行初始化操作
        ModelBase.__init__(self, uidriver, case_id)  # 调用父类初始化方法
        self.scene_no = "browse_huawei_video"  # 原子用例id
        self.scene_name = "浏览视频应用"  # 原子用例名字
        self.scene_type = "浏览视频应用场景"  # 原子用例类型
        self.scene_path = "日常高频操作-基础操作场景-系统通用操作场景-浏览视频应用"  # 原子用例所属路径
        self.driver = uidriver
    def setup(self):
        # 原子用例预置动作
        # 停止指定的应用
        self.driver.stop_app('com.huawei.hmsapp.himovie')
        # 返回手机桌面主页
        self.driver.go_home()
    @ModelBase.scene_recover
    def execute(self):
        # 1.冷启动应用'视频'
        # start_application_perf 启动应用的接口，从主页开始滑动查找对应APP名的应用，应用需要在桌面上可见，找到应用直接点击，打开应用
        # start_application_perf 接口为6.0版本新增接口请基于 DevEco Testing Hypium6.0.0 Release版本使用
        self.driver.start_application_perf("视频", SceneType.COLD_START)
        # 等待指定时间，等待界面稳定，再进行下一步操作
        self.driver.wait(3)
        # 2.上滑1次浏览界面
        # swipe_perf 在屏幕上或者指定区域area中执行朝向指定方向direction的滑动操作
        self.driver.swipe_perf(UiParam.UP,
                               tag=self.create_tag("上滑1次浏览界面", SceneType.NO_PAGE_SWITCH))
        # 等待指定时间，等待界面稳定，再进行下一步操作
        self.driver.wait(1)
        # 3.下滑1次浏览界面
        self.driver.swipe_perf(UiParam.DOWN,
                               tag=self.create_tag("下滑1次浏览界面", SceneType.NO_PAGE_SWITCH))
        # 等待指定时间，等待界面稳定，再进行下一步操作
        self.driver.wait(1)
        # 4.使用find_component查找控件，返回一个控件对象（控件文本为影院）
        com = self.driver.find_component(BY.text('影院'))
        # 可将控件对象传入touch_perf，会自动识别并转换为坐标点击
        self.driver.touch_perf(com, tag=self.create_tag("切换到影院界面", SceneType.WITH_PAGE_SWITCH))
        # 5.精确的向上滑动界面
        # slide_perf 根据指定的起始和结束位置执行滑动操作，起始和结束的位置可以为控件或者屏幕坐标。该接口用于执行较为精准的滑动操作。
        self.driver.slide_perf((0.5, 0.8), (0.5, 0.2), slide_time=0.5,
                               tag=self.create_tag("精确的向上滑动界面", SceneType.NO_PAGE_SWITCH))
        # 6.抛滑，向下滑动界面
        # fling_perf 抛滑接口
        self.driver.fling_perf(UiParam.DOWN, tag=self.create_tag("抛滑，向下滑动界面", SceneType.NO_PAGE_SWITCH))
        # 对于不需要性能指标的接口，可以使用不带perf的接口
        self.driver.touch((0.5, 0.3))
        # 等待指定时间，等待界面稳定，再进行下一步操作
        self.driver.wait(3)
        # 7.侧滑返回，退出
        # swipe_to_back_perf 滑动屏幕右侧返回
        self.driver.swipe_to_back_perf(tag=self.create_tag("侧滑返回", SceneType.WITH_PAGE_SWITCH))
        # 使用find_all_components根据BY指定的条件查找控件, 返回所有符合条件的控件，返回值是多个多个控件对象的值组成的列表（控件text值为我的）
        comps = self.driver.find_all_components(BY.text("我的"))
        # 8.点击我的
        # 可将控件对象传入touch_perf，会自动识别并转换为坐标点击
        self.driver.touch_perf(comps[0], tag=self.create_tag("点击我的", SceneType.WITH_PAGE_SWITCH))
        # 9.上滑返回桌面
        # swipe_to_home_perf 从屏幕底部上滑返回桌面
        self.driver.swipe_to_home_perf(tag=self.create_tag("上滑返回桌面", SceneType.WITH_PAGE_SWITCH))
    def teardown(self):
        # 原子用例结束清理步骤
        # 停止指定的应用
        self.driver.stop_app('com.huawei.hmsapp.himovie')
```

**5、使用UIViewer查看控件**

使用DevEco Testing->实用工具->UIViewer工具，辅助脚本写作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/P7xwhcOQRkGx2F5MRhI4ew/zh-cn_image_0000002663932241.png)

## 测试框架介绍

**1、功能介绍**

性能测试框架作为Hypium自动化测试框架的增强能力，其设备操作API与Hypium保持一致。该框架主要负责性能自动化测试模型的流程控制，管理测试过程中的trace资源和视频资源采集，并提供自动化测试完成后的指标分析功能。

Hypium基本API接口功能介绍，请参考指导：[Hypium框架-API使用方法](hypium-python-guidelines.md#section1141818121333)。

注：若测试场景包含隐私界面则无法录屏进行测试，例如银行类应用、密码界面等。

**2、场景tag**

场景tag是测试框架定义的一套用于标注测试步骤使用场景的标签。

```screen
def create_tag(self, step_name="", scene_type="", tag_id="", pkg_name="", dynamic_type="", action_type="", trigger_type="", is_first_swipe=False, wait_time=0, is_watch=False, is_seek=False, is_short_video=False, need_wait_scene=True, ad_monitor=False, cold_start_wait_time=None, pop_up_window_enable=True, extend_param={})
```

| 参数名称 | 参数描述 |
| --- | --- |
| step\_name | 必填，测试步骤名字。 |
| scene\_type | 必填，对应性能tag类型，从SceneType中选择。 |
| tag\_id | 非必填，指定标签id。 |
| pkg\_name | 非必填，测试应用相关包名。 |
| dynamic\_type | 非必填，标记当前操作是否为动态阈值。 |
| action\_type | 非必填，标记当前操作的类型。 |
| is\_first\_swipe | 默认False，标记是否为列表页面的首次滑动。 |
| wait\_time | 默认0，增加采集时长，避免采集未包含全部动效。 |
| is\_watch | 默认False，不做视频观看操作，设置为True会对页面进行30S观看，在scene\_type为WATCH时生效。 |
| is\_seek | 默认False，设置为True表示该操作为滑动进度条的操作。 |
| is\_short\_video | 默认False，在scene\_type字段为PLAY\_VIDEO时生效，标记起播视频为长视频（False）或者短视频（True）。  （时长小于5分钟的视频为短视频） |
| need\_wait\_scene | 默认True，在执行完perf接口后需要进行预置等待时间，设置为False时，不需要进行等待。 |
| ad\_monitor | 默认为False，在scene\_type字段为COLD\_START时生效，设置为True时，会进行广告检测。 |
| cold\_start\_wait\_time | 非必填，在scene\_type字段为COLD\_START时生效，表示冷启动后，需要额外等待的时间。 |
| pop\_up\_window\_enable | 默认True，在scene\_type字段为COLD\_START时生效，表示冷启动后，是否执行一次弹窗检测操作。 |
| extend\_param | 预留字段。 |

**注意** 

所有性能测试需要采集指标的步骤，有以下3个原则：

* API接口使用 \_perf方法。
* 必须带上场景tag。
* 每个步骤必须是单独的tag，不能多个步骤共用一个tag。

**3、****场景tag类型**

```screen
class SceneType(Enum):
    # 起播时延
    PLAY_VIDEO = "PLAY_VIDEO"
    # 冷启
    COLD_START = "COLD_START"
    # 热启
    HOT_START = "HOT_START"
    # 有页面切换
    WITH_PAGE_SWITCH = "WITH_PAGE_SWITCH"
    # 无页面切换
    NO_PAGE_SWITCH = "NO_PAGE_SWITCH"
    # 视频观看
    WATCH = "WATCH"
```

注：滑动和无页面切换操作的场景不测完成时延；冷启动操作前需要杀掉该后台应用，热启动操作前需要拉起该应用并置于后台。

**4、****hypium\_perf常用接口和用法**

在Hypium的界面操作接口上封装一套perf接口，提供给性能测试使用。

**须知** 

以下所有示例代码中driver都是UiExplorerPerf对象。

**Phone常用接口**

**1、点击****操作**

```screen
def touch_perf(self, target: Union[By, UiComponent, tuple], wait_time: float = 0.1, tag: Tag = None)
```

**接口说明**

根据选定的控件或者坐标位置执行点击操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | target | 需要点击的目标，可以为控件（通过By类指定）或者屏幕坐标（通过tuple类型指定，例如（100，200）， 其中100为x轴坐标，200为y轴坐标）， 或者使用find\_component找到的控件对象。 |
| 2 | wait\_time | 点击后等待响应的时间，默认0.1s。 |
| 3 | tag | 对应性能场景tag，点击如果进入新界面，需使用WITH\_PAGE\_SWITCH（有界面切换的场景类型）。 |

**使用示例**

```screen
# 点击文本为"hello"的控件
driver.touch_perf(BY.text("hello"), tag=self.create_tag("点击hello", SceneType.NO_PAGE_SWITCH))

# 点击（100，200）的位置
driver.touch_perf(（100，200）, tag=self.create_tag("点击（100，200）", SceneType.NO_PAGE_SWITCH))

# 冷启动相机
APP_NAME="相机"
icon_pos = self.driver.find_app_in_launcher(APP_NAME)
driver.touch_perf(icon_pos, tag=self.create_tag("相机冷启动", SceneType.COLD_START))
```

**2、长按****操作**

```screen
def long_touch_perf(self, target: Union[By, UiComponent, tuple], tag: Tag = None)
```

**接口说明**

根据选定的控件或者坐标位置执行长按操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | target | 需要点击的目标，可以为控件（通过By类指定）或者屏幕坐标（通过tuple类型指定，例如（100，200）， 其中100为x轴坐标，200为y轴坐标），或者使用find\_component找到的控件对象。 |
| 2 | tag | 对应性能场景tag，点击如果进入新界面，需使用WITH\_PAGE\_SWITCH（有界面切换的场景类型）。 |

**使用示例**

```screen
# 长按相机图标，弹出弹窗
APP_NAME="相机"
icon_pos = self.driver.find_app_in_launcher(APP_NAME)
driver.long_touch_perf(icon_pos, tag=self.create_tag("长按相机图标弹出弹窗", SceneType.NO_PAGE_SWITCH))
```

**3、双击****操作**

```screen
def double_touch_perf(self, target: Union[By, UiComponent, tuple], tag: Tag = None)
```

**接口说明**

根据选定的控件或者坐标位置执行双击操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | target | 需要点击的目标，可以为控件（通过By类指定）或者屏幕坐标（通过tuple类型指定，例如（100，200）， 其中100为x轴坐标，200为y轴坐标），或者使用find\_component找到的控件对象。 |
| 2 | tag | 对应性能场景tag，点击如果进入新界面，需使用WITH\_PAGE\_SWITCH（有界面切换的场景类型）。 |

**使用示例**

```screen
# 双击确认按钮（控件文本为确认）
driver.double_touch_perf(BY.text("确认"), tag=self.create_tag("双击确认按钮", SceneType.WITH_PAGE_SWITCH))
```

**4、执行指定距离的滑动操作**

```screen
def swipe_perf(self, direction: str, distance: int = 60, start_point: tuple = None, swipe_time: float = None, tag: Tag = None)
```

**接口说明**

在屏幕上或者指定区域area中执行朝向指定方向direction的滑动操作。该接口用于执行不太精准的滑动操作。

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | direction | 滑动方向，目前支持：”LEFT” 左滑；”RIGHT” 右滑；”UP” 上滑；”DOWN” 下滑。 |
| 2 | distance | 相对滑动区域总长度的滑动距离，范围为1~100，表示滑动长度为滑动区域总长度的1%到100%， 默认为60。 |
| 3 | start\_point | 滑动起始点，默认为None，表示在区域中间位置执行滑动操作，可以传入滑动起始点坐标，支持使用(0.5, 0.5)这样的比例坐标。当同时传入side和start\_point的时候，仅start\_point生效。 |
| 4 | swipe\_time | 滑动时间（s)， 默认0.3s。 |
| 5 | tag | 对应性能场景tag，若该操作不涉及页面切换，需使用NO\_PAGE\_SWITCH。 |

**使用示例**

```screen
# 在屏幕上向上滑动40
driver.swipe_perf(UiParam.UP, distance=40, tag=self.create_tag("向上滑动", SceneType.NO_PAGE_SWITCH))

# 在屏幕上向右滑动, 滑动时间为0.1秒
driver.swipe_perf(UiParam.RIGHT, swipe_time=0.1, tag=self.create_tag("向右滑动", SceneType.NO_PAGE_SWITCH))

# 在屏幕起始点为比例坐标为(0.8, 0.8)的位置向上滑动30
driver.swipe_perf(UiParam.UP, 30, start_point=(0.8, 0.8), tag=self.create_tag("向上滑动", SceneType.NO_PAGE_SWITCH))
```

**5、执行精准的滑动操作**

```screen
def slide_perf(self, start: Union[By, tuple], end: Union[By, tuple], slide_time: float = 2, tag: Tag = None)
```

**接口说明**

根据指定的起始和结束位置执行滑动操作，起始和结束的位置可以为控件或者屏幕坐标。该接口用于执行较为精准的滑动操作。

**参数说明**

| 序列 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | start | 滑动起始位置，可以为控件BY.text("滑块")或者坐标（100，200），或者使用find\_component找到的控件对象。 |
| 2 | end | 滑动结束位置，可以为控件BY.text("最大值")或者坐标（100，200）, 或者使用find\_component找到的控件对象。 |
| 3 | slide\_time | 滑动操作总时间，单位秒。 |
| 4 | tag | 对应性能场景tag，若该操作不涉及页面切换，需使用NO\_PAGE\_SWITCH。 |

**使用示例**

```screen
# 从类型为Slider的控件滑动到文本为最大的控件
driver.slide_perf(BY.type("Slider"), BY.text("最大"),tag=self.create_tag("滑动到最大", SceneType.NO_PAGE_SWITCH))

# 从坐标100，200滑动到300，400
driver.slide_perf(（100，200）, (300, 400), tag=self.create_tag("向上滑动", SceneType.NO_PAGE_SWITCH))

# 从坐标100，200滑动到300，400, 滑动时间为3秒
driver.slide_perf(（100，200）, (300, 400), slide_time=3, tag=self.create_tag("向上滑动", SceneType.NO_PAGE_SWITCH))
```

**6、拖拽****操作**

```screen
def drag_perf(self, start: Union[By, tuple], end: Union[By, tuple],
                  area: By = None, press_time: float = 1, drag_time: float = 1, tag: Tag = None)
```

**接口说明**

根据指定的起始和结束位置执行拖拽操作，起始和结束的位置可以为控件或者屏幕坐标。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | start | 拖拽起始位置，可以为控件BY.text("滑块")或者坐标（100，200），或者使用find\_component找到的控件对象。 |
| 2 | end | 拖拽结束位置，可以为控件BY.text("最大值")或者坐标（100，200），或者使用find\_component找到的控件对象。 |
| 3 | area | 拖拽操作区域，可以为控件BY.text("画布")，或者使用find\_component找到的控件对象。目前仅在start或者end为坐标时生效，指定区域后，当start和end为坐标时，其坐标将被视为相对于指定的区域的相对位置坐标。 |
| 4 | press\_time | 拖拽操作开始时长按的时间，默认为1s（暂不支持修改）。 |
| 5 | drag\_time | 拖动的时间， 默认为1s（整个拖拽操作总时间 = press\_time + drag\_time）。 |
| 6 | tag | 对应性能场景tag，若该操作不涉及页面切换，需使用NO\_PAGE\_SWITCH。 |

**使用示例**

```screen
# 拖拽文本为"文件.txt"的控件到文本为"上传文件"的控件
driver.drag_perf(BY.text("文件.txt"), BY.text("上传文件"), tag=self.create_tag("拖拽文件", SceneType.NO_PAGE_SWITCH))

# 拖拽id为"start_bar"的控件到坐标（100，200）的位置, 拖拽时间为2秒
driver.drag_perf(BY.key("start_bar"), （100，200）, drag_time=2, tag=self.create_tag("拖拽start_bar", SceneType.NO_PAGE_SWITCH))

# 在id为"Canvas"的控件上从相对位置(10, 20)拖拽到（100，200）
driver.drag_perf((10, 20), （100，200）, area = BY.id("Canvas"), tag=self.create_tag("拖拽Canvas", SceneType.NO_PAGE_SWITCH))

# 在滑动条上从相对位置(10, 10)拖拽到(10, 200)
driver.drag_perf((10, 10), (10, 200), area=BY.type("Slider"), tag=self.create_tag("拖拽滑动条", SceneType.NO_PAGE_SWITCH))
```

**7、屏幕侧边滑动返回****操作**

```screen
def swipe_to_back_perf(self, side=UiParam.RIGHT, times: int = 1, height: float = 0.5, tag: Tag = None)
```

**接口说明**

滑动屏幕侧边返回。设备需开启触摸屏手势导航。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | side | 滑动的位置，“RIGHT“表示在右边滑动返回，“LEFT“表示在左边滑动返回。 |
| 2 | times | 滑动次数，默认1次，某些场景可能需要两次才能返回。 |
| 3 | height | 滑动位置在屏幕中Y轴的比例高度（从屏幕顶部开始计算）。 |
| 4 | tag | 对应性能场景tag，侧边返回有界面切换时，需使用WITH\_PAGE\_SWITCH。 |

**使用示例**

```screen
# 侧滑返回
self.driver.swipe_to_back_perf(tag=self.create_tag("侧滑返回", SceneType.WITH_PAGE_SWITCH))

# 侧滑2次返回
self.driver.swipe_to_back_perf(times=2, tag=self.create_tag("侧滑2次返回", SceneType.WITH_PAGE_SWITCH))

# 设置侧滑位置的高度比例为屏幕高度的80%，即在屏幕靠下的位置侧滑返回
self.driver.swipe_to_back_perf(height=0.8, tag=self.create_tag("屏幕靠下的位置侧滑返回", SceneType.WITH_PAGE_SWITCH))
```

**8、从屏幕底部上滑返回桌面**

```screen
def swipe_to_home_perf(self, times: int = 1, tag: Tag = None)
```

**接口说明**

屏幕底端上滑回到桌面，设备预置：设备开启触摸屏手势导航。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | times | 上滑次数，默认1次，某些场景可能需要两次上滑才能返回桌面。 |
| 2 | tag | 对应性能场景tag，返回桌面一般带有界面切换，需使用WITH\_PAGE\_SWITCH。 |

**使用示例**

```screen
# 上滑返回桌面
self.driver.swipe_to_home_perf(tag=self.create_tag("上滑返回桌面", SceneType.WITH_PAGE_SWITCH))

# 连续上滑2次返回桌面
self.driver.swipe_to_home_perf(times=2, tag=self.create_tag("上滑返回桌面", SceneType.WITH_PAGE_SWITCH))
```

**9、观看视频**

```screen
def watch_perf(self, watch_time, is_bullet_screen=False, is_full_screen=False, watch_tag_desc=None)
```

**接口说明**

在页面停留指定时间，进行观看视频操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | watch\_time | 观看时长，防止长时间观看行为导致视频过大，会按照30S对时长进行分割。 |
| 2 | is\_bullet\_screen | 默认False，设置为True时，对视频播放与弹幕进行卡顿检测。 |
| 3 | is\_full\_screen | 默认False，设置为True时，表示当前为全屏播放。 |
| 4 | watch\_tag\_desc | 非必填，填写后会生成步骤操作描述，对于观看时间大于30S的场景，不建议设置。 |

**使用示例**

```screen
# 观看20S视频，检测视频卡顿
self.watch_perf(20)

# 全屏观看20S视频，检测弹幕卡顿与视频卡顿
self.watch_perf(20, is_bullet_screen=True, is_full_screen=True)

# 指定操作步骤观看视频
self.watch_perf(20, watch_tag_desc="观看直播视频")
```

**10、在桌面滑动查找APP，并打开应用**

```screen
def start_application_perf(self, app_name, scene_type, tag=None)
```

**接口说明**

基于APP名称，在桌面上滑动查找指定APP，并进行点击。设备预置：需提前下载APP，并放置在桌面，不要放入文件夹中。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | app\_name | 应用名称，与桌面上显示的名称一致。 |
| 2 | scene\_type | 应用启动方式，为SceneType.COLD\_START或者SceneType.HOT\_START。 |
| 3 | tag | 非必填，如果没赋值，则会根据scene\_type自动生成。 |

**使用示例**

```screen
# 启动设置应用
self.driver.start_application_perf("设置", SceneType.COLD_START)
```

**使用示例**

```screen
# 查找需要操作的窗口
window = driver.find_window(WindowFilter().bundle_name(package_name))
# 点击窗口最小化
driver.minimize_window_perf(window, tag=self.create_tag("点击窗口最小化", 
scene_type=SceneType.WITH_PAGE_SWITCH))
```

**常用视频检测场景介绍**

**1、视频起播时延测试步骤**

```screen
# 点击视频图框播放视频
self.driver.touch_perf(BY.text("视频"), tag=self.create_tag("点击播放长视频", SceneType.PLAY_VIDEO, is_seek=False, is_short_video=True))
```

**2、视频卡顿测试步骤**

场景1：测试视频卡顿

```screen
# 观看180S视频
self.watch_perf(180)
```

场景2：测试起播时延与视频卡顿

```screen
watch_tag=self.create_tag("点击播放长视频并观看", SceneType.PLAY_VIDEO, is_seek=False, is_short_video=True)
watch_tag.watch_time=10
# 点击视频图框播放视频，并观看10S视频
self.driver.touch_perf(BY.text("视频"), tag=watch_tag)
```

## 本地脚本调试

**1、****main.py实现**

**方法一：**在main.py中修改cmd命令，将参数替换为本地调试的场景用例名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/cQWH7IRUSU65c7kA7gp-UA/zh-cn_image_0000002633533170.png "点击放大")

main.py示例

```screen
import time
from xdevice.__main__ import main_process
if __name__ == "__main__":
    try:
        pass_dict = dict()
        pass_dict['task_id'] = time.strftime('%Y%m%d%H%M%S', time.localtime())
        cmd = 'run -l OH_PerfDemoTest -ta pass_through:' + str(pass_dict)
        main_process(cmd)
        time.sleep(10)
    except Exception as e:
        print(e)
    finally:
        print("Task is End")
```

**方法二：**在main.py同级目录下，新建一个json文件，命名为action\_testsuite.json，并在main.py中修改cmd命令。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/_UzE4y-bQUaJVrtAIZiZsw/zh-cn_image_0000002633693082.png "点击放大")

action\_testsuite.json示例

```screen
{
    "description": "hypium test case",
    "environment": [
        {
            "type": "device"
        }
    ],
    "driver": {
        "type": "DeviceTest",
        "py_file": [
            "OH_PerfDemoTest.py"
        ]
    },
    "kits": [
    ]
}
```

**2、本地多用例执行方式**

一个测试任务执行多个场景用例，而不必每个场景用例单独执行，任务会按照顺序依次执行指定的场景用例。

**方法一：**在main.py 的cmd命令中指定多个case，用”;”分割。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/5GAjH-qmROijoCyPyHPy1A/zh-cn_image_0000002664012307.png "点击放大")

**方法二：**在json文件配置，并在main.py的cmd命令参数中指定json文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/KAa_b_SSQsWAThRl4OvuHA/zh-cn_image_0000002633693088.png "点击放大")

action\_testsuite.json示例

```screen
{
    "description": "hypium test case",
    "environment": [
        {
            "type": "device"
        }
    ],
    "driver": {
        "type": "DeviceTest",
        "py_file": [
            "Open_Perf_Test.py",
            "OH_PerfDemoTest.py"
        ]
    },
    "kits": [
    ]
}
```

**说明** 

**执行方式：**在工程文件中执行 main.py；

**预期结果：**设备按照脚本定义的测试步骤执行。

## **性能脚本测试执行**

性能脚本本地调试验证成功后，可在DevEco Testing创建性能测试任务，请查看文档：[场景化性能测试-任务创建](performance-testing.md#section8642101711299)。
