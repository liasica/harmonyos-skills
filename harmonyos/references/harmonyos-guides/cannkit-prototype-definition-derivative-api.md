---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-prototype-definition-derivative-api
title: 原型定义衍生接口说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > 原型定义衍生接口说明
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:f9e1b1c0c1a3e83c3830b980283161c3ced6f1d3feb76b7ef487be1af136ae1e
---

算子原型定义的相关接口会自动生成对应的衍生接口，可用于IR模型构建。

## REG\_OP

注册算子类型后，会自动生成算子类型的两个构造函数。

例如，注册算子的类型名称Conv2D，可调用REG\_OP(Conv2D)接口，调用该接口后，定义了算子的类型名称Conv2D，同时产生Conv2D的两个构造函数，其中，**Conv2D(const AscendString& name)** 需指定算子名称，Conv2D()使用默认算子名称。

```cpp
class Conv2D : public Operator {
    typedef Conv2D _THIS_TYPE;
public:
    explicit Conv2D(const char *name);
    explicit Conv2D();
}
```

## INPUT

注册算子输入信息成功后，自动生成算子输入的相关接口，用于获取算子输入的名称、设置算子输入的对应描述等。

例如，注册算子输入x，算子输入支持的数据类型为TensorType{DT\_FLOAT}，可调用**INPUT(x, TensorType{DT\_FLOAT})** 接口，注册算子输入成功后，自动生成以下相关接口：

```cpp
static const string name_in_x(); // 返回输入的名称，即“x”
_THIS_TYPE &set_input_x(Operator& v, const string& srcName); // 指定输入x与算子对象v的输出srcName存在连接关系，返回算子对象本身
_THIS_TYPE &set_input_x_by_name(Operator& v, const char *srcName); // 指定输入x与算子对象v的输出srcName存在连接关系，返回算子对象本身
_THIS_TYPE &set_input_x(Operator &v, uint32_t index); // 指定输入x与算子对象v的索引为index的输出存在连接关系，返回算子对象本身
_THIS_TYPE &set_input_x(Operator& v); // 指定输入x与算子对象v的索引0的输出存在连接关系，返回算子对象本身
TensorDesc get_input_desc_x(); // 返回输入x对应的描述
graphStatus update_input_desc_x(const TensorDesc& tensorDesc); // 设置输入x对应的描述，包括Shape、DataType、Format等信息，graphStatus即uint32_t类型，返回非0表示出错
```

## OPTIONAL\_INPUT

注册可选算子输入信息成功后，自动生成算子输入的相关接口，用于获取算子输入的名称、设置算子输入的对应描述等。

例如，注册算子输入b，算子输入支持的数据类型为TensorType{DT\_FLOAT}，可调用**OPTIONAL\_INPUT(b, TensorType{DT\_FLOAT})** 接口，注册算子输入成功后，自动生成以下相关接口：

```cpp
static const string name_in_b(); // 返回输入的名称，即“b”
_THIS_TYPE& set_input_b(Operator& v, const string& srcName); // 指定输入b与算子对象v的输出srcName存在连接关系，返回算子对象本身
_THIS_TYPE& set_input_b_by_name(Operator& v, const char *srcName); // 指定输入b与算子对象v的输出srcName存在连接关系，返回算子对象本身
_THIS_TYPE& set_input_b(Operator& v); // 指定输入b与算子对象v的索引0的输出存在连接关系，返回算子对象本身
TensorDesc get_input_desc_b(); // 返回输入b对应的描述
graphStatus update_input_desc_b(const TensorDesc& tensorDesc); // 设置输入b对应的描述，包括Shape、DataType、Format等信息
```

## DYNAMIC\_INPUT

注册动态算子输入信息成功后，自动生成算子输入的相关接口，用于创建动态输入、设置算子输入的对应描述等。

例如，注册算子的动态输入d，算子输入支持的数据类型为TensorType{DT\_FLOAT}，可调用**DYNAMIC\_INPUT(d, TensorType{DT\_FLOAT})** 接口，注册算子的动态输入成功后，自动生成以下相关接口：

```cpp
_THIS_TYPE& create_dynamic_input_d(unsigned int num); // 创建动态输入d，包括num个输入，并且把这个输入做为算子最后的输入
_THIS_TYPE &create_dynamic_input_byindex_d(unsigned int num, size_t index) // 创建动态输入d，包括num个输入，插入到索引为index的位置，和create_dynamic_input_d不能同时使用
TensorDesc get_dynamic_input_desc_d(unsigned int index); // 返回动态输入d第index个描述，包括Shape、DataType、Format等信息
graphStatus update_dynamic_input_desc_d(unsigned int index, const TensorDesc& tensorDesc); // 更新动态输入d的第index个描述
_THIS_TYPE& set_dynamic_input_d(unsigned int dstIndex, Operator &v); // 设置输入d的第dstIndex个输入与算子对象v的索引0的输出存在连接关系，返回算子对象本身
_THIS_TYPE& set_dynamic_input_d(unsigned int dstIndex, Operator &v, const string &srcName); // 指定动态输入d的第dstIndex个输入与算子对象v的输出srcName存在连接关系，返回算子对象本身
_THIS_TYPE& set_dynamic_input_d(unsigned int dstIndex, Operator &v, const char *srcName); // 指定动态输入d的第dstIndex个输入与算子对象v的输出srcName存在连接关系，返回算子对象本身
```

## OUTPUT

注册算子输出信息成功后，自动生成算子输出的相关接口，开发者获取算子输出的名称、获取算子输出的描述、设置算子输出的描述。

例如，注册算子输出y，算子输出支持的数据类型为TensorType{DT\_FLOAT}，可调用**OUTPUT(y, TensorType{DT\_FLOAT})** 接口，注册算子输出成功后，自动生成以下相关接口：

```cpp
static const string name_out_y(); // 返回输出的名称，即“y”
TensorDesc get_output_desc_y(); // 返回输出y对应的描述
graphStatus update_output_desc_y(const TensorDesc& tensorDesc); // 设置输出y对应的描述，包括Shape、DataType、Format等信息
```

## DYNAMIC\_OUTPUT

注册动态算子输出信息成功后，自动生成动态算子输出的相关接口，包括用于创建动态输出、设置算子输出的对应描述等。

例如，注册动态算子输出d，算子输出支持的数据类型为TensorType{DT\_FLOAT}，可调用**DYNAMIC\_OUTPUT(d, TensorType{DT\_FLOAT})** 接口，注册动态算子输出成功后，自动生成以下相关接口：

```cpp
_THIS_TYPE& create_dynamic_output_d(unsigned int num); // 创建动态输出d，包括num个输出
TensorDesc get_dynamic_output_desc_d(unsigned int index); // 返回动态输出d第index个描述，包括Shape、DataType、Format等信息
graphStatus update_dynamic_output_desc_d(unsigned int index, const TensorDesc& tensorDesc); // 更新动态输出d的第index个描述
```

## REQUIRED\_ATTR

注册算子属性成功后，自动生成算子属性的3个对外接口，用于获取属性的名称、获取属性的值、设置属性的值。

例如，注册类型为int64\_t的属性mode，可调用**REQUIRED\_ATTR(mode, Int)** 接口，注册算子属性成功后，会自动生成如下接口：

```cpp
static const string name_attr_mode(); // 返回属性的名称，即“mode”
static const void name_attr_mode(AscendString &attr_name); // 出参获取属性的名称，即“mode”
OpInt get_attr_mode() const; // 返回mode属性的值，OpInt即int64_t
_THIS_TYPE& set_attr_mode(const OpInt& v); // 设置mode属性的值，返回算子对象本身
```

## ATTR

注册算子属性成功后，自动生成算子属性的3个对外接口，用于获取属性的名称、获取属性的值、设置属性的值。

下面以注册类型为int64\_t的属性、类型为int64\_t列表两种场景为例，说明所生成的算子属性接口：

* 调用ATTR(mode, Int, 1)接口，注册属性mode，属性类型为int64\_t，默认值为1。

  注册属性成功后，自动生成以下接口：

  ```cpp
  static const string name_attr_mode(); // 返回属性的名称，即“mode”
   static const void name_attr_mode(AscendString &attr_name); // 出参获取属性的名称，即“mode”
   OpInt get_attr_mode() const; // 返回mode属性的值，OpInt即int64_t
   _THIS_TYPE& set_attr_mode(const OpInt& v); // 设置mode属性的值，返回算子对象本身
  ```
* 调用ATTR(pad, ListInt, {0, 0, 0, 0})接口，注册属性pad，属性类型为int64\_t列表，默认值为{0,0,0,0}。

  注册属性成功后，自动生成以下接口：

  ```cpp
  static const string name_attr_pad(); // 返回属性的名称，即“pad”
   static const void name_attr_pad(AscendString &attr_name); // 出参获取属性的名称，即“pad”
   OpListInt get_attr_pad() const; // 返回属性pad的值，OpListInt即vector<int64_t> 
   _THIS_TYPE& set_attr_pad(const OpListInt& v); // 设置属性pad的值，返回算子对象本身
  ```

下面以注册类型为string属性场景为例，说明所生成的算子属性接口：

调用ATTR(data\_format, String, "NHWC")接口，注册属性data\_format，属性类型为string。

```cpp
static const string name_attr_data_format(); // 返回属性的名称，即“data_format”
static const void name_attr_data_format(AscendString &attr_name); // 出参获取属性的名称，即“data_format”
OpString get_attr_data_format() const; // 返回data_format属性的值，OpString即string
graphStatus get_attr_data_format(AscendString &val); // 出参返回data_format属性的值
_THIS_TYPE& set_attr_data_format(const string& v); // 设置data_format属性的值，返回算子对象本身
_THIS_TYPE& set_attr_data_format(const char* v); // 设置data_format属性的值，返回算子对象本身
```

## GRAPH

注册算子子图信息成功后，自动生成算子子图的相关接口，开发者获取算子子图的名称、获取算子子图的描述、设置算子子图的描述。

例如，注册算子子图y，可调用**GRAPH(y)** 接口，注册算子子图成功后，自动生成以下相关接口：

```cpp
static const string name_graph_y(); // 返回算子子图的名称，即“y”
SubgraphBuilder get_subgraph_builder_y() const; // 返回子图y对应的构建函数对象
_THIS_TYPE &set_subgraph_builder_y(const SubgraphBuilder &v); // 设置子图y对应的构建函数对象
Graph get_subgraph_y() const; // 获取子图y对应的graph对象
```

## DYNAMIC\_GRAPH

注册动态算子子图信息成功后，自动生成动态算子子图的相关接口，包括用于创建动态子图、设置算子子图的对应描述等。

例如，注册动态算子子图branches，可调用**DYNAMIC\_GRAPH(branches)** 接口，注册动态算子子图成功后，自动生成以下相关接口：

```cpp
_THIS_TYPE& create_dynamic_subgraph_branches(unsigned int num); // 创建动态子图branches，包括num个子图
SubgraphBuilder get_dynamic_subgraph_builder_branches(unsigned int index); // 返回动态输子图第index个子图构建函数对象
Graph get_dynamic_subgraph_branches(unsigned int index); // 返回动态输子图第index个子图对象
_THIS_TYPE &set_dynamic_subgraph_builder_branches(unsigned int index,const SubgraphBuilder &v); // 设置动态子图branches的第index个子图构建函数对象
```
