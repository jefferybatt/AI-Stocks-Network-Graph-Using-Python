# Full, runnable Python code to recreate the bubble-planet style network graph
# (including standardized sector/industry mapping.
# Requires: networkx, matplotlib

import networkx as nx
import matplotlib.pyplot as plt

# --- Standardized sector/industry mapping (GICS-style labels) ---
stocks_info = {
    # Information Technology
    "NVDA": {"industry": "Semiconductors", "sector": "Information Technology"},
    "AMD":  {"industry": "Semiconductors", "sector": "Information Technology"},
    "TSM":  {"industry": "Semiconductors", "sector": "Information Technology"},
    "ASML": {"industry": "Semiconductor Equipment & Materials", "sector": "Information Technology"},
    "PLTR": {"industry": "Application Software", "sector": "Information Technology"},
    "SHOP": {"industry": "Application Software", "sector": "Information Technology"},
    "ONDS": {"industry": "Wireless Communications Equipment", "sector": "Information Technology"},
    "BBAI": {"industry": "Artificial Intelligence & Analytics", "sector": "Information Technology"},

    # Consumer Discretionary
    "AMZN": {"industry": "Internet & Direct Marketing Retail", "sector": "Consumer Discretionary"},
    "TSLA": {"industry": "Automobiles", "sector": "Consumer Discretionary"},

    # Utilities
    "CEG": {"industry": "Electric Utilities", "sector": "Utilities"},
    "VST": {"industry": "Independent Power Producers & Energy Traders", "sector": "Utilities"},
    "SMR": {"industry": "Independent Power Producers (Nuclear)", "sector": "Utilities"},

    # Health Care
    "TGEN": {"industry": "Biotechnology", "sector": "Health Care"},
}

# --- Build the graph: sectors ↔ industries ↔ stocks ---
G = nx.Graph()
for ticker, info in stocks_info.items():
    sector = info["sector"]
    industry = info["industry"]

    # Add typed nodes
    G.add_node(sector, type="sector")
    G.add_node(industry, type="industry")
    G.add_node(ticker, type="stock")

    # Connect the hierarchy
    G.add_edge(industry, sector)
    G.add_edge(ticker, industry)

# --- Layout: spring for "bubble planet" feel ---
pos = nx.spring_layout(G, k=0.5, iterations=100, seed=42)

# --- Partition nodes by type ---
sectors = [n for n, d in G.nodes(data=True) if d["type"] == "sector"]
industries = [n for n, d in G.nodes(data=True) if d["type"] == "industry"]
stocks = [n for n, d in G.nodes(data=True) if d["type"] == "stock"]

# --- Draw ---
plt.figure(figsize=(18, 13))

# Nodes (colored bubbles)
nx.draw_networkx_nodes(G, pos, nodelist=sectors, node_color="lightgreen", node_size=1800, label="Sectors", alpha=0.9)
nx.draw_networkx_nodes(G, pos, nodelist=industries, node_color="skyblue", node_size=1400, label="Industries", alpha=0.9)
nx.draw_networkx_nodes(G, pos, nodelist=stocks, node_color="orange", node_size=1000, label="Stocks", alpha=0.9)

# Edges
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.6)

# Labels
nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")

plt.title("Bubble-Planet Style Network Graph (Sectors → Industries → Stocks)", fontsize=18)
plt.legend(scatterpoints=1)
plt.axis("off")
plt.tight_layout()

# --- Optional: save files ---
# png_path = "bubble_planet_network.png"
# svg_path = "bubble_planet_network.svg"
# plt.savefig(png_path, dpi=200, bbox_inches="tight")
# plt.savefig(svg_path, bbox_inches="tight")

plt.show()
