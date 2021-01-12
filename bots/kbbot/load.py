from .kb import KB, Boolean, Integer

# Initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
# Play ACE strategy KB
A0 = Boolean('a0')
A1 = Boolean('a1')
A2 = Boolean('a2')
A3 = Boolean('a3')
A4 = Boolean('a4')
A5 = Boolean('a5')
A6 = Boolean('a6')
A7 = Boolean('a7')
A8 = Boolean('a8')
A9 = Boolean('a9')
A10 = Boolean('a10')
A11 = Boolean('a11')
A12 = Boolean('a12')
A13 = Boolean('a13')
A14 = Boolean('a14')
A15 = Boolean('a15')
A16 = Boolean('a16')
A17 = Boolean('a17')
A18 = Boolean('a18')
A19 = Boolean('a19')
PA0 = Boolean('pa0')
PA1 = Boolean('pa1')
PA2 = Boolean('pa2')
PA3 = Boolean('pa3')
PA4 = Boolean('pa4')
PA5 = Boolean('pa5')
PA6 = Boolean('pa6')
PA7 = Boolean('pa7')
PA8 = Boolean('pa8')
PA9 = Boolean('pa9')
PA10 = Boolean('pa10')
PA11 = Boolean('pa11')
PA12 = Boolean('pa12')
PA13 = Boolean('pa13')
PA14 = Boolean('pa14')
PA15 = Boolean('pa15')
PA16 = Boolean('pa16')
PA17 = Boolean('pa17')
PA18 = Boolean('pa18')
PA19 = Boolean('pa19')
# PLAY 10 KB Strategy
T0 = Boolean('a0')
T1 = Boolean('a1')
T2 = Boolean('a2')
T3 = Boolean('a3')
T4 = Boolean('t4')
T5 = Boolean('t5')
T6 = Boolean('t6')
T7 = Boolean('t7')
T8 = Boolean('t8')
T9 = Boolean('t9')
T10 = Boolean('t10')
T11 = Boolean('t11')
T12 = Boolean('t12')
T13 = Boolean('t13')
T14 = Boolean('t14')
T15 = Boolean('t15')
T16 = Boolean('t16')
T17 = Boolean('t17')
T18 = Boolean('t18')
T19 = Boolean('t19')
PT0 = Boolean('pt0')
PT1 = Boolean('pt1')
PT2 = Boolean('pt2')
PT3 = Boolean('pt3')
PT4 = Boolean('pt4')
PT5 = Boolean('pt5')
PT6 = Boolean('pt6')
PT7 = Boolean('pt7')
PT8 = Boolean('pt8')
PT9 = Boolean('pt9')
PT10 = Boolean('pt10')
PT11 = Boolean('pt11')
PT12 = Boolean('pt12')
PT13 = Boolean('pt13')
PT14 = Boolean('pt14')
PT15 = Boolean('pt15')
PT16 = Boolean('pt16')
PT17 = Boolean('pt17')
PT18 = Boolean('pt18')
PT19 = Boolean('pt19')


def general_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    # This adds information which cards are ACES
    kb.add_clause(A0)
    kb.add_clause(A5)
    kb.add_clause(A10)
    kb.add_clause(A15)
    # This adds information which cards are TENS
    kb.add_clause(T1)
    kb.add_clause(T6)
    kb.add_clause(T11)
    kb.add_clause(T16)


def strategy_knowledge(kb):
    # DEFINITION OF THE STRATEGY
    # Add clauses (This list is sufficient for this strategy)
    # PA is the strategy to play ace first, so all we need to model is all x PA(x) <-> A(x),
    # In other words that the PA strategy should play a card when it is a ace
    kb.add_clause(~A0, PA0)
    kb.add_clause(~A5, PA5)
    kb.add_clause(~A10, PA10)
    kb.add_clause(~A15, PA15)
    kb.add_clause(~PA0, A0)
    kb.add_clause(~PA5, A5)
    kb.add_clause(~PA10, A10)
    kb.add_clause(~PA15, A15)
    # Play ten first
    kb.add_clause(~T1, PT1)
    kb.add_clause(~T6, PT6)
    kb.add_clause(~T11, PT11)
    kb.add_clause(~T16, PT16)
    kb.add_clause(~PT1, T1)
    kb.add_clause(~PT6, T6)
    kb.add_clause(~PT11, T11)
    kb.add_clause(~PT16, T16)
