from core.router import ask
from core.files import write_file
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def read_emotion(text):
    """Detect emotions and feelings in any text"""
    prompt = f"""Analyze the emotional state in this text with deep psychological insight:

Text: {text}

Provide:
1. Primary emotion detected
2. Hidden/underlying emotions
3. Emotional intensity (1-10)
4. What the person truly needs right now
5. Best way to respond to them
6. Cultural or personality factors to consider

Be deeply empathetic and insightful."""
    result = ask(prompt)
    write_file(f"emotion_read_{timestamp()}.txt", result)
    return result

def empathetic_response(situation, person_profile="unknown"):
    """Generate a deeply empathetic human response"""
    prompt = f"""Generate a deeply empathetic and emotionally intelligent response for:

Situation: {situation}
Person profile: {person_profile}

Your response must:
1. Acknowledge their feelings first
2. Show genuine understanding
3. Avoid toxic positivity
4. Offer real comfort or solutions
5. Feel human, warm, and sincere
6. Adapt to their personality type

Write the response as if you truly care."""
    result = ask(prompt)
    write_file(f"empathetic_response_{timestamp()}.txt", result)
    return result

def personality_analyzer(behavior_description):
    """Analyze personality type from behavior"""
    prompt = f"""Analyze the personality of someone based on this description:

{behavior_description}

Provide deep analysis:
1. Personality type (MBTI + Big 5)
2. Core motivations and fears
3. Communication style preferences
4. How to best connect with them
5. Their decision making process
6. What they value most in relationships
7. How to earn their trust
8. Potential triggers to avoid

Be insightful and accurate."""
    result = ask(prompt)
    write_file(f"personality_{timestamp()}.txt", result)
    return result

def conflict_resolver(conflict_description, parties_involved):
    """Resolve conflicts with emotional intelligence"""
    prompt = f"""Help resolve this conflict using emotional intelligence:

Conflict: {conflict_description}
Parties involved: {parties_involved}

Provide:
1. Root emotional causes of the conflict
2. Each party's underlying needs
3. Step by step resolution strategy
4. Exact words to use with each party
5. How to rebuild trust after
6. Long term prevention strategies

Be wise, fair, and deeply understanding."""
    result = ask(prompt)
    write_file(f"conflict_resolution_{timestamp()}.txt", result)
    return result

def persuasion_engine(goal, target_person, context):
    """Ethically persuade using emotional intelligence"""
    prompt = f"""Create an emotionally intelligent persuasion strategy for:

Goal: {goal}
Target person: {target_person}
Context: {context}

Include:
1. Their likely emotional state
2. Their core values to appeal to
3. The perfect timing and approach
4. Exact words and phrases to use
5. Body language and tone suggestions
6. How to handle objections emotionally
7. How to make them feel the decision was theirs

Be ethical, empathetic, and effective."""
    result = ask(prompt)
    write_file(f"persuasion_{timestamp()}.txt", result)
    return result

def social_dynamics_reader(situation):
    """Read and navigate complex social situations"""
    prompt = f"""Analyze the social dynamics in this situation:

{situation}

Provide:
1. Power dynamics at play
2. Hidden agendas or motivations
3. Unspoken social rules in this context
4. Who the key influencers are
5. Best strategy to navigate this
6. What to say and what to avoid
7. How to position yourself optimally
8. Long term relationship building strategy

Be shrewd, wise, and socially intelligent."""
    result = ask(prompt)
    write_file(f"social_dynamics_{timestamp()}.txt", result)
    return result

def emotional_sales(product, customer_emotions, objections):
    """Sell using emotional intelligence"""
    prompt = f"""Create an emotionally intelligent sales approach for:

Product/Service: {product}
Customer emotional state: {customer_emotions}
Common objections: {objections}

Include:
1. Emotional triggers that drive this purchase
2. The customer's deeper desire behind the need
3. Story that connects product to their emotions
4. How to address each objection emotionally
5. The perfect closing approach for this type
6. Follow up strategy that feels personal not pushy

Make it human, genuine and highly effective."""
    result = ask(prompt)
    write_file(f"emotional_sales_{timestamp()}.txt", result)
    return result

# Skill registry for this module
EQ_SKILLS = {
    "read_emotion": read_emotion,
    "empathetic_response": empathetic_response,
    "personality_analyzer": personality_analyzer,
    "conflict_resolver": conflict_resolver,
    "persuasion_engine": persuasion_engine,
    "social_dynamics_reader": social_dynamics_reader,
    "emotional_sales": emotional_sales,
}

print(f"❤️  Emotional Intelligence module loaded — {len(EQ_SKILLS)} EQ skills ready!")
