public class Persona {
    
    private String nombre;
    private String tel;
    private String email;
    private int id;
    private static int numeroPersona = 0;

    //CONSTRUCTOR VACIO
    public Persona(){
        this.id = ++Persona.numeroPersona;
    }

    public Persona(String nombre, String tel,String email){
        this();
        this.nombre = nombre;
        this.tel = tel;
        this.email = email;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public static int getNumeroPersona() {
        return numeroPersona;
    }

    public static void setNumeroPersona(int numeroPersona) {
        Persona.numeroPersona = numeroPersona;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Persona [ id=" + id + ", nombre= "+ nombre + ", tel=" + tel + ", email=" + email +" ]";
    }

}

