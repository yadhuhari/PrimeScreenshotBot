class Messages:
    ADDED_TO_QUEUE = (
        "<b> Your request has been added to the queue. If you have more than {per_user_process_count} </b>"
        "<b> ongoing processes, then this process will only start after one of them finishes. </b>"
    )
    MEDIA_MESSAGE_DELETED = "<b> Why did you delete the file 😠, Now i cannot help you 😒. </b>"
    CANNOT_OPEN_FILE = "<b> 😟 Sorry! I cannot open the file. </b>"
    PROCESS_TIMEOUT = (
        "<b> 😟 Sorry! process failed due to timeout. Your process was </b>"
        "<b> taking too long to complete, hence cancelled. </b>"
    )
    TRACK_USER_ACTIVITY = "<b> User id: `{chat_id}` </b>"
    PROCESSING_REQUEST = "<b> Processing your request, Please wait! 😴 </b>"
    SCREENSHOT_AT = "<b> Screenshot at {time} </b>"
    SCREENSHOT_PROCESS_FAILED = "<b> 😟 Sorry! Screenshot generation failed possibly due to some infrastructure failure 😥. </b>"
    SCREENSHOT_PROCESS_SUCCESS = (
        "<b>🤓 You requested {count} screenshots and </b>"
        "<b> {total_count} screenshots generated, </b>"
        "<b> Now starting to upload! </b>"
    )
    PROCESS_UPLOAD_CONFIRM = (
        "<b> Successfully completed process in {total_process_duration}\n\n </b>"
        "<b> If You find me helpful, please rate me [here](tg://resolve?domain=botsarchive&post=1206). </b>"
    )
    WRONG_FORMAT = "<b> Please follow the specified format </b>"
    VIDEO_PROCESS_CAPTION = "<b> Sample video. {duration}s from {start} </b>"
    SCREENSHOTS_START = "<b> 😀 Generating screenshots!. </b>"

    SAMPLE_VIDEO_PROCESS_START = "<b> 😀 Generating Sample Video! This might take some time. </b>"
    SAMPLE_VIDEO_PROCESS_FAILED = "<b> 😟 Sorry! Sample video generation failed possibly due to some infrastructure failure 😥. </b>"
    SAMPLE_VIDEO_PROCESS_SUCCESS = (
        "<b> 🤓 Sample video was generated successfully!, Now starting to upload! </b>"
    )
    SAMPLE_VIDEO_PROCESS_FAILED_GENERATION = (
        "<b> stream link : {file_link}\n\n duration {sample_duration} sample video </b>"
        "<b> generation failed\n\n{ffmpeg_output} </b>"
    )
    SAMPLE_VIDEO_PROCESS_OPEN_ERROR = (
        "<b> stream link : {file_link}\n\nSample video requested\n\n{duration} </b>"
    )

    SCREENSHOTS_PROGRESS = "<b> 😀 `{current}` of `{total}` generated! </b>"
    MANUAL_SCREENSHOTS_OPEN_ERROR = (
        "<b> stream link : {file_link}\n\nRequested manual screenshots\n\n{duration} </b>"
    )
    MANUAL_SCREENSHOTS_NO_VALID_POSITIONS = (
        "<b> 😟 Sorry! None of the given positions where valid! </b>"
    )
    MANUAL_SCREENSHOTS_VALID_PISITIONS_ABOVE_LIMIT = (
        "<b> 😟 Sorry! Only 10 screenshots can be generated. Found {valid_positions_count} </b>"
        "<b> valid positions in your request </b>"
    )
    MANUAL_SCREENSHOTS_INVALID_POSITIONS_ALERT = (
        "<b> Found {invalid_positions_count} invalid positions ({invalid_positions}).\n\n </b>"
        "<b> 😀 Generating screenshots after ignoring these!. </b>"
    )
    MANUAL_SCREENSHOTS_FAILED_GENERATION = (
        "<b> stream link : {file_link}\n\nmanual screenshots {raw_user_input}. </b>"
    )
    TRIM_VIDEO_INVALID_RANGE = "<b> The range you provided is invalid! </b>"
    TRIM_VIDEO_DURATION_ERROR = (
        "<b> Please provide any range that's upto {max_duration}s. </b>"
        "<b> Your requested range **{start}:{end}** is `{request_duration}s` long! </b>"
    )
    TRIM_VIDEO_OPEN_ERROR = "<b> stream link : {file_link}\n\ntrim video requested\n\n{start}:{end}\n\n{duration} </b>"
    TRIM_VIDEO_RANGE_OUT_OF_VIDEO_DURATION = (
        "<b> 😟 Sorry! The requested range is out of the video's duration!. </b>"
    )
    TRIM_VIDEO_PROCESS_FAILED = (
        "<b> 😟 Sorry! video trimming failed possibly due to some infrastructure failure 😥. </b>"
    )
    TRIM_VIDEO_PROCESS_FAILED_GENERATION = "<b> stream link : {file_link}\n\nVideo trim failed.\n\n{start}:{end}\n\n{ffmpeg_output} </b>"
    TRIM_VIDEO_PROCESS_SUCCESS = (
        "<b> 🤓 Video trimmed successfully!, Now starting to upload! </b>"
    )
    TRIM_VIDEO_START = "<b> 😀 Trimming Your Video! This might take some time. </b>"

    SCREENSHOTS_OPEN_ERROR = "<b> stream link : {file_link}\n\nRequested screenshots: {num_screenshots}.\n\n{duration} </b>"
    SCREENSHOTS_FAILED_GENERATION = (
        "<b> stream link : {file_link}\n\n{num_screenshots} screenshots where requested </b>"
        "<b> and Screen shots where not generated. </b>"
    )

    SETTINGS = "<b> Here You can configure my behavior.\n\nPress the button to change the settings. </b>"

    MEDIAINFO_START = "<b> Finding the media info, media info will be send here shortly! </b>"
