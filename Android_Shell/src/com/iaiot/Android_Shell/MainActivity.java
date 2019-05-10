package com.iaiot.Android_Shell;

import com.iaiot.Android_Shell.R;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebView;

public class MainActivity extends Activity {

	private WebView Android_Shell;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		Android_Shell = (WebView) findViewById(R.id.wv);
		
		Android_Shell.loadUrl("http://www.baidu.com");
	}
}
