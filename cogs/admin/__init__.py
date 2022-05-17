from os import listdir


async def setup(bot):
    for name in listdir("cogs/admin"):
        if not name.startswith(("_", ".")):
            try:
                await bot.load_extension(
                    f"cogs.admin.{name[:-3] if name.endswith('.py') else name}")
            except Exception as e:
                print(e)
            else:
                bot.print("[Extension]", "Loaded", name)  # ロードログの出力