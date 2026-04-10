import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Ton token (on va le cacher après)
# Au lieu de :
# Au lieu de :
TOKEN = "t.me/joyzet_bot"

# Mets :
TOKEN = os.environ.get("https://core.telegram.org/bots/api")

# Commande /start
async def start(update: Update, context):
    await update.message.reply_text(
        "🔥 BIENVENUE SUR MINI ZETSU  ! 🔥\n\n"
        "🎬 Le réseau social de partage vidéo\n\n"
        "📱 Commandes disponibles :\n"
        "/joy - Présentation de l'app\n"
        "/info - Infos sur JOY PURGE\n"
        "/contact - Nous contacter\n"
        "/aide - Toutes les commandes\n\n"
        "✨ Bientôt disponible sur iOS et Android !"
    )

# Commande /joy
async def joy(update: Update, context):
    await update.message.reply_text(
        "🎬 Mini Zetsu\n\n"
        "Partage tes vidéos avec tes amis 🎥\n"
        "Like, commente et abonne-toi ❤️\n"
        "Rejoins la communauté dès maintenant ! 🚀"
    )

# Commande /info
async def info(update: Update, context):
    await update.message.reply_text(
        "📊 Mini Zetsu en chiffres :\n\n"
        "• Lancement prévu : 2025\n"
        "• Plateformes : iOS, Android, Web\n"
        "• Gratuit : Toujours !\n\n"
        "Plus d'infos bientôt... 🔥"
    )

# Commande /contact
async def contact(update: Update, context):
    await update.message.reply_text(
        "📧 Nous contacter :\n\n"
        "Email : joypurge@proton.me\n"
        "Twitter : @JoyPurge\n"
        "Instagram : @joypurge_official\n\n"
        "💬 Réponse sous 24h !"
    )

# Commande /aide
async def aide(update: Update, context):
    await update.message.reply_text(
        "📋 LISTE DES COMMANDES :\n\n"
        "/start - Message d'accueil\n"
        "/joy - Présentation de l'app\n"
        "/info - Infos et dates\n"
        "/contact - Nous contacter\n"
        "/aide - Cette liste\n\n"
        "💡 Envoie n'importe quel message, je répondrai !"
    )

# Réponse aux messages normaux
async def repondre(update: Update, context):
    message = update.message.text.lower()
    
    if "bonjour" in message or "salut" in message:
        await update.message.reply_text("👋 Salut ! Bienvenue sur Mini Zetsu  !")
    elif "video" in message:
        await update.message.reply_text("🎥 Bientôt, tu pourras partager tes vidéos ici !")
    elif "abon" in message:
        await update.message.reply_text("📢 Abonne-toi pour ne rien rater du lancement !")
    else:
        await update.message.reply_text(
            "🤖 Je suis le bot officiel de zetsu  !\n"
            "Tape /aide pour voir les commandes."
        )

# Configuration du bot
app = Application.builder().token(TOKEN).build()

# Ajouter les commandes
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("joy", joy))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("aide", aide))

# Ajouter la réponse aux messages normaux
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repondre))

# Démarrer
if __name__ == "__main__":
    print("🤖 Mini  Zetsu est en ligne !")
    app.run_polling()
  by joyboy
