class config:
    BOT_TOKEN = "1720686387:AAFAVz_7De_zX3DADIBTEQ6wudLNmrUDL78"
    APP_ID = "2403280"
    API_HASH = "c38aebd98ee37c86d585678dc4b44c66"
    DATABASE_URL = "postgres://rgzfizxotdnejq:0008056f777e9652f8dafb51866161f23fa0c6c187ac53a12bd39e7c0bee3e6a@ec2-3-215-40-176.compute-1.amazonaws.com:5432/d7tis35cbvm46c"
    SUDO_USERS = "1082702383" # Sepearted by space.
    SUPPORT_CHAT_LINK = "https://t.me/danuma01"
    DOWNLOAD_DIRECTORY = "./downloads/"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  Ytdl = ['ytdl']

class Messages:
    START_MSG = "**ආයුබෝවන් {}**\n  ප්‍රථම සිංහල Google Drive bot  වෙත සාදරයෙන් පිලිගන්නවා\n Bot බාවිතා කරන ආකාරය ගැන දැනගැනීමට /help විදානය බාවිතා කරන්න...."

    HELP_MSG = [
        ".",
        "**SL Gdrive Uploder**\n ඔබ ලබාදෙන direct link එකක් හෝ Telegram Files ඩේටා වියදමකින් තොරව ඔබගේ Drive ෆෝල්ඩරය වෙත uplode කිරීමට මට පුළුවන්. ඊට අවශ්‍ය වන්නේ Gdrive අවසර ලබාදීම පමණි.__\n\n මට තවත් විශේෂාංග තිබේ ...! ඒ ගැන දැන ගැනීමට අවශ්යද? පහත බොත්තම් උපයෝගී කරගෙන තවත් විස්තර ලබාගන්න ",
        
        f"**Google Drive වෙත අවසර ගැනීමට**\n /{BotCommands.Authorize[0]} ලෙස ටයිප් කර මට එවූ විට ලැබෙන URL වීවෘත කර අදාල උපදෙස් පිලිපැදීමෙන් ලැබෙන **කේතය** මට එවන්න. අවසර ලබාදුන් ගිනුමක් ඉවත් කිරීමට මෙම විදානය යොදාගන්න /{BotCommands.Revoke[0]} \n\n**Note: අවසර ලබාදෙන තුරු මෙය කිසිවකට ප්‍රතිචාර නොදක්වයි !**",
        
        f"**Direct Links**\n  direct download link එකක් එවූ විට කෙලින්ම ඔබගේ Drive ගිණුමට උඩු ගත කල හැකි අතර  files rename කර උඩුගත කිරිඉමට මේ ආකාරය යොදාගන්න **\n\n ```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n **Telegram Files**\n ලේසිම ක්‍රමය 😁 ගිණුමට අවසර ලබාදුන් පසු බොත වෙත ෆෝවඩ් කරන files ඔබගේ drive ගිණුමට උඩුගත වේ.  Note: Telegram File එකෙහි විශාලත්වය මත උඩුගත වන කාලය වෙනස් විය හැක \n\n **YouTube-DL Support**\n YOUTUBE වීඩියෝ කෙලින්ම drive ගිණුම යැවීමට වලංගු යුඋටියුබ් ලින්කුවක් බොට් වෙත එවන්න \nUse /{BotCommands.Ytdl[0]} ඉබෙම උඩුගත වුයේ නැතිනම් මෙම විධානය ලිෂ්කුවට රිප්ලයි කරන්න",
        
        f"**Custom Folder for Upload**\n **TeamDrive** තුල වෙනත් ෆෝල්ඩරයක් සාදාගැනීමට \nUse /{BotCommands.SetFolder[0]} (Folder URL/drive ගිණුම තුල ඔබ සෑදු ෆෝල්ඩරයට අදාල ලින්කුව ) ලෙස බොට් වෙත එවන්න .\n ඉන්පසු ඔබ උඩුගත කරන සියල්ල ඒ තුලට උඩුගත වනු ඇත ",
        
        f"**Delete Google Drive Files**\n drive ගිණුමෙහි ඇති FILE හෝ ෆෝල්ඩර් Delete කිරිඉමට  /{BotCommands.Delete[0]} (File/Folder URL) ලෙස බෝට් වෙත එවන්න .\n එලෙසම TRASH files delete කිරිමට  /{BotCommands.EmptyTrash[0]} විධානය දෙන්න \n Note: අදාල ගොනු සදාකාලිකව මකියනුඇත. \n",
        
        "**Rules & Precautions**\n__1. කිසිවිටෙකත් විශාල files කොපි කිරිඉමෙන් වලකින්න .එමගින් බොට් හෝ ඔබගේ ගොනු විකුර්ති විය හැක  \n2.වරකට එක ඉල්ලීමක් බැගින් බොට් වෙත යොමු කරන්න..\n3. Don't send slow  it first.\n4. බොට්ව අවබාවිතයෙන් වලකින්න ඔබව බෑන් විය හැක",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by SLdevilX**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **දිනකට ලබාදෙන ප්‍රමනය ඔබ බාවිතා කර අවසන් **\n බොට් UPGRADE කරගන්න හෝ පය 24 කින් පසුව උත්සහ කරන්න "
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder සොයාගත නොහැක .**\n__File id - {} 😒 . එය වලංගු ගොනුවක්ද හා ඔබ නිසිලෙස ගිණුමට අවසර ලබාගෙනද යන්න සොයා බලන්න "
    
    INVALID_GDRIVE_URL = "❗ **වැරදි Google Drive URL එකකි **\n නිවැරදි ලින්කුවක් එවන්න "
    
    COPIED_SUCCESSFULLY = "✅ **සාර්ථකව COPY කරනලදී**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **ඔබ කිසිදු ගිණුමක් සදහා අවසර ලබාගෙන නැත **\n /{BotCommands.Authorize[0]} විධානය මගින් අවසර ලබාදෙන්න "
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **සාර්ථකව උඩුගතවිය .**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**බාගත කිරීමට නොහැක**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **බාගතවෙමින් පවතී...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **ඔබ ගිණුමකට අවසර සපුරා ඇත**\n /revoke එවා ගිණුම විසන්දිකර නැවත උත්සාහ කරන්න."
    
    FLOW_IS_NONE = f"❗ **වැරදි කේතයකි**\n {BotCommands.Authorize[0]} සත්‍යාපනය වී නැවත උත්සහ කරන්න."
    
    AUTH_SUCCESSFULLY = '🔐 **සාර්ථකව ගිණුමට අවසර ලබාගන්නා ලදී**'
    
    INVALID_AUTH_CODE = '❗ **වැරදි කේතයකි**\n එවූ කේතය පෙර බාවිතා කල හෝ වැරදි කේතයකි . මුල සිට අරඹා නව කේතයක් ලබාගන්න'
    
    AUTH_TEXT = "⛓️ **ඔබගේ Google ගිණුම සමග සම්බන්ධ වීමට  [URL]({})  හරහා ගොස් ලබාගත් කේතය බොට් වෙත එවන්න  **\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"
    
    DOWNLOAD_TG_FILE = "📥 **බාගතවෙමින් පවතී...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **එවූ නව ෆෝල්ඩරයේ ලින්කුව සාර්ථකව සකසන ලදී.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **එම  Folder ID සාර්ථකව මකාදමන ලදී.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **වත්මන් ෆෝල්ඩරයේ අංකය (ID) - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **පැවති ගිණුමෙන් සාර්ථකව ඉවත්විය **\n නව ගිණුමක් එකතු කිරිමට /{BotCommands.Authorize[0]} විධානය යොදාගන්න"
    
    NOT_FOLDER_LINK = "❗ **වැරදි ෆෝල්ඩර් ලින්කුවක්**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Google Drive වෙත පිටපත් කරමින්...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ නිවැරදි  Google Drive URL එකක් නිවැරදි විධානය සමග එවන්න.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **ඔබගේ ගිණුමෙන් අවශ්‍ය තරම් අවසර ලැබී නොමැත**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ගොනුව සාර්ථකව මකාදමන ලදී**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: කුමක් හෝ වැරදි ඇත**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**ට්‍රෑෂ් ගොනු සාර්ථකව මකන ලදී!**"
    
    PROVIDE_YTDL_LINK = "❗**නිවැරදි YOUTUBE ලින්කුවක් එවන්න**"
