#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> edges(m, std::vector<int>(3));
    for (int i = 0; i < m; ++i) {
        std::cin >> edges[i][1] >> edges[i][2] >> edges[i][0];
        edges[i][1]--;
        edges[i][2]--;
    }
    std::sort(edges.begin(), edges.end());

    std::vector<int> comp(n);
    for (int i = 0; i < n; ++i)
        comp[i] = i;

    int ans = 0;
    for (auto &edge : edges) {
        int weight = edge[0];
        int start = edge[1];
        int end = edge[2];
        if (comp[start] != comp[end]) {
            ans += weight;
            int a = comp[start];
            int b = comp[end];
            for (int i = 0; i < n; ++i)
                if (comp[i] == b)
                    comp[i] = a;
        }
    }
    std::cout << ans << std::endl;
}
