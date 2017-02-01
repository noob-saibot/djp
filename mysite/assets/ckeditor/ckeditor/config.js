/**
 * @license Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

//CKEDITOR.plugins.addExternal('eqneditor', 'http://192.168.0.105/static/ckeditor/ckeditor/plugins/');

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
//        config.extraPlugins = 'eqneditor';
//           config.extraPlugins = 'eqneditor';
        //   config.toolbar_Full.push(['eqneditor']);

config.pbckcode = {
    // An optional class to your pre tag.
    cls: '',

    // The syntax highlighter you will use in the output view
    highlighter: 'PRETTIFY',

    // An array of the available modes for you plugin.
    // The key corresponds to the string shown in the select tag.
    // The value correspond to the loaded file for ACE Editor.
    modes: [['HTML', 'html'], ['CSS', 'css'], ['PHP', 'php'], ['JS', 'javascript']],

    // The theme of the ACE Editor of the plugin.
    theme: 'textmate',

    // Tab indentation (in spaces)
    tab_size: '4'
  };

};
