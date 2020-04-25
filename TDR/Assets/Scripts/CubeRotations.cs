using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeRotations : MonoBehaviour
{
    public Collider coll;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject L1;
    public GameObject L2;
    public GameObject L3;
    public GameObject L4;
    public GameObject L6;
    public GameObject L7;
    public GameObject L8;
    public GameObject L9;
    public GameObject B2;
    public GameObject B8;
    public GameObject F2;
    public GameObject F8;
    public GameObject R1;
    public GameObject R2;
    public GameObject R3;
    public GameObject R4;
    public GameObject R6;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject U;
    public GameObject R;
    public GameObject F;
    public GameObject D;
    public GameObject L;
    public GameObject B;
    Vector3 inicialpos = new Vector3();
    Vector3 finalpos = new Vector3();
    Vector3 deltapos = new Vector3();
    private static bool mousepressed = false;
    private static bool hasrotated = false;
    private static int mousedir = 0;
    private static string rotationaxis = "";
    public int speed = 2;
    public int speedx = 3;
    public float correction = 55;
    private LayerRotation layerRotation;
    GameObject uchild;
    GameObject rchild;
    GameObject fchild;
    GameObject dchild;
    GameObject lchild;
    GameObject bchild;

    void Awake()
    {
        layerRotation = Cube.GetComponent<LayerRotation>();
    }
    void Start()
    {
        coll = GetComponent<Collider>();
    }

    void Update()
    {      
        deltapos.Set(0, 0, 0);
        if (Input.GetMouseButtonDown(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (!coll.Raycast(ray, out hit, 100.0f))
            {
                mousepressed = true;
                Cube2.transform.parent = Cube.transform;
                inicialpos = Input.mousePosition;
            }
        }
        if (mousepressed && !hasrotated)
        {
            
            if (mousedir == 0)
            {
                deltapos = Input.mousePosition - inicialpos;
                if (Mathf.Abs(deltapos.x) > Mathf.Abs(deltapos.y))
                {                   
                    Cube.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);                   
                    mousedir = 1;
                }
                if (Mathf.Abs(deltapos.x) < Mathf.Abs(deltapos.y))
                {
                    if (inicialpos.x < Screen.width / 2)
                    {
                        Cube.transform.Rotate(speedx * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
                        rotationaxis = "x";
                    }
                    if (inicialpos.x > Screen.width / 2)
                    {
                        Cube.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
                        rotationaxis = "z";
                    }
                    mousedir = 2;
                }
            }
            if (mousedir == 1)
            {
                if (Mathf.Abs(Cube.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.y) < 271.5)
                {
                    
                    Cube.transform.rotation = Quaternion.Euler(0, -90, 0);
                    hasrotated = true;
                }
                if (Mathf.Abs(Cube.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.y) < 91.5)
                {
                    Cube.transform.rotation = Quaternion.Euler(0, 90, 0);
                    hasrotated = true;
                }
                else
                {
                    Cube.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                }                              
            }
            if (mousedir == 2)
            {
                if (rotationaxis == "x")
                {
                    if (Mathf.Abs(Cube.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.x) < 271.5)
                    {
                        Cube.transform.rotation = Quaternion.Euler(-90, 0, 0);
                        hasrotated = true;
                    }
                    if (Mathf.Abs(Cube.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.x) < 91.5)
                    {
                        Cube.transform.rotation = Quaternion.Euler(90, 0, 0);
                        hasrotated = true;
                    }
                    else
                    {
                        Cube.transform.Rotate(speedx * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
                    }                   
                }
                if (rotationaxis == "z")
                {
                    if (Mathf.Abs(Cube.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.z) < 271.5)
                    {
                        Cube.transform.rotation = Quaternion.Euler(0, 0, -90);
                        hasrotated = true;
                    }
                    if (Mathf.Abs(Cube.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(Cube.transform.rotation.eulerAngles.z) < 91.5)
                    {
                        Cube.transform.rotation = Quaternion.Euler(0, 0, 90);
                        hasrotated = true;
                    }
                    else
                    {
                        Cube.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
                    }
                }
            }
        }
        if (Input.GetMouseButtonUp(0))
        {
            finalpos = Input.mousePosition;
            deltapos = finalpos - inicialpos;
            if (mousedir == 1)
            {
                if (Cube.transform.rotation.eulerAngles.y > 330)
                {
                    Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (Cube.transform.rotation.eulerAngles.y > 265)
                    {
                        Cube.transform.rotation = Quaternion.Euler(0, -90, 0);
                        layerRotation.uprime();
                        layerRotation.e();
                        layerRotation.d();
                        reset();
                    }
                    else
                    {
                        if (Cube.transform.rotation.eulerAngles.y > 30)
                        {
                            Cube.transform.rotation = Quaternion.Euler(0, 90, 0);
                            layerRotation.u();
                            layerRotation.eprime();
                            layerRotation.dprime();
                            reset();
                        }
                        else
                        {
                            Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }                
            }
            if (mousedir == 2)
            {
                if (rotationaxis == "x")
                {
                    if (Cube.transform.rotation.eulerAngles.x > 330)
                    {
                        Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (Cube.transform.rotation.eulerAngles.x > 265)
                        {
                            Cube.transform.rotation = Quaternion.Euler(-90, 0, 0);
                            layerRotation.rprime();
                            layerRotation.m();
                            layerRotation.l();
                            reset();
                        }
                        else
                        {
                            if (Cube.transform.rotation.eulerAngles.x > 30)
                            {
                                Cube.transform.rotation = Quaternion.Euler(90, 0, 0);
                                layerRotation.r();
                                layerRotation.mprime();
                                layerRotation.lprime();
                                reset();
                            }
                            else
                            {
                                Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                }
                if (rotationaxis == "z")
                {
                    if (Cube.transform.rotation.eulerAngles.z > 330)
                    {
                        Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (Cube.transform.rotation.eulerAngles.z > 265)
                        {
                            Cube.transform.rotation = Quaternion.Euler(0, 0, -90);
                            layerRotation.f();
                            layerRotation.s();
                            layerRotation.bprime();
                            reset();
                        }
                        else
                        {
                            if (Cube.transform.rotation.eulerAngles.z > 30)
                            {
                                Cube.transform.rotation = Quaternion.Euler(0, 0, 90);
                                layerRotation.fprime();
                                layerRotation.sprime();
                                layerRotation.b();
                                reset();
                            }
                            else
                            {
                                Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                }
            }
            rotationaxis = "";
            Cube2.transform.parent = null;
            Cube.transform.rotation = Quaternion.Euler(0, 0, 0);
            mousedir = 0;
            mousepressed = false;
            hasrotated = false;
        }
    }
    public void reset()
    {
        uchild = U.transform.GetChild(0).gameObject;
        uchild.transform.parent = null;
        U.transform.rotation = Quaternion.Euler(0, 0, 0);
        U.transform.position = new Vector3(0, 4, 0);
        uchild.transform.parent = U.transform;
        fchild = F.transform.GetChild(0).gameObject;
        fchild.transform.parent = null;
        F.transform.rotation = Quaternion.Euler(0, 0, 0);
        F.transform.position = new Vector3(0, 2, -2);
        fchild.transform.parent = F.transform;
        dchild = D.transform.GetChild(0).gameObject;
        dchild.transform.parent = null;
        D.transform.rotation = Quaternion.Euler(0, 0, 0);
        D.transform.position = new Vector3(0, 0, 0);
        dchild.transform.parent = D.transform;
        bchild = B.transform.GetChild(0).gameObject;
        bchild.transform.parent = null;
        B.transform.rotation = Quaternion.Euler(0, 0, 0);
        B.transform.position = new Vector3(0, 2, 2);
        bchild.transform.parent = B.transform;
        rchild = R.transform.GetChild(0).gameObject;
        rchild.transform.parent = null;
        R.transform.rotation = Quaternion.Euler(0, 0, 0);
        R.transform.position = new Vector3(2, 2, 0);
        rchild.transform.parent = R.transform;
        lchild = L.transform.GetChild(0).gameObject;
        lchild.transform.parent = null;
        L.transform.rotation = Quaternion.Euler(0, 0, 0);
        L.transform.position = new Vector3(-2, 2, 0);
        lchild.transform.parent = L.transform;
    }
}
