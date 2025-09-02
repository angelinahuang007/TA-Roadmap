# MKDOCS功能测试

记录一些案例实现方式，避免忘记。

## Code Block Test

=== "Python"

    ```python
    def prefix_sum(arr):
    prefix = [0]*(len(arr)+1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]
    return prefix
    ```
=== "C++"

    ```cpp
    #include <vector>
    using namespace std;

    vector<int> prefix_sum(vector<int>& arr) {
        vector<int> prefix(arr.size()+1, 0);
        for (int i=0; i<arr.size(); i++) {
            prefix[i+1] = prefix[i] + arr[i];
        }
        return prefix;
    }
    ```

## Drop down test
??? info "info"
    这里是隐藏的额外说明。

??? note "note"
    这里是隐藏的额外说明。

??? warning "warning"
    这里是隐藏的额外说明。

??? warning "warning+"
    这里是隐藏的额外说明。
    ??? note "note"
        ## 测试层内层
        heading测试
        ??? info "info"
            测试测试
            ### 内层内层
            heading测试2

## progress bar
学习 MkDocs: ==70%==

## keyboard hint
save： <kbd>Ctrl</kbd> + <kbd>S</kbd>

## todo
- [x] 配置 mkdocs.yml
- [ ] 部署到 GitHub Pages

## Mermaid 
```mermaid
sequenceDiagram
    User->>System: Request
    System->>User: Response