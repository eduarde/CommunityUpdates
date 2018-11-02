function CustomFileBrowser(field_name, url, type, win) {

    var cmsURL = '/backoffice/filebrowser/browse/?pop=2';
    cmsURL = cmsURL + '&type=' + type;

    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 980,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'no',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no'
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

function CharactersCounterInit(inst) {
    // initialize characters counters for tinymce field
    django.jQuery('#' + inst.editorId).next().after('<div class="counter"></div>');
    CharactersCounterUpdate(inst);
}

function CharactersCounterUpdate(inst) {
    var characters_counter = django.jQuery(inst.getContent()).text().length;
    django.jQuery('#' + inst.editorId).next().next().text('Characters: ' + characters_counter);
}


tinyMCE.init({

    // see http://www.tinymce.com/wiki.php/Configuration

    init_instance_callback: "CharactersCounterInit",

    setup: function (ed) {
        ed.onKeyUp.add(function (ed, e) {
            CharactersCounterUpdate(ed);
        });
    },

    // Init
    mode: 'textareas',
// # deactivating as it puts the widget on every single textarea
    theme: 'advanced',
    skin: 'grappelli',
    selector: '#newsletter_form textarea, #achievement_form textarea, #newsletter_item0 textarea',


    // General
    accessibility_warnings:
        false,
    browsers:
        'gecko,msie,safari,opera',
    dialog_type:
        'window',
    editor_deselector:
        'mceNoEditor',
    keep_styles:
        false,
    language:
        'en',
    object_resizing:
        false,
    plugins:
        'advimage,advlink,fullscreen,paste,media,searchreplace,grappelli,template,table',
    // directionality : "rtl",

    // Callbacks
    file_browser_callback:
        'CustomFileBrowser',

    // Cleanup/Output
    element_format:
        'xhtml',
    fix_list_elements:
        true,
    forced_root_block:
        'p',
    // style formsts overrides theme_advanced_styles
    // see http://www.tinymce.com/wiki.php/Configuration:style_formats
    style_formats:
        [
            {title: 'Paragraph Small', block: 'p', classes: 'p_small'},
            {title: 'Paragraph ImageCaption', block: 'p', classes: 'p_caption'},
            {title: 'Clearfix', block: 'p', classes: 'clearfix'},
            {title: 'Code', block: 'p', classes: 'code'}
        ],
    verify_html:
        true,

    // URL
    relative_urls:
        false,
    remove_script_host:
        true,

    // Layout
    width:
        758,
    height:
        300,
    indentation:
        '10px',

    // Content CSS
    // customize your content ...
    // content_css : "css/example.css",

    // Theme Advanced
    theme_advanced_toolbar_location:
        'top',
    theme_advanced_toolbar_align:
        'left',
    theme_advanced_statusbar_location:
        'bottom',
    theme_advanced_buttons1:
    'formatselect,styleselect,|,bold,italic,underline,|' +
    ',justifyleft,justifycenter,justifyright,|,bullist,numlist,blockquote,|' +
    ',undo,redo,|,link,unlink,|,image,|,fullscreen,|,grappelli_adv',
    theme_advanced_buttons2:
    'search,|,pasteword,template,media,charmap,|,code,|' +
    ',tablecontrols,table,cleanup,grappelli_documentstructure',
    theme_advanced_buttons3:
        '',
    theme_advanced_path:
        false,
    theme_advanced_blockformats:
        'p,h1,h2,h3,h4,pre',
    theme_advanced_resizing:
        true,
    theme_advanced_resize_horizontal:
        false,
    theme_advanced_resizing_use_cookie:
        true,

    // Image Plugin
    // see http://www.tinymce.com/wiki.php/Plugin:advimage
    theme_advanced_styles:
        'Image Left=img_left;Image Right=img_right;Image Block=img_block',
    advimage_update_dimensions_onchange:
        true,

    // Link Settings
    // see http://www.tinymce.com/wiki.php/Plugin:advlink
    advlink_styles:
        'Internal Link=internal;External Link=external',

    // Media Plugin
    // see http://www.tinymce.com/wiki.php/Plugin:media
    media_strict:
        true,

    // Grappelli Settings
    grappelli_adv_hidden:
        false,
    grappelli_show_documentstructure:
        'on'

})
;

