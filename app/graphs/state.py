from typing import TypedDict, List, Dict, Any


class StockAgentState(TypedDict):

    user_query: str

    symbol: str

    stock_data: Dict[str, Any]

    indicators: Dict[str, Any]

    news: List[Dict]

    sentiment: str

    recommendation: str

    reasoning: List[str]

    final_answer: str