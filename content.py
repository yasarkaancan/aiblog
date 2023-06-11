import os, datetime, openai

openai.api_key = "YOUR_API_KEY_HERE"

print("How many blogs shall I write ?")
blog_count = int(input())
total_blog = blog_count

print("What should the blogs be about ?(empty for random)")
about = input()

if about == "":
    about = "random topic"

print("Do you want to push the changes to github ? (y/n)")
push = input()

for i in range(blog_count):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Metadata:\ntitle: Specifies the title of the blog post.\ndescription: Provides a brief description of the blog post.\nHeadings:\n##: Represents a level 2 heading.\n###: Represents a level 3 heading.\n####: Represents a level 4 heading.\nQuoted text:\n>: Indicates a quoted text or blockquote.\nCode blocks:\nhtml ... : Encloses an HTML code block.\njs ... : Encloses a JavaScript code block.\nInline code:\nEnclosing backticks (`) around inline code snippets.\nLinks:\n[text](URL): Formats a hyperlink with the specified text and URL.\nLists:\n-: Represents an unordered list item.\n1., 2., 3.: Represents ordered list items.\nNested lists are also used with indentation.\nText formatting:\n**text**: Makes the enclosed text bold.\n_text_: Makes the enclosed text italic.\nImages:\n<Image src=\"/blog-post-4.jpg\" width=\"718\" height=\"404\" alt=\"Image\" />: Represents an image with the specified source, width, height, and alt attribute.\nTables:\n|: Separates table cells.\nRows starting and ending with | represent table rows.\nClosing paragraph or statement.\n\nCreate me a blog page in mdx format that is about {about} with the syntax given above, when specifying metadata start with --- and close with ---. Do not quote or write anything else another than title & description. Include a blank before title and description.",
    temperature=1,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    if response.choices[0].text == "":
        print("No response from the AI, please trying again !")
    else:
        prompt = response.choices[0].text


        prompt = prompt.split("\n")
        prompt.insert(5, f"date: '{datetime.datetime.now().strftime('%Y-%m-%d')}'")
        prompt = "\n".join(prompt)


        title = prompt.split("---")[1].split("title:")[1].split("description")[0].strip().replace(" ", "-").lower()
        title = "".join([i for i in title if i.isalpha() or i == "-"])
        
        prompt = prompt.split("\n")
        prompt = prompt[2:]
        prompt = "\n".join(prompt)
        
        path = os.path.join("content", "posts") + f"/{title}" + ".mdx"

        with open(path, "w") as f:
            f.write(prompt)
        blog_count -= 1
        print(f"#{i+1} {title}")

if push == "y":
    os.system("git pull origin main")
    os.system("git add .")
    os.system(f"git commit -m \"Added {total_blog} new blogs\"")
    os.system("git push origin main")
    print("Changes pushed to github successfully !")
    
print("Done !")
