# Houdini

houdini是个很强大的3D软件，可以想为3D的IDE

分为六个核心部分：

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
