from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
        he Matrix is a 1999 science fiction action film written and directed by the Wachowskis.[a] It is the first installment in the Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. It depicts a dystopian future in which humanity is unknowingly trapped inside the Matrix, a simulated reality created by intelligent machines. Believing computer hacker Neo to be "the One" prophesied to defeat them, Morpheus recruits him into a rebellion against the machines.

        Following the success of Bound (1996), Warner Bros. gave the go-ahead for The Matrix after the Wachowskis sent an edit of the film's opening minutes. Action scenes were influenced by anime and martial arts films, particularly fight choreography and wire fu techniques from Hong Kong action cinema. Other influences include Plato's cave, 1990's Telnet hacker communities, and William Gibson's cyberpunk novel Neuromancer. The film popularized terms such as the red pill as well as a novel visual effect known as "bullet time" in which a character's heightened perception is represented by allowing the action within a shot to progress in slow motion while the camera appears to move through the scene at normal speed.

        The Matrix opened in theaters in the United States on March 31, 1999, to widespread acclaim from critics, who praised its innovative visual effects, action sequences, cinematography and entertainment value.[6][7] The film was a box office success, grossing over $460 million on a $63 million budget, becoming the highest-grossing Warner Bros. film of 1999 and the fourth-highest-grossing film of that year. The film received nominations at the 72nd Academy Awards for Best Visual Effects, Best Film Editing, Best Sound and Best Sound Effects Editing, winning all four categories. The film was also the recipient of numerous other accolades, including Best Sound and Best Special Visual Effects at the 53rd British Academy Film Awards, and the Wachowskis were awarded Best Director and Best Science Fiction Film at the 26th Saturn Awards.

        The Matrix is considered to be among the greatest science fiction films of all time,[8][9][10] and in 2012, the film was selected for preservation in the United States National Film Registry by the Library of Congress for being "culturally, historically, and aesthetically significant".[11] The film's success led to two sequels by the Wachowskis, both released in 2003, The Matrix Reloaded and The Matrix Revolutions. The Matrix franchise was further expanded through the production of comic books, video games and an animated anthology film, The Animatrix, with which the Wachowskis were heavily involved. The franchise has also inspired books and theories expanding on some of the religious and philosophical ideas alluded to in the films. A fourth film, titled The Matrix Resurrections and directed solely by Lana Wachowski, was released in 2021.
    """
    summary_template = """
        given the information {information}, about the movie The Matrix, I want to create:
        1. A shot summary of the movie
        2. 2 interesting insights
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatGroq(temperature=0, model="groq/compound")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
