# 程序化生成 (Procedural Generation)

程序化生成是技术美术的重要技能之一，主要涉及使用算法和参数化方法自动创建内容。Houdini是这一领域的核心工具。

## Houdini 核心技能

Houdini是一个强大的3D软件，可以视为3D的IDE，分为六个核心部分：

### 建模

- 基于SOP节点，程序化几何
- poly、VDB、曲线、布尔
- procedural制作HDA

用节点快速搭建复杂模型，熟悉VDB、布尔、Copy to Points、Attribute Wrangle等常用工具、做可复用的程序化资产

### 程序化动画

- Attribute驱动的动画
- Point VOP/VEX
- CHOPs
- MotionFX

用VEX/Arrtibute做动态变化，会基于属性做动画控制，理解CHOPs逻辑

### 特效模拟

- 粒子（POP）
- 流体（FLIP）
- 烟雾火焰（Pyro）
- 刚体/软体（RBD/Vellum）
- 海洋（Ocean）

做主流的特效模拟（爆炸、烟雾、流体），会调解算速递、缓存、碰撞、碰撞代理，能对接渲染和后期

### 渲染

- Mantra
- Karma
- Redshit、Arnold、Octane
- 材质/贴图（SHOPs/MaterialX）

会材质网格、贴图投射，输出多通道AOV，会设置灯光、渲染参数

### 程序化资产与HDA开发

- 创建可复用数字资产
- 参数化工具
- Houdini Engine对接Unity/UE
- pipeline集成（USD）

会打包HDA并发布给团队使用，熟悉参数、接口，能对接其他DCC软件

### 编程与脚本

- VEX（高性能表达式）
- Python（脚本、自动化）
- HOM（Houdini Object Model）
- TOPs（任务调度）

用VEX操作几何/例子熟悉，用python写工具或批处理，熟悉HOM API

## VEX 编程

VEX是Houdini中的高性能表达式语言，是程序化生成的核心。

### Joy of VEX 学习路径

参考资源：[Joy of Vex](https://www.tokeru.com/cgwiki/JoyOfVex.html)

#### VEX基础 (d1-d5)

基础syntax，@Cd、@Time、attributes、arithmetic、ramps & modulo

学完能做：学会简单的@Cd动画，用Ramp和Clamp做渐变，学会波形动画

#### 几何操作 & 流程控制 (d6-d14)

多输入wrangle、噪声和矢量运算、条件判断、数组和循环、动态生成/删除集合体

学完能做：用噪声做复杂随机效果，写条件逻辑判断，创建点/面

#### 实例化 & 更多数据操作 (d15-d20)

Copy SOP、四元数旋转、Intrinsics、Primuv/xyzdist查询、点云过滤

学完能做：控制实例化方向、缩放、旋转，进行几何查询，用点云做平滑/混合

### 20天学完后能：

- 做大部分日常需要的VEX脚本
- 控制属性随机、动画、渐变
- 进行噪声/波形/clamp/ramp映射
- 写循环、条件判断、数组逻辑
- 生成和删除几何体
- 实例化控制：随机缩放、方向旋转（四元数）
- 查询几何（primuv、xyzdist、nearpoints）
- 用点云实现平滑和过滤

## 学习资源

- [Joy of Vex](https://www.tokeru.com/cgwiki/JoyOfVex.html) - VEX编程教程
- Houdini官方文档
- SideFX官方教程
- 社区论坛和教程

## 实践项目

1. 创建程序化建筑生成器
2. 开发地形生成工具
3. 制作程序化植被系统
4. 构建粒子特效系统
5. 开发HDA资产库 