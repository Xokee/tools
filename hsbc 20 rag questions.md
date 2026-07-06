# 20 English Graph RAG Test Questions Focused on HSBC, Investment Products, HK & US Stock Trading
All questions support **multi-hop graph reasoning**, covering HSBC group structure, wealth management products, cross-border stock brokerage, fund allocation, equity holding relationships, supply chain & client links, suitable for Graph RAG multi-path retrieval benchmark testing. Difficulty tiered: 2-hop (8), 3-hop (7), 4-hop complex (5). Each labeled reasoning hops, graph relations & test capability.

## Part 1: Basic 2-Hop Retrieval Questions (8 items)
1. Which HSBC wealth management unit provides US stock trading services for Hong Kong retail clients, and what low-cost index ETF products does this division launch?
    - Hops: 2 | Graph Relations: HSBC Subsidiary - Service Scope, Subsidiary - Investment Products
    - Test: Department-service-product two-layer entity association
2. Among HSBC’s listed equity funds focused on Hong Kong market, which funds hold large-cap HK financial stocks as core underlying assets?
    - Hops: 2 | Graph Relations: HSBC Fund - Underlying Assets, Fund - HK Stock Sector Exposure
    - Test: Fund-asset sector cross matching
3. HSBC Global Private Banking serves many US-listed Chinese concept firms; what structured investment products are customized for these corporate clients?
    - Hops: 2 | Graph Relations: HSBC Business Line - Target Client, Business Line - Customized Investment Products
    - Test: Client group and product mapping retrieval
4. Which HSBC brokerage platforms support simultaneous HKEX and NYSE stock trading, and what currency margin financing tools do these platforms offer?
    - Hops: 2 | Graph Relations: Trading Platform - Supported Markets, Platform - Margin Financing Tools
    - Test: Trading channel + financial instrument dual relation query
5. HSBC issues RMB-denominated wealth products linked to US tech stock indices; which top US tech constituent stocks are embedded in these linked notes?
    - Hops: 2 | Graph Relations: Structured Note - Underlying Index, Index - Constituent US Stocks
    - Test: Derivative product to underlying stock entity tracing
6. HSBC Asset Management runs multiple HK equity mutual funds; which offshore fund distributors cooperate with HSBC to sell these Hong Kong stock funds to Asian investors?
    - Hops: 2 | Graph Relations: Fund Issuer - Distribution Partners, Fund - HK Stock Exposure
    - Test: Issuer-distributor business chain retrieval
7. HSBC’s Hong Kong retail banking division provides cross-border stock investment accounts; what HSBC foreign exchange products help clients convert HKD to USD for US stock purchases?
    - Hops: 2 | Graph Relations: Stock Account Service - FX Demand, HSBC FX Product - Currency Conversion Function
    - Test: Cross-service scenario association reasoning
8. HSBC has strategic shareholdings in several Asian securities firms; which of these invested brokers offer zero-commission US stock trading for individual users?
    - Hops: 2 | Graph Relations: HSBC - Invested Brokerages, Brokerage - US Stock Trading Policy
    - Test: Equity investment + business feature two-hop screening

## Part 2: Medium 3-Hop Retrieval Questions (7 items, mainstream test difficulty)
9. HSBC Global Asset Management manages a US semiconductor equity fund, whose top 10 holdings include US-listed chip firms; which HSBC structured deposit products are linked to the performance of these semiconductor stocks?
    - Hops: 3 | Path: HSBC AM → US Semiconductor Fund → Chip Stock Holdings; HSBC Retail → Linked Structured Deposits
    - Test: Cross HSBC department multi-path merging & asset linkage
10. HSBC Hong Kong’s stock brokerage arm partners with US prime brokers for US stock settlement; which HSBC money market funds can be used as collateral for US stock margin loans via this partnership?
    - Hops: 3 | Path: HSBC HK Broker → US Prime Broker Partner; Broker Margin Service → Eligible Collateral Funds; Collateral Funds - HSBC Money Market Series
    - Test: Cross-border cooperation + financing collateral triple-layer reasoning
11. The HSBC Global Equity Income Fund heavily allocates high-dividend Hong Kong blue chips; which HSBC private banking portfolio allocation strategies combine this fund with US dividend ETFs for cross-region income investment?
    - Hops: 3 | Path: HSBC Fund → HK Dividend Stock Holdings; HSBC PB → Client Portfolio Strategies; Strategies → Mixed HK & US Income Assets
    - Test: Fund underlying + wealth allocation strategy multi-node filtering
12. HSBC owns a stake in a Hong Kong listed securities company that provides HK & US stock margin trading; which offshore bond products issued by HSBC can be used to offset margin interest fees for clients of this securities firm?
    - Hops: 3 | Path: HSBC Equity Investment → HK Listed Broker; Broker → Margin Trading Service; HSBC Fixed Income Products → Margin Interest Rebate Function
    - Test: Equity holding, trading service, value-added product three-hop chain
13. HSBC launched cross-border stock investment plans for Mainland China investors via Hong Kong; which US-listed Chinese concept stocks are prioritized in these plans, and which HSBC currency hedging tools reduce USD exchange risks for these holdings?
    - Hops: 3 | Path: HSBC Cross-border Scheme → Target US Chinese Stocks; Stock Holding → FX Risk Demand; HSBC Tools → Currency Hedging Function
    - Test: Policy investment scheme + underlying stock + risk hedging composite retrieval
14. HSBC’s US wealth subsidiary issues index-linked notes tracking NASDAQ 100; which HSBC HK discretionary portfolio management services allocate these notes alongside Hong Kong technology stocks for balanced growth exposure?
    - Hops: 3 | Path: HSBC US Subsidiary → NASDAQ Linked Notes; HSBC HK Wealth → Discretionary Portfolios; Portfolios → Mixed HK Tech & US Index Assets
    - Test: Cross-regional subsidiary product combination reasoning
15. Institutional clients using HSBC prime brokerage for HK stock block trading can access HSBC securities lending services; which US stock ETFs managed by HSBC AM are available for securities lending via the same prime brokerage channel?
    - Hops: 3 | Path: HSBC Prime Broker → HK Block Trading Clients; Broker Channel → Securities Lending Service; Lending Pool → HSBC-managed US ETFs
    - Test: Institutional service channel cross-asset screening

## Part 3: High Complexity 4-Hop Retrieval Questions (5 items, distinguish Graph RAG from vanilla vector RAG)
16. Two core HSBC HK funds focusing on Hong Kong financial blue chips share the same underlying banking stocks; the asset management team running these funds also manages US financial sector ETFs, and which HSBC structured capital protected products tie returns to the combined performance of both HK bank stocks and US financial ETFs?
    - Hops: 4 | Path: Dual HSBC HK Funds → Shared HK Bank Underlyings; Fund Team → US Financial ETF Lineup; HSBC Retail Division → Capital Protected Structured Products; Products Linked to HK + US Financial Assets
    - Test: Multiple fund entity merging + cross-region asset + derivative product long-chain reasoning
17. HSBC holds minority equity in a Hong Kong brokerage offering fractional US stock trading; this brokerage’s clearing partner is a US prime broker, and the prime broker cooperates with HSBC’s global asset management division to launch multi-asset portfolios combining fractional US stocks and Hong Kong small-cap equities, what HSBC short-term liquidity funds serve as cash allocation tools within these cross-border portfolios?
    - Hops: 4 | Path: HSBC Equity Stake → HK Fractional Stock Broker; Broker → US Clearing Prime Broker; Prime Broker + HSBC AM → Cross-Border Mixed Portfolios; Portfolios Supporting HSBC Liquidity Funds
    - Test: Multi-layer equity investment, cross-border cooperation, portfolio construction, cash tool four-hop trace
18. HSBC’s cross-border wealth scheme for Greater China investors prioritizes US-listed AI Chinese concept stocks; these US stocks are included in HSBC global equity funds, and the fund’s risk hedging relies on HSBC FX forward contracts, which HSBC private banking customized allocation models integrate the AI stocks, equity funds and FX hedging contracts together for high-net-worth clients?
    - Hops: 4 | Path: HSBC Greater China Scheme → US AI Concept Stocks; Stocks → HSBC Global Equity Funds; Funds Risk Control → HSBC FX Forward Products; HSBC PB → Custom Multi-Asset Allocation Models
    - Test: Investment scheme, underlying stocks, hedging derivatives, wealth model full-length reasoning
19. HSBC Global Private Banking serves US-listed multinational enterprise clients; these corporates hold large positions in Hong Kong listed suppliers via HSBC stock custody, HSBC’s corporate treasury team provides USD-HKD swap products for these cross-border equity holdings, and which HSBC multi-currency income funds are recommended by treasury advisors alongside the swap tools for corporate excess capital allocation?
    - Hops: 4 | Path: HSBC PB → Multinational US-listed Clients; Clients Custody → HK Supplier Stocks; HSBC Treasury → Cross-Currency Swap Products; Treasury Advisory → Matching Multi-Currency Income Funds
    - Test: Corporate client, cross-market stock custody, FX derivatives, corporate fund allocation complex graph path
20. HSBC’s Hong Kong retail trading platform supports both HKEX and NYSE stock purchases, clients investing in US semiconductor stocks via this platform face USD exchange fluctuation risks, HSBC issues currency-linked deposits to hedge USD exposure, and which HSBC thematic tech funds combine these currency deposits with Hong Kong semiconductor stocks as a packaged retail investment solution?
    - Hops: 4 | Path: HSBC HK Trading Platform → US Semiconductor Stock Trades; US Stock Holdings → USD FX Risk; HSBC Retail → Currency Linked Deposit Hedging Tools; HSBC Thematic Funds → Packaged HK + US Tech + FX Hedge Portfolios
    - Test: Trading channel, underlying US stocks, hedging deposits, packaged fund product four-layer serial retrieval

## Graph RAG Benchmark Usage Notes
1. Core Graph Nodes: HSBC group subsidiaries, regional business divisions, investment funds, structured products, HKEX/NYSE listed stocks, broker partners, prime brokers, HNW/institutional/retail clients, FX hedging instruments
2. Core Graph Edges: Owns equity stake in, provides trading service for, underlying asset of, distributes product, cooperates with, hedges risk for, allocates within portfolio, supports as collateral
3. Evaluation Metrics: Multi-hop path completeness, cross-department entity linking accuracy, cross-market asset relation recall, hallucination suppression for cross-border financial logic
