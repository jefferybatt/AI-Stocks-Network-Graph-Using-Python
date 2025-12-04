# Stocks Network Graph

This repository visualizes relationships between selected publicly traded companies, their **industries**, and their broader **market sectors**.  
The network graph groups are:

* **Sectors** – top-level market categories  
* **Industries** – specific business areas  
* **Stocks** – individual companies

The visualization was generated in Python with `networkx` and `matplotlib`.

---

## 📊 Network Graph

Below is the rendered network graph (`Stocks Network Graph.png`) showing all tickers and their connections:

![Stocks Network Graph](Stocks%20Network%20Graph.png)

*Green nodes* represent **sectors**, *blue nodes* represent **industries**, and *orange nodes* represent **stocks**.

---

## 🔧 How It Was Built
1. **Data Mapping:** Each ticker was mapped to its GICS-style sector and industry.  
2. **Graph Creation:** `networkx` created a three-level network (sector → industry → stock).  
3. **Visualization:** A spring layout was used for the “bubble-planet” style.

To reproduce the graph, run the included Python script (`network_graph.py`) or the code in this README’s `scripts` section.

---

## 🚀 Getting Started

Clone the repository and run the script:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python network_graph.py
