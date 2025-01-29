from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.6)

def generate(cuisine):
    """Generate a restaurant name and menu items based on cuisine type."""
    
    # Prompt templates for restaurant name and menu items
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this, only one name."
    )

    prompt_template_item = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}. Return a comma-separated list."
    )

    # Define the LLM chains
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    item_chain = LLMChain(llm=llm, prompt=prompt_template_item, output_key="menu_items")

    # Create a sequential chain
    chain = SequentialChain(
        chains=[name_chain, item_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )

    # Invoke the chain
    response = chain.invoke({"cuisine": cuisine})

    return response

# Test the function
if __name__ == "__main__":
    print(generate("American"))
