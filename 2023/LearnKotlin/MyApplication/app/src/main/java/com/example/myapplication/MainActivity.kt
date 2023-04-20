package com.example.myapplication

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.view.View
import android.view.inputmethod.EditorInfo
import android.view.inputmethod.InputMethodManager
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Toast
import com.example.myapplication.databinding.ActivityMainBinding



class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    var DataList = arrayListOf(
        Data(R.drawable.sample, "0번"),
        Data(R.drawable.sample, "1번"),
        Data(R.drawable.sample, "2번"),
        Data(R.drawable.sample, "3번")
    )
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
//        setContentView(R.layout.activity_main)
        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)
        binding.listView.adapter = CustomAdapter(this,DataList)




        }

    /*    val item = arrayOf("0번","1번","2번","3번","4번","5번","6번","7번","8번","9번")
        binding.listView.adapter = ArrayAdapter(this,android.R.layout.simple_list_item_1, item)*/

    }
   /* fun Login(v: View) {
        var imm = getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
        imm.hideSoftInputFromWindow(v.windowToken, 0)
        startActivity(Intent(this,LoginActivity::class.java))
    println("성공")
    }

    fun LoadImage(v: View) {
        startActivityForResult(Intent(Intent.ACTION_PICK, MediaStore.Images.Media.INTERNAL_CONTENT_URI), 0)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if(data!= null) binding.ivBasic.setImageURI(data?.data)
    }*/

