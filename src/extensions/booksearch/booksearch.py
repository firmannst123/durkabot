from discord.ext import commands

from extensions.booksearch.booksite import BookSite


class BookSearch:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def booksearch(self, ctx, book_site: BookSite, *, query: str):
        """
        Search for a book in the given library

        To see currently supported libraries, run the `booksearch libraries` command.

        Args:
            book_site: Name of library as returned in `booksearch libraries`
            query: Search query for the book

        Returns:
            Search results with direct links and links on library site
        """
        embed = await book_site.search(query)
        await ctx.send(embed=embed)

    @booksearch.command()
    async def libraries(self, ctx):
        """
        Returns list of currently supported libraries in no particular order
        """
        libraries = str(BookSite.libraries()).strip('{}').replace("'", '')
        await ctx.send(f'Supported libraries are: ```\n{libraries}```')
